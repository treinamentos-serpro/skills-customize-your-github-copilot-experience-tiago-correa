# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small REST API with FastAPI to manage a collection of books or tasks. This assignment focuses on API routes, request validation, JSON responses, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App

#### Description
Create a FastAPI application and define the basic structure for a RESTful API that serves data in JSON format.

#### Requirements
The completed program must:

- Import and initialize a FastAPI application.
- Define a root endpoint such as `/` that returns a welcome message.
- Configure the app with a reasonable title and description.
- Run the app locally using `uvicorn`.
- Confirm the app responds successfully in a browser or with an HTTP client.

### 🛠️ Build CRUD Endpoints

#### Description
Implement endpoints to create, read, update, and delete records in a simple in-memory database.

#### Requirements
The completed program must:

- Store data in an in-memory list or dictionary.
- Implement `GET /items` or `GET /books` to return all records.
- Implement `GET /items/{item_id}` or `GET /books/{book_id}` to return one record.
- Implement `POST /items` or `POST /books` to create a new record.
- Implement `PUT /items/{item_id}` or `PUT /books/{book_id}` to update an existing record.
- Implement `DELETE /items/{item_id}` or `DELETE /books/{book_id}` to remove a record.
- Return an appropriate `404` status code when a requested item is not found.
- Use Pydantic models to validate request payloads.
- Include a response model or clear JSON structure for each endpoint.

### 🛠️ Test and Validate the API

#### Description
Verify that the API behaves correctly by sending requests and checking the returned JSON and status codes.

#### Requirements
The completed program must:

- Test creating a new record through the API.
- Test retrieving all records and a single record.
- Test updating an existing record.
- Test deleting a record.
- Verify that invalid or missing IDs return an error response.
- Provide sample request examples in the final explanation or in comments.
