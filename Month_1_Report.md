# Month 1 Internship Progress Report
**Backend Development Internship | Weeks 1–4**

| Field | Details |
|---|---|
| Intern | Prajeena G.C. |
| Organization | Codavatar |
| Track | Backend Development |
| Reporting period | Month 1 (Weeks 1–4) |
| Report prepared | 18 November 2026 |
| GitHub | [Repository](https://github.com/prajeenagc/Internship) |

## 1. Executive Summary

During the first month of my Backend Development internship at Codavatar, I progressed from Python fundamentals and basic project setup to developing REST APIs, integrating PostgreSQL databases, and learning authentication concepts. The first two weeks focused on Python, Django, and FastAPI fundamentals, including request validation, CRUD operations, service-layer separation, error handling, middleware, background tasks, and automated API testing.

In the third week, I worked with SQL and SQLAlchemy to connect backend applications to PostgreSQL databases. I also practised database relationships, constraints, repository functions, and schema migrations using Alembic. During the fourth week, I began working on authentication, including user registration, password hashing and verification, and the foundations of JWT-based authentication.

Alongside the weekly exercises, I continued developing a practical backend project using FastAPI, PostgreSQL, SQLAlchemy, and Alembic. This work helped me apply the concepts from the weekly exercises in a more structured application.

## 2. Weekly Progress Summary

| Week | Focus | Work Completed |
|---|---|---|
| Week 1 | Python and project foundation | Practised Python fundamentals, input validation, reusable functions, exceptions, type hints, environment configuration, and Git. Also developed a basic Django Todo CRUD application. |
| Week 2 | FastAPI and REST API development | Built FastAPI endpoints and CRUD operations, created Pydantic schemas, separated service logic, implemented middleware and exception handling, used background tasks, and wrote API tests with pytest and TestClient. |
| Week 3 | PostgreSQL, SQLAlchemy, and Alembic | Integrated PostgreSQL with backend applications, created ORM models and relationships, practised SQL queries, implemented database operations, and configured Alembic migrations. |
| Week 4 | Authentication and backend security | Worked on user registration, password hashing and verification, login-related service logic, and the foundations of JWT authentication and bearer-token-based user identification. |

## 3. Weekly Progress Details

### Week 1 — Python and Project Foundation

The first week focused on strengthening Python fundamentals and establishing good development practices.

**Key activities:**
- Set up the development environment, project repository, virtual environment, and `.gitignore`.
- Practised Python input validation, including handling empty strings, whitespace, boundary values, and invalid inputs.
- Created reusable functions and service modules, with meaningful exceptions and clear inputs and outputs.
- Used type hints and environment variables, including safe defaults and an `.env.example` file.
- Practised Git workflows involving branches, diffs, and merge conflicts.
- Recreated the project environment using setup instructions to check reproducibility.
- Developed an additional Django Todo CRUD application.

**Django concepts practised:**
- Models, views, URL routing, forms, and templates.
- Django ORM and database migrations.
- Creating, viewing, updating, and deleting Todo records.

**Learning outcomes:** Improved understanding of Python fundamentals, validation, modular code, exception handling, environment configuration, Git, and the basic structure of a Django application.

### Week 2 — FastAPI and Backend Development

The second week focused on building REST APIs with FastAPI and understanding how backend applications handle requests and responses.

**Key activities:**
- Created FastAPI applications and basic GET endpoints, including health-check and task-retrieval routes.
- Used Swagger UI to inspect and test API endpoints.
- Created Pydantic request and response schemas using `BaseModel` and `Field`.
- Implemented POST and GET endpoints and developed a basic CRUD API.
- Separated route handling from business logic using service modules.
- Used `HTTPException` and appropriate HTTP status codes for error handling.
- Implemented middleware to generate request IDs, measure request duration, and log request details.
- Created a custom application exception and a centralized exception handler.
- Used FastAPI `BackgroundTasks` for audit logging.
- Wrote automated API tests using pytest and FastAPI `TestClient`.

**Testing coverage included:**
- Creating and retrieving tasks.
- Updating and deleting tasks.
- Handling requests for missing resources.
- Validating invalid input and checking response status codes and bodies.

**Learning outcomes:** Gained practical experience with FastAPI routing, Pydantic validation, REST API design, service-layer separation, middleware, exception handling, background tasks, and automated testing.

**Limitations identified:** The basic task API used in-memory storage, so data was not persistent. Authentication, authorization, and database integration were not part of that initial exercise.

### Week 3 — Database Integration and SQLAlchemy

The third week focused on connecting backend applications to PostgreSQL and managing database operations through SQLAlchemy.

**Key activities:**
- Configured SQLAlchemy using `create_engine()`, declarative models, `sessionmaker()`, and a database dependency with `get_db()`.
- Created ORM models for users, projects, project members, and tasks.
- Practised primary keys, foreign keys, unique constraints, check constraints, and relationships.
- Explored referential actions such as `CASCADE`, `RESTRICT`, and `SET NULL`.
- Implemented database-backed create and retrieve operations.
- Practised the repository pattern and separated database operations into reusable functions.
- Used database session operations such as `add()`, `commit()`, `refresh()`, and `rollback()`.
- Configured application settings and database connection details through environment variables.
- Set up Alembic and practised creating, applying, and reverting schema migrations.
- Wrote SQL queries using `SELECT`, `WHERE`, `ORDER BY`, `INNER JOIN`, `LEFT JOIN`, and common table expressions.
- Used `EXPLAIN ANALYZE` to inspect query execution and explored indexing.
- Practised transactions, foreign-key constraints, `UPDATE ... RETURNING`, and task status history.

**Database-backed API work included:**
- CRUD operations for users, projects, and tasks.
- PATCH updates using `model_dump(exclude_unset=True)`.
- Validation of referenced records.
- Handling database integrity errors with rollback and appropriate HTTP responses.
- A database health check using `SELECT 1`.
- Initial Alembic migrations, indexes, constraints, and a database seeding script.

**Learning outcomes:** Developed a better understanding of relational database design, SQL querying, SQLAlchemy ORM, database sessions, repository functions, transaction handling, and schema versioning with Alembic.

**Limitations identified:** Repository-based organization was practised but was not applied consistently across every exercise. Authentication and authorization were not yet implemented in the database exercises, and automated API testing still needed to be expanded.

### Week 4 — Authentication and Backend Security

The fourth week introduced authentication and the security considerations involved in handling user accounts.

**Key activities and concepts:**
- Worked on user registration with database integration.
- Implemented password hashing so that plain-text passwords are not stored in the database.
- Practised password verification during authentication.
- Worked on the login flow and the service logic required to authenticate a user.
- Configured JWT-related application settings, including the secret key, signing algorithm, and token expiration.
- Studied bearer-token authentication and the role of OAuth2 dependencies in FastAPI.
- Began working through the process of extracting a token, validating it, and identifying the current user.

**Learning outcomes:** Built an initial understanding of authentication workflows, secure password storage, password verification, JWT configuration, and how protected API endpoints identify authenticated users.

**Current status:** Authentication work was still in progress at the end of the reporting period. The registration and password-hashing components had been worked on, while the login, token-validation, and current-user flow were being developed and tested.

## 4. Practical Backend Project

### Task Management Backend

Alongside the weekly exercises, I worked on a practical backend application using FastAPI and PostgreSQL. The project is intended to provide a foundation for a broader employee workspace where users can manage tasks and, as the application develops, support additional workflow features.

| Area | Current scope and progress |
|---|---|
| Backend framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Database migrations | Alembic |
| Task management | Implemented core task creation, retrieval, updating, and deletion operations. |
| Request and response validation | Used Pydantic schemas for create, update, and response data. |
| Authentication | User model, registration schema, password hashing, and password verification work started; the complete authentication flow remains in progress. |
| Future project direction | The broader application may include role-based access and task assignment. These are planned extensions, not completed features. |

**Development approach:**
- Organized the application into separate modules for models, schemas, routes, services, and database configuration.
- Used Pydantic schemas to validate incoming data and shape API responses.
- Kept database operations separate from route handlers.
- Used SQLAlchemy for database interaction and Alembic for schema migrations.
- Tested API behaviour through the interactive API documentation while developing endpoints.

The project provided an opportunity to apply the concepts covered during the internship in a single application. It also helped identify areas that require further work, particularly completing authentication, adding authorization, and expanding automated tests.

## 5. Tools and Technical Skills

| Category | Tools / Technologies | Application |
|---|---|---|
| Programming language | Python | Backend logic, validation, reusable functions, and services |
| Web frameworks | Django, FastAPI | Django CRUD application and REST API development |
| API validation | Pydantic | Request validation and response schemas |
| API testing | Swagger UI | Manual endpoint checks and automated API tests |
| Database | PostgreSQL | Relational data storage and querying |
| ORM | SQLAlchemy | Models, relationships and database operations |
| Migrations | Alembic | Database schema version control |
| Query language | SQL | Filtering, joins, transactions, CTEs, and query analysis |
| Authentication | Password hashing, JWT, OAuth2 bearer-token concepts | User authentication learning and implementation |
| Version control | Git, GitHub | Repository management, branches, commits, and collaboration workflows |
| Configuration | Environment variables, `.env`, `.env.example` | Application configuration and secret handling |

## 6. Challenges and Resolutions

| Challenge | Approach / Resolution |
|---|---|
| Handling invalid and unexpected input | Added explicit validation rules, considered boundary cases, and used meaningful exceptions. |
| Keeping API routes organized | Separated business logic into service modules instead of placing all operations in route handlers. |
| Returning consistent API errors | Practised HTTP exceptions, status codes, custom exceptions, and centralized exception handling. |
| Managing database sessions and failures | Used SQLAlchemy session methods and rollback handling when database operations failed. |
| Understanding relationships and constraints | Practised primary keys, foreign keys, relationship rules, and referential actions in PostgreSQL and SQLAlchemy. |
| Managing database schema changes | Used Alembic revisions and practised both upgrade and downgrade operations. |
| Understanding authentication flow | Worked through password hashing and verification before progressing to login, JWT validation, and current-user dependencies. |

## 7. Evidence and Deliverables

The following work represents the main practical outputs from the first month:

- **Week 1:** Python validation and reusable-function exercises, environment and Git practice, and a Django Todo CRUD application.
- **Week 2:** FastAPI endpoints, Pydantic schemas, CRUD API, middleware, exception handling, background-task example, and pytest API tests.
- **Week 3:** PostgreSQL and SQLAlchemy models, database-backed API operations, SQL query exercises, and Alembic migration work.
- **Week 4:** User registration and password-hashing work, plus initial implementation and study of the JWT-based authentication flow.
- **Practical project:** FastAPI task-management backend with PostgreSQL integration, SQLAlchemy models, CRUD operations, and Alembic configuration.

Repository: [Internship GitHub Repository](https://github.com/prajeenagc/Internship)

## 8. Reflection

The first month helped me build a stronger understanding of how backend applications are structured and how their components work together. I progressed from writing individual Python functions to building APIs, validating requests, handling errors, writing tests, and integrating a relational database. Working with SQLAlchemy and Alembic also helped me understand the importance of database relationships, transaction handling, and controlled schema changes.

One important area of progress was learning to separate route handling, business logic, and database operations rather than writing everything in a single file. I also became more aware of the importance of testing edge cases and handling failures instead of focusing only on successful requests.

Authentication is an area I am still developing. I have started implementing registration and password security and am continuing to work through the login and token-validation flow. Overall, the first month provided a practical foundation in Python backend development and prepared me to build more complete and maintainable applications.

## 9. Conclusion

During the first month of the internship, I gained practical experience with Python, Django, FastAPI, REST API development, PostgreSQL, SQLAlchemy, Alembic, and the fundamentals of authentication. I completed exercises covering the core stages of backend development, from project setup and request validation to database integration and API testing. I also applied these concepts to a practical task-management backend project. The work completed during this period has established a foundation for continuing development and improving the reliability, security, and structure of backend applications.

---

**Prepared by:** Prajeena G.C.  
**Organization:** Codavatar  
**Supervisor review:** ______________________________
