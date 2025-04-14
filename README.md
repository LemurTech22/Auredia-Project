# Intern Auredia-Project

## User Management API Microservice

## Goal
Design a microservice-based API for user management using Docker and PostgreSQL. 

## Technical Requirements
* Containerize the application using Docker 
* Use PostgreSQL as the database 
* Create a Docker Compose configuration 
* Implement a robust user management service 
* Mandatory Components

## Technologies used:
* Flask
* Python
* PostgreSQL
* SQLAlchemy
* Flasgger/Swagger UI

# Pre-requisites before running the Code
* **Install Docker Desktop**

# Running the code
1. Clone the Repo into your favorite IDE
2. cd into Auredia_Project (check if you are in the correct directory). cd Auredia_Project
3. Build and start Docker containers: ``docker-compose up --build``

# Accessing the Interface
In the interface I used Swagger UI/ Flasgger to interact with the API. The API key is necessary to run the each CRUD functionality.
# Steps
1. After Docker is finished Running, Open any browser and insert this address: ``localhost:5000/apidocs/``
2. You should be greated with the interface with the CRUD functionalities of the API.
3. Insert the API Key. This allows access to using the API functionalities. Go to the Authorize Green button and insert the following API Key: ``bfcdtexzrofwtsdvfxmyrginsidaduxtnadlwjeynlsjgchussxrtzqdqhdfektptklucqtlxhatuctqcdbcyktzlarkkayndmktlkjaffxgvomsqaupvlxwnhehppat``. (FOR TESTING PURPOSES ONLY. LEAVING API KEYS IN REPOSITORIES IS A BIG NO NO.)
# Using the API
4. There are 4 different functionalities Insert, Gather, Update, and Delete. If you click on one of the functionalities it should have a dropdown and top right should be Try it now on each dropdown. The Database should be empty so try inserting data. <br/>This accepts a Json format and Inserting Information is the template as followed:
<br/>Template <br/>
```
{
  "email": "string",
  "first_name": "string",
  "last_name": "string",
  "user_name": "string"
}
```
You must fill out all the information inorder to insert data b/c it will throw errors.<br/>If all is well you should get a confirmation about the data you inserted and ID Number.<br/>
6. Getting Information:<br/>
   Clicking to Getting information you need the ID number from Creating a user: <br/>
```
{
   User_ID: insert ID number here
}
```
You should get the users information. 
<br/>If the user id doesnt exist then it throws a error.<br/>
7. Updating user information:<br/> 
You need the user ID to update information. You can update First and Last name, email and User Name. You can also update only one field as well.
```
  {
  user_id: textbox
  }
  
  {
    "email": "string",
    "first_name": "string",
    "last_name": "string",
    "user_name": "string"
  }
  
  or 
  
  {
    "first_name": "string"
  }
```
<br/>
8. Deleting User Information <br/>
Should be easy, just need the ID number to delete users. After deleting you should get confirmation that the user has been deleted.

```
{
  user_id: textbox
}
```
