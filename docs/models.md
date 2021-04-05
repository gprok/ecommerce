# Basic Models

[Back](../README.md) 

1. Create the basis models for **Category** and **Product**
and their relationship.
1. Prepare the migrations for the new models: 
```python manage.py makemigrations```
1. Do the migrations: ```python manage.py migrate```
and notice that a number of tables for the user is also created.
1. Create an administrator ```python manage.py createsuperuser```
1. Register the models to Admin.py 