RESTful Server Architecture Test
You have 7 days to complete this test. Upon completion please provide either automated tests or instructions on how to test the server application within a README.md file.
SERVER SPECIFICATION
Create a Python with Django/Django Rest Framework server program that can receive HTTP requests with a JSON formatted body payload. Based on the requests that this server program receives, this program should be able store a list of vehicles that are in the garage, as well as some relevant information on each one. The different types of vehicles are as follows: car, truck, and boat.
Following REST Pattern, the following HTTP Methods should correspond to the operations noted below.
AUTHENTICATION
You are required to create an authentication flow for the server application. All routes must be protected against anonymous usage.
Our recommendation is to use a token-based scheme utilizing the JWT standard, but that is not a requirement. Creating an authentication flow may require you to make user accounts to go along with the resources that are detailed below. You get to decide that though.
CARS RESOURCE
  
CAR - /cars
Make 
Model 
Year 
Seats 
Color 
VIN 
Current Mileage 
Service Interval 
Next Service 


Truck - /trucks
Make 
Model 
Year 
Seats 
Bed Length 
Color 
VIN 
Current Mileage 
Service Interval 

Boat - /boats
Make 
Model 
Year 
Length 
Width 
HIN 
Current Hours 
Service Interval 
Next Service 


LIST /cars
READ /cars/id
CREATE cars/
UPDATE cars/id
DELETE cars/id



To run tests:
- go to a project directory
- creare and/or activate virtual environment
- install required packeges `pip install -r requirements.txt`
- run tests  `python manage.py test`
