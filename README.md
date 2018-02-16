
This showcase implements a platform (or a feature subset) which allow to retrieve, from the backend, a Form so Insurence Careers may customize data to be collect per insurence.

# Use Case
![Alt text](https://github.com/taquiles/nuagesdr/blob/master/docs/Use%20Case%20-%20RiverMoon%20-%20Page%201%20(3).png/?raw=trque "Optional Title")
# Architecture
# Database

The Archicture is as follows:


# Startup the Application
## Database
  - Python Database Configuration in settings.py:
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'nuages',
              'USER': 'postgres',
              'PASSWORD': 'a',
              'HOST': 'localhost',
              'PORT': '5432',
          }
    }
  - Note: Database 'nuagaes', as in settings-py, must be created before the folowwing commands:
  
    cd nuagesdr/nuagesdr
    python ./manage.py migrate
    python manage.py loaddata backend/fixtures/initial_data.json 

## Frontend
    cd nuagesdr/nuagesdr
    python manage.py runserver

## Backend
    cd nuagesdr/frontend
    npm run dev




