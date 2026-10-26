# Week 1 - Python and Project Foundation

## Overview

This repository contains my Week 1 backend development internship exercises. The focus is on Python fundamentals, input validation, reusable functions, environment configuration, Git, and building a reproducible project setup.

The week also includes a Django todo CRUD application as practical work with models, views, URLs, templates, and database operations.

## Learning Objectives

- Set up a Python development environment and Git repository.
- Validate input using explicit rules and boundary checks.
- Write reusable functions and import them from separate modules.
- Understand exceptions, return values, and type hints.
- Read configuration from environment variables.
- Practise Git branches, diffs, and conflict resolution.
- Document setup instructions, test results, and remaining gaps.


## Day 1 - Environment and Repository

**Objective:** Understand the development environment and create a reproducible project setup.

### Activities

- Check the installed Python and Git versions.
- Identify the project root and organize the project files.
- Create a virtual environment.
- Add an appropriate `.gitignore`.
- Document the setup and dependency installation commands.

### Expected outcome

A repository with clear setup instructions that another developer can follow from a fresh terminal.

## Day 2 - Python Values and Validation

**Objective:** Learn to validate values before accepting them into an application.

### Activities

- Write title and priority validators.
- Define explicit validation rules.
- Test empty strings and whitespace.
- Test valid boundary values and invalid priorities.
- Use assertions to verify expected behavior.
- Document the rules in a validation table.

### Expected outcome

A validation module with clear rules and sample outputs demonstrating both accepted and rejected inputs.

## Day 3 - Functions and Modules

**Objective:** Separate business logic from user interaction and make functions reusable.

### Activities

- Move validation logic into an importable service module.
- Write task-creation logic that returns a new record without modifying the original input.
- Raise meaningful exceptions for invalid input.
- Create a small command-line program that calls the service.
- Test independent function calls and module imports.

### Expected outcome

A reusable service module and a command-line caller that demonstrate inputs, outputs, and error handling.

## Day 4 - Types, Configuration, and Git

**Objective:** Practise type hints, environment settings, secrets management, and reviewable Git changes.

### Activities

- Add type hints to the task service.
- Introduce and inspect a deliberate type mismatch.
- Read configuration from environment variables with safe defaults.
- Use `.env.example` to document expected settings without real credentials.
- Ensure `.env` is excluded from Git.
- Create a branch, review its diff, and resolve a disposable merge conflict.

### Expected outcome

A typed service, configuration example, and evidence of Git branch and diff practice.

## Day 5 - Foundation Review

**Objective:** Demonstrate the week's foundational skills independently.

### Activities

- Recreate the environment by following the README in a new folder.
- Implement one new validation rule without copying a solution.
- Explain function inputs and outputs.
- Explain which exceptions can be raised and where they are handled.
- Review the Git history.
- Document the remaining gaps.

### Expected outcome

A runnable program, a corrected README, demonstrated boundary behavior, and a list of known limitations.

## Additional Practice - Django Todo CRUD Application

This project provides additional practice with Django's Model–View–Template workflow.

### Features

- Create tasks.
- View tasks.
- Update existing tasks.
- Delete tasks.
- Store task data in a database.

### Django concepts practised

- Models and database migrations.
- Views and URL routing.
- Forms and input handling.
- Templates for displaying and editing tasks.
- Django ORM operations for CRUD functionality.





## Week 1 Learning Outcomes

- Setting up and running a Python project
- Writing and testing input validation rules
- Creating reusable functions and modules
- Understanding exceptions and function behavior
- Using type hints and environment configuration
- Managing and reviewing changes with Git
- Documenting project setup, usage, and known limitations


