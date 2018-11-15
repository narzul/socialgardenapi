import socialgardenapi
import serial
from time import sleep

#Time_Stamp:0
#Frequency:1
#VImax:2
#VImin:3
#RMS:4
#Phas:5
#VVmax:6
#VVmin:7
#Corr:8
#CH2_VI_max:9
#CH2_VI_min:10
#CH2_RMS:11
#CH2_Phas:12
#CH2_VV_max:13
#CH2_VV_min:14
#CH2_Corr:15
#t_PCB:16
#t_thermost:17
#Magnetometer_X:18
#Magnetometer_Y:19
#Magnetometer_Z:20
#Accelerometer_X:21
#Accelerometer_Y:22
#Accelerometer_Z:23
#External_temperature:24
#External_light:25
#External_humidity:26
#CH1_Differential_potential:27
#CH2_Differential_potential:28
#RF_power:29
#Transpiration_sensor:30
#Sap_flow:31
#Air_pressure:32

DataArray=[["Time_Stamp","Frequency","VImax","VImin","RMS","Phas","VVmax","VVmin","Corr","CH2_VI_max","CH2_VI_min","CH2_RMS","CH2_Phas","CH2_VV_max","CH2_VV_min","CH2_Corr","t_PCB","t_thermost","Magnetometer_X","Magnetometer_Y","Magnetometer_Z","Accelerometer_X","Accelerometer_Y","Accelerometer_Z","External_temperature","External_light","External_humidity","CH1_Differential_potential","CH2_Differential_potential","RF_power","Transpiration_sensor","Sap_flow","Air_pressure"],[None]*33]
Messurment_time = "10000*"

#Serial setup
ser = serial.Serial(
	port='/dev/ttyACM0',
	baudrate=625000,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout = 0
)

def read_data_setup(input):
	count = 0
	count_read_flag = False
	ser.write(input)
	sleep(1)
        while True:
                data = ser.readline()
                if data:
                        print(data)
			count_read_flag = True
		elif count < 3 and count_read_flag==False:
			sleep(1)
			count += 1
			ser.write(input)
		else:
			break

#Serial Start
ser.close()
ser.open()
read_data_setup("mp*")
read_data_setup("ss*")
read_data_setup("mi"+Messurment_time)
read_data_setup("ss*")

def read_data():
	while True:
                data = ser.readline()
		if data and data !="Z" and data != "A":
			data = data.replace("\r\n","")
			words = data.split(" ")
			if len(words) >= 33:
				for i in range(len(words)):
					DataArray[1][i] = words[i]
				socialgardenapi.insertStream("Test65", "Test65 to next 64",'[{"Name":"HHHH","Value":'+DataArray[1][2]+'}]')
				#print("Test64", "Test64 used for Mu.",'[{"Name":'+DataArray[0][2]+',"Value":'+str(DataArray[1][2])+'},{"Name":'+DataArray[0][3]+',"Value":'+str(DataArray[1][3])+'},{"Name":'+DataArray[0][15]+',"Value":'+str(DataArray[1][15])+'},{"Name":'+DataArray[0][24]+',"Value":'+str(DataArray[1][24])+'},{"Name":'+DataArray[0][28]+',"Value":'+str(DataArray[1][28])+'}]')
ser.write("ms*")
read_data()
