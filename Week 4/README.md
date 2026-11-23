# Week 4 - Authentication, Authorization, and Backend Security

## Overview

This repository contains my Week 4 backend development internship exercises. The main focus of this week was understanding how authentication and authorization work in backend applications and learning how to protect API endpoints and user data.

The exercises cover user registration, password hashing, database integration, JWT-based authentication, protected routes, task ownership, and role-based access control. The week also includes automated testing to check authentication functionality and ensure that users can only access resources they are authorized to use.

## Learning Objectives

- Understand the difference between authentication and authorization.
- Implement user registration and login functionality.
- Learn how to hash passwords and verify user credentials.
- Integrate FastAPI with PostgreSQL using SQLAlchemy.
- Create and manage user records in a database.
- Generate and validate JWT access tokens.
- Protect API endpoints using authentication dependencies.
- Retrieve information about the currently authenticated user.
- Implement resource ownership and restrict access to user-specific data.
- Understand and implement role-based access control.
- Write automated tests for authentication and authorization.
- Verify that users cannot access or modify resources belonging to others.

## Day 16 - Introduction to Authentication

**Objective:** Understand the basic authentication process and implement user registration, login, and protected endpoints.

### Activities

- Create a basic FastAPI authentication application.
- Define Pydantic schemas for user registration and login.
- Implement user registration using temporary in-memory storage.
- Validate user input using Pydantic.
- Hash passwords before storing them.
- Verify passwords during login.
- Generate JWT access tokens after successful authentication.
- Implement token verification.
- Use `OAuth2PasswordBearer` to extract access tokens from requests.
- Create a dependency to identify the currently authenticated user.
- Implement a protected endpoint to retrieve the current user's information.
- Write basic tests for registration, login, and token validation.

### Expected outcome

A basic authentication API that supports user registration, login, password hashing, JWT token generation, and protected user profile access.

## Day 17 - Database Integration and User Registration

**Objective:** Replace temporary user storage with a database and implement persistent user registration using SQLAlchemy.

### Activities

- Configure application settings using Pydantic Settings.
- Connect the FastAPI application to a PostgreSQL database.
- Set up the SQLAlchemy database engine and session factory.
- Create a database dependency using `get_db`.
- Define a SQLAlchemy User model.
- Create Pydantic schemas for user registration and responses.
- Implement password hashing using `pwdlib`.
- Separate user registration logic into a service module.
- Check whether a username or email address is already registered.
- Store new user records in the database.
- Handle duplicate registration attempts.
- Return user information without exposing password hashes.
- Test the registration endpoint and database operations.

### Expected outcome

A database-backed user registration API that stores user information persistently, validates registration data, hashes passwords, and handles duplicate accounts appropriately.

## Day 18 - JWT Authentication and Protected Routes

**Objective:** Implement database-backed authentication and use JWT access tokens to protect API endpoints.

### Activities

- Configure authentication settings using environment variables.
- Define the JWT secret key, algorithm, and access token expiration time.
- Implement password hashing and password verification.
- Create functions to generate and verify JWT access tokens.
- Implement user registration and login endpoints.
- Authenticate users using their email addresses and passwords.
- Generate an access token after successful login.
- Use `OAuth2PasswordBearer` to retrieve tokens from incoming requests.
- Create a `get_current_user` dependency.
- Validate access tokens and retrieve the corresponding user from the database.
- Handle invalid and expired tokens.
- Prevent inactive users from accessing protected endpoints.
- Implement a protected endpoint to retrieve the current user's profile.
- Write tests for registration, login, and protected route access.

### Expected outcome

An authentication API with database-backed user accounts, password verification, JWT access tokens, and protected endpoints that require valid authentication.

## Day 19 - Resource Ownership and Role-Based Access Control

**Objective:** Understand how resource ownership and user roles can be used to control access to API resources and administrative operations.

### Activities

- Create SQLAlchemy models for users and tasks.
- Define the relationship between users and their tasks.
- Use foreign keys to associate tasks with their owners.
- Add a role field to the User model.
- Implement a dependency to identify the current user.
- Create a `require_admin` dependency to restrict administrative access.
- Implement task creation for the current user.
- Retrieve individual tasks belonging to the current user.
- Implement task update and deletion operations.
- Prevent users from accessing or modifying tasks belonging to other users.
- Create an administrator-only endpoint for deleting users.
- Handle unauthorized access using appropriate HTTP status codes.
- Write tests to verify task ownership and administrative permissions.

### Expected outcome

A task API that supports user-specific resource access and role-based authorization, ensuring that users can manage their own tasks while administrative operations remain restricted to administrators.

## Day 20 - Authentication, Authorization, and Security Testing

**Objective:** Bring the authentication and authorization concepts together and verify that the API behaves correctly under different access conditions.

### Activities

- Review the user registration and login process.
- Review password hashing and verification.
- Verify JWT access token generation and validation.
- Organize authentication and authorization logic into reusable modules.
- Implement database-backed user and item management.
- Protect user profile and item endpoints using authentication dependencies.
- Associate newly created items with the currently authenticated user.
- Implement retrieval of items belonging to the current user.
- Restrict individual item retrieval, updates, and deletion based on ownership.
- Prevent inactive users from accessing protected endpoints.
- Configure a separate SQLite database for automated testing.
- Use pytest and FastAPI `TestClient` to test API functionality.
- Write tests for successful registration and login.
- Test duplicate registration and incorrect login credentials.
- Verify that protected endpoints reject requests without valid tokens.
- Test access to authenticated user profiles.
- Create tests involving multiple users to verify resource ownership.
- Confirm that users cannot retrieve, update, or delete items belonging to other users.

### Expected outcome

An authentication and authorization API with protected user and item endpoints, database-backed resource ownership, and automated tests covering login, token validation, and unauthorized resource access.

## Week 4 Learning Outcomes

By completing the exercises, I gained practical experience with:

- Understanding authentication and authorization in backend applications.
- Implementing user registration and login.
- Hashing passwords and verifying user credentials.
- Integrating FastAPI with PostgreSQL using SQLAlchemy.
- Creating database models and managing database sessions.
- Separating authentication and business logic into reusable modules.
- Generating and validating JWT access tokens.
- Using authentication dependencies to protect API endpoints.
- Retrieving the currently authenticated user.
- Handling invalid tokens and inactive user accounts.
- Implementing database relationships between users and their resources.
- Using foreign keys to establish resource ownership.
- Restricting access to user-specific resources.
- Implementing role-based access control for administrative operations.
- Writing automated tests using pytest and FastAPI TestClient.
- Testing authentication, authorization, and resource ownership.

## Known Limitations

- The exercises focus on backend functionality and do not include a complete frontend application.
- Refresh token functionality is not implemented.
- Server-side token revocation and logout functionality are not implemented.
- The Day 19 exercise uses a user ID supplied through a request header to demonstrate user identification and role-based access checks. This is a learning implementation rather than a production authentication mechanism.
- The exercises demonstrate selected authentication and authorization scenarios rather than a complete production security implementation.