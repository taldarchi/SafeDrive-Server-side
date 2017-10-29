Safedrive server side.

Using heroku as the host: colmansafedrive.herokuapp.com

Web server is built using Django REST framework in python.

###Screens:
---
##### Website:
<img src="/Capture.PNG" alt="com" width="800" height="500"/>


#Querying the server:

* List of drivers: 

```bash
$ curl http://colmansafedrive.herokuapp.com/api/v1/safedrive/drivers/
>> {
        "id": 1,
        "user": {
            "id": 1,
            "username": "rave"
        },
        "name": "r",
        "creation_date": "2017-05-20",
        "driving_data": "http://colmansafedrive.herokuapp.com/api/v1/safedrive/data-drivers/1/"
    },
    {
        "id": 2,
        "user": {
            "id": 2,
            "username": "taldarchi"
        },
        "name": "s",
        "creation_date": "2017-05-24",
        "driving_data": "http://colmansafedrive.herokuapp.com/api/v1/safedrive/data-drivers/2/"
    },
```   

* Drive details

```bash
$ curl http://colmansafedrive.herokuapp.com/api/v1/safedrive/data-drivers/
>>     {
        "id": 4,
        "data": [
            [
                {
                    "accelerator": "-1",
                    "load": "48.627453",
                    "throttle": "20.784313",
                    "gps": {
                        "lat": "31.95804896",
                        "lon": "34.7910002"
                    },
                    "rpm": "2199",
                    "time": 1496686810935,
                    "speed": "30",
                    "maximum_limition_of_speed": -1
                },
                {
                    "accelerator": "-1",
                    "load": "47.843136",
                    "throttle": "21.17647",
                    "gps": {
                        "lat": "31.95804896",
                        "lon": "34.7910002"
                    },
                    "rpm": "2335",
                    "time": 1496686812148,
                    "speed": "33",
                    "maximum_limition_of_speed": -1
                },
                
                ...
```   

