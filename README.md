# Pageloot API

## Overview

This is a Django-based REST API for managing Users and Expenses. It includes CRUD operations, custom filtering by date range, and expense category summaries, all built with Django REST Framework.

## Features

* User management
* Expense CRUD operations
* Date range filtering for expenses
* Category-wise expense summaries for a given month
* Input validation (e.g., positive expense amounts)
* API documentation using Swagger (drf-yasg)

## Requirements
- Python 3.9+
- Django 5.x
- Django REST Framework
- drf-yasg
- django-jazzmin (For admin panel)

## Setup
1. Clone the repository.
    ```bash
    git clone https://github.com/k4rimDev/Pageloot-BE-task
    cd pageloot_backend
    ```
2. Install Dependencies
Use Poetry to install all required packages:
   ```bash
    poetry install
   ```
3. Run migrations:
    ```bash
    poetry run python manage.py migrate
    ```
4. Start the server:
    ```bash
    poetry run python manage.py runserver
    ```

## Endpoints

* `/api/users/` - CRUD for Users.
* `/api/expenses/` - CRUD for Expenses.
* `/api/expenses/list_by_date_range/` - Get expenses by date range.
* `/api/expenses/category_summary/` - Get total expenses per category for a month.
* `/swagger/` - API documentation.


## Validation Rules

* Expense amounts must be positive.
* Required query parameters for custom endpoints:
    * list_by_date_range: user, start_date, and end_date
    * category_summary: user and month


## API Documentation

Swagger documentation is available at:

```/swagger/```

---

### Key Features
1. **Advanced Querying**: Date range filtering and category summaries.
2. **Validation**: Ensures expenses are positive.
3. **Swagger Docs**: Easy-to-read API documentation.
4. **Scalability**: Modular and clean structure for future extensions.
