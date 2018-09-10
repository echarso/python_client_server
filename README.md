# Simple server client python app



## Logic of the application 

We publish  2 endpoints that can increase and decrease the value of a global parameter stored in our service.
In our service we maintain logic such as we do not allow the value of this parameter to be either larger of 100 or less that -100.

Our endpoints published give the possibility to the user to select the value that will be added or reduced from the global param


## Tech details

Python 2.7.13 :: Anaconda custom (x86_64)

### micro service execution 
how to run -> python service_starter.py 
flask is used and listens on localhost:5000
endpoints
/increase?value=x
/decrease?value=x

Flask has been used.

### python client code 
how to run -> python atm_client.py 
sends requests to localhot:5000

endpoints
/increase?value=x
/decrease?value=x


