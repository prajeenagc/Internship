# Week 2 - FastAPI and Backend Development

## Overview

This repository contains my Week 2 backend development internship exercises. The focus is on understanding FastAPI fundamentals, building REST APIs, request and response validation, separating business logic into service modules, error handling, middleware, background tasks, and automated API testing.

The week progresses from creating basic FastAPI endpoints to building a small CRUD API with reusable services and automated tests.

## Learning Objectives

- Understand FastAPI application setup and endpoint creation.
- Create REST API endpoints using different HTTP methods.
- Validate request data using Pydantic schemas.
- Define response models and appropriate HTTP status codes.
- Separate API routes from business logic using service modules.
- Handle missing resources and application errors.
- Understand middleware and request processing.
- Use background tasks for operations outside the main request-response cycle.
- Write automated API tests using pytest and FastAPI TestClient.

## Day 6 - FastAPI Introduction and Basic Endpoints

**Objective:** Understand FastAPI application structure and create basic API endpoints.

### Activities

- Create a FastAPI application.
- Understand the role of `FastAPI()`.
- Create GET endpoints.
- Implement a health-check endpoint.
- Return task data through an API endpoint.
- Run the application and test endpoints using the interactive API documentation.

### Expected outcome

A basic FastAPI application with working health-check and task retrieval endpoints.

## Day 7 - Request Validation and Response Models

**Objective:** Understand how to validate incoming request data and structure API responses.

### Activities

- Create Pydantic schemas using `BaseModel`.
- Use `Field()` to define validation rules.
- Implement a task creation schema.
- Implement a task response schema.
- Create POST and GET endpoints.
- Use `response_model` to define expected API responses.
- Set appropriate HTTP status codes for successful requests.
- Store created tasks temporarily in memory.

### Expected outcome

A basic task API that supports task creation and retrieval with validated request data and structured responses.

## Day 8 - CRUD Operations and Service Layer

**Objective:** Implement complete CRUD functionality and separate business logic from API endpoints.

### Activities

- Create a separate service module for task operations.
- Move task creation logic into the service layer.
- Implement task retrieval by ID.
- Implement retrieval of all tasks.
- Implement task updates.
- Implement task deletion.
- Use `TaskCreate`, `TaskResponse`, and `TaskUpdate` schemas.
- Handle nonexistent tasks using `HTTPException`.
- Return appropriate HTTP status codes for successful and unsuccessful operations.

### Expected outcome

A CRUD API supporting task creation, retrieval, updating, and deletion, with business logic separated into reusable service functions.

## Day 9 - Middleware, Error Handling, and Background Tasks

**Objective:** Understand request processing, centralized error handling, and background task execution.

### Activities

- Implement custom HTTP middleware.
- Generate unique request IDs using UUID.
- Measure request processing time.
- Add request IDs to response headers.
- Log request methods, paths, status codes, and execution duration.
- Create a custom application exception.
- Implement a centralized exception handler.
- Use `JSONResponse` to return structured error responses.
- Implement background tasks using FastAPI `BackgroundTasks`.
- Add an audit logging function to record endpoint activity.

### Expected outcome

A FastAPI application with request tracking, execution-time logging, centralized application error handling, and background audit logging.

## Day 10 - REST API Testing

**Objective:** Test REST API functionality and verify expected application behavior using automated tests.

### Activities

- Set up pytest and FastAPI `TestClient`.
- Write automated tests for task creation.
- Test retrieval of existing tasks.
- Test task updates.
- Test task deletion.
- Test requests for nonexistent tasks.
- Test input validation using invalid task data.
- Verify response status codes and response bodies.
- Run the test suite and review test results.

### Expected outcome

An automated test suite covering the main CRUD operations, error responses, and request validation.

## Week 2 Learning Outcomes

- Setting up and running a FastAPI application.
- Creating REST API endpoints using HTTP methods.
- Understanding request validation with Pydantic.
- Defining request schemas and response models.
- Working with HTTP status codes.
- Implementing CRUD operations.
- Separating business logic into service modules.
- Handling application errors and missing resources.
- Understanding middleware and request lifecycle.
- Implementing request IDs and execution-time logging.
- Using background tasks for audit logging.
- Writing and running automated API tests using pytest and TestClient.

## Known Limitations

- Task data is stored in an in-memory Python list rather than a persistent database.
- Data is lost when the application restarts.
- Authentication and authorization are not implemented.
- The API does not yet use a production database or database migrations.