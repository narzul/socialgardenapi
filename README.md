# Social garden python API client
Python version 2.7

If running on computer with later version, then run by the following command in front of all calls, such as following:
```
Python2.7 send-to-server-example.py
```

##### Year - 2018 IT-University of Copenhagen, Denmark
The Social garden API is a client site tool for sending and retrieving data from the Social garden database.

The API, has been setup to send REST CRUD (Create, Read, Update and Delete) operations to the database via a web service. Researchers can thus use this API in order to connecting devices and sensors to a central server.
This package can be imported into any other python package by downloading the package to the same folder.


## Installation guide

In order to use the API, clone the root repository via terminal or github UI.
```
git clone https://github.com/RohlederCPH/socialgarden
```
enter the python folder through the terminal or cmd (Command Prompt)

```
cd socialgarden/python
```

The API uses geocoder in order to find the coordinates of the device, based on IP.
```
pip2.7 install geocoder
```

## Use cases
Whenever the social garden API client is used, it has to be imported as is standard for python programs.
We have two basic usecases: send data and retrieve data. Futhermore all the data can be looked up via the socailgarden website (currently in beta): [Socialgarden website](http://159.65.116.139:3000/)

If you run send-to-server-example.py and get-data-from-server-example.py at the same time, from two terminals, you see how the API should be used for communication between sensors and database. The sensor should be implemented as the send-to-server-example.py.

When one wishes to work with the data, it can be done as in get-data-from-server-example.py.



###### Now you should try the API!

## Test API
The following test will open multiple terminal windows in order to demo their usages.


```
 ./TEST-API.sh
```


## Individual parts of the test
in terminal 1
```
python2.7 send-to-serve-example.py
```
in terminal 2
```
python2.7 get-data-from-server-example.py
```
in terminal 3
```
python2.7  get-attributes-example.py
```

### Sending data to server
Data can be send to the server as shown in the following example:

###### Example send-to-server-example.py
```
import socialgardenapi
import time
for x in range(0, 100):
    socialgardenapi.insertStream("myStream", "Beskrivelse",'{"Name":"light","Value":10}')
    time.sleep(0.2)
    socialgardenapi.insertStream("myStream", "Beskrivelse",'{"Name":"water","Value":20}')
    time.sleep(0.2)
```

### Retrieving data from server
Data can be retrieved as in the following example:


###### Example get-data-from-server-example.py
```
import socialgardenapi
print('Starting listener')
while True:
    print( socialgardenapi.getNewData("myStream") )
```

###### Example Response data as json
```
{
  u 'DeviceName': u 'devices',
  u 'Description':
  u 'Beskrivelse',
  u 'TimeStamp': u '2018-06-20 18:04:08.924477',
  u '__v': 0, u 'Location': {
    u 'Latitude': u '55.6667',
    u 'Longitude': u '12.5833'
  }, u 'updatedAt': u '2018-06-20T18:04:08.939Z', u '_id': u '5b2a97181832ed04c7a19640', u 'Sensor': [{
    u '_id': u '5b2a97181832ed04c7a19641',
    u 'Name': u 'light',
    u 'Value': u '10'
  }], u 'createdAt': u '2018-06-20T18:04:08.939Z'
}
```
### Get specific attributes from stream
###### Example get-attribute-example.py
if you have desire to get a specific attribute, it can be accomplished like so. In this case we get the TimeStamp and the StreamName.
```
import socialgardenapi
print('Starting listener')
while True:
    resp = socialgardenapi.getNewData("myStream")
    print("TimeStamp: " + resp['TimeStamp'])
    print("StreamName: " + resp['StreamName'])
```
###### Returned data
```
TimeStamp: 2018-06-20 20:53:57.936449
StreamName: myStream
```
###### Callable attributes
```
  DeviceName - is the database streamname
  Description - description of dat
  TimeStamp - TimesStamp in the following form  '2018-06-20 18:04:08.924477'
  Location: {
    Latitude: '55.6667',
    Longitude:'12.5833'
  },
   updatedAt - returns a timestamp
   createdAt - returns a timestamp
   Sensor - return a list of sensors
```



## Methods
All getters return data as JSON.
```
getNewData(StreamName) - Get new data points, check every 0.5 sec.
streamExists(StreamName)  - Check if stream exists in database, return True or False.
getAllData(StreamName) - Get all data from stream.
getLastData(StreamName) - Get last data from stream.
insertStream(StreamName,  Description, Sensor[]) - insert new data, autogenerated coordinate.
insertStreamManualCoordinates(StreamName,  Description, Sensor[], Lat, Lng)- insert new data, manually generated coordinates.
deleteStream(StreamName) - Delete stream from database (Warning. this method will delete all data related to a stream)
```


### Using website for basic analysis
[Socialgarden website](http://159.65.116.139:3000/)

######  @ - Thomas Charles Rohleder - REAL - ITU

### Refrences
We are using [Skywind3000](https://github.com/skywind3000/terminal)'s python script to execute multiple terminal windows in our test



## Supported Curl commands
###### Get all data from Stream
```
curl -i -H "Accept: application/json" http://159.65.116.139:3000/devices/"StreamName"
```
###### Get last data from Stream
```
curl -i -H "Accept: application/json" http://159.65.116.139:3000/devices/"StreamName"/one
```

###### Post data to stream
```
curl -i -X POST -H "Content-Type: application/json" -d
'{"DeviceName": "StreamName",
"TimeStamp" :"datetime",
"Description":"Description",
"Location":{
  "Latitude":lat,
  "Longitude":lng,
  "ManuallyCoords":false
  },
"Sensor" :[
    {"Name":sensorName,"value":val},
    {"Name":sensorName,"value":val}
    ]}'
http://159.65.116.139:3000/devices/
```
###### Delete stream
```
curl -i -H "Accept: application/json" http://159.65.116.139:3000/devices/"StreamName"/delete
```
