# CEN 5011 Project: Giving Hope

Add description.
***

# Table of Contents

* **[Get Started](#get-started)**

* **[Install packages](#install-package)**

* **[Create App](#create-app)**

* **[Useful Links](#useful-links)**

***

# Get Started

* Install python

* Install virtualenv
    *   ```
        pip install virtualenv
        ```
    *   ```
        pip3 install virtualenv
        ```

# Install Packages

* Install stripe
```
   pip install stripe
 ```
 
 * Install Bootstrap4/5
  ```
       pip install django-bootstrap4
  ```
  Add to INSTALLED_APPS in your settings.py file.
  ```
     INSTALLED_APPS = [
           .... ,
           "bootstrap4",
           ...,
       ]
   ```
 
 * Install datepicker
  ```
       pip install django-bootstrap-datepicker-plus
  ```
  Add bootstrap_datepicker_plus to the list of INSTALLED_APPS in your settings.py file.
  ```
     INSTALLED_APPS = [
           .... ,
           'bootstrap_datepicker_plus',
       ]
   ```
  


## MacOS/Linux

* Navigate to desired directory.

```
git clone https://github.com/caflore/giving-hope
cd giving-hope
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt 
python manage.py runserver
```

***

# Create App

It is sometimes best to create your own app to implement your feature.

```
mkdir ./giving_hope/apps/<APP_NAME>
python manage.py startapp <APP_NAME> ./giving_hope/apps/<APP_NAME>
```

Add your app to `settings.py` like below:

```python
INSTALLED_APPS = [
    ...,
    'giving_hope.apps.<APP_NAME>',
]
```

Make sure to edit `apps.py` inside the `/apps/<APP_NAME>` directory like below:

```python
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'giving_hope.apps.<APP_NAME>'
```

# Useful Links

* [Django Tutorial](https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
