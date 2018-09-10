# python_client_server


A client server application .

#Logic of the application 

We publish  2 endpoints that can increase and decrease the value of a global parameter stored in our service.
In our service we maintain logic such as we do not allow the value of this parameter to be either larger of 100 or less that -100.

Our endpoints published give the possibility to the user to select the value that will be added or reduced from the global param


#Tech details

Python 2.7.13 :: Anaconda custom (x86_64)

python service_starter.py runs on localhost:5000
python atm_client.py sends requests to localhot:5000

file service_starter.py is our microservice implemented using flask
file atm_client.py is a small application that uses the endpoints published by the service starter app

endpoints
/increase?value=x
/decrease?value=x


