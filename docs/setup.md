# Setup Project

[Back](../README.md) 

1. Create a new Django project. You can do that from 
within PyCharm (File -> New Project) or from the terminal typing 
   ```django-admin startproject ecommerce```.
1. Create a new application from the terminal typing 
```python manage.py startapp store```
1. Register the new app in settings.py in INSTALLED_APPS
1. In the store folder add a file ```urls.py```
1. Add the new urls.py file the the ecommerce/urls.py 
by adding ```path('store/', include('store.urls'))```
1. Then add some basic routes and respective views methods, 
like category and product just to see that urls work properly.
   
Branch: startup-project