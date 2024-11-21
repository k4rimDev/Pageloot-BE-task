# Pageloot API

## Requirements
- Python 3.9+
- Django 4.x
- Django REST Framework
- drf-yasg
- django-jazzmin (For admin panel)

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
    ```bash
    python manage.py migrate
    ```
4. Start the server:
    ```bash
    python manage.py runserver
    ```

## Endpoints

* `/api/users/` - CRUD for Users.
* `/api/expenses/` - CRUD for Expenses.
* `/api/expenses/list_by_date_range/` - Get expenses by date range.
* `/api/expenses/category_summary/` - Get total expenses per category for a month.
* `/swagger/` - API documentation.

---

### Key Features
1. **Advanced Querying**: Date range filtering and category summaries.
2. **Validation**: Ensures expenses are positive.
3. **Swagger Docs**: Easy-to-read API documentation.
4. **Scalability**: Modular and clean structure for future extensions.
