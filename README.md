# CRUD_Project
# API Documentation

This README provides documentation for the APIs available in this Django project.

#### Create a User
-url: /api
-Method: 'POST'
-Description: The CreateUserView API allows you to create a new user by sending a POST request with the user's name and email in the request body. This API enforces validation to ensure that the name is a valid string containing only alphabetic characters and spaces and also that the email provided is valid. If the validation passes and the user is successfully created, the API will respond with the user's information in JSON format.


Request:

Method: POS

Endpoint: /api/users

Request Body:
{
  "name": "John Doe",
  
  "email": "johndoe@example.com"
  
}
Response:

Status Code: 200 OK

Response Body:
{
  "id": 123,
  
  "name": "John Doe",
  
  "email": "johndoe@example.com"
  
}
Error Responses:

If the provided name is not a valid string (contains non-alphabetic characters), the API will respond with a 400 Bad Request status and an error message.
If an error occurs during user creation for any other reason, the API will respond with a 400 Bad Request status and an error message describing the issue.

#### User Retrieval, Update, and Deletion

URL: /api/:identifier

HTTP Methods: GET, PUT, DELETE

Description:

The UserRetrieveUpdateDestroyView API allows you to perform various operations on a user resource by providing either the user's ID, name, or email as the :identifier parameter in the URL. This API provides the following functionality:

## Retrieve User Information
GET /api/users/:identifier

Retrieve user information by providing either the user's ID, name, or email as the :identifier parameter.
If found, the API will respond with the user's information serialized in JSON format.
If the provided :identifier cannot be converted to an integer, it is assumed to be a name, and the API searches for the user by name.

Example:
GET /api/johndoe

Response Body:

Status Code: 200 OK

{  id: 2
  "name": "Updated Name",
}



## Update User Information

PUT /api/users/:identifier

Update user information by providing the user's ID, name, or email as the :identifier parameter.
The updated user data should be included in the request body in JSON format.
If the user is found and the update is successful, the API will respond with the updated user information.

Request Body:
{
  "name": "Updated Name",
  
  "email": "updated.email@example.com"
  
}
Example:

PUT /api/123

Response Body:

Status Code: 200 OK

{  id: 2

  "name": "Updated Name",
  
  "email": "updated.email@example.com"
  
}

## Delete User

DELETE /api/users/:identifier

Delete a user by providing either the user's ID, name, or email as the :identifier parameter.
If the user is found and successfully deleted, the API will respond with a success message.

Example:

DELETE /api/johndoe


Response Body:

Status Code: 200 OK
{
  "Success": "User deleted "
}


Error Responses:

one common error is particularly faced in the PUT method. it is possible that the name or email provided is already by another user in the database. it would raise a an error known as Unique constraint error
If the provided :identifier does not correspond to an existing user (neither by ID nor by name), the API will respond with a 404 Not Found status and an error message indicating that the user does not exist.

Example Error Response:

{

  "Error": "User does not exist"
  
}







