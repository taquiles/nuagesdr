
This showcase implements a platform (or a feature subset) which allow to retrieve, from the backend, a Form so Insurence Careers may customize data to be collect per insurence.

# Use Case

The Use case is depicted bellow.

![Use Case](https://github.com/taquiles/nuagesdr/blob/master/docs/Use_Case-Nuages.png)

# Architecture

The pre requisits included Python and Vue (ES6 flavor).

DjangoRestframework, a Django framework, was used for Rest Library and for the MVT pattern (Model-View-Template). Other option, with similar features, would be Flask.

![System-Components](https://github.com/taquiles/nuagesdr/blob/master/docs/Stack-System-Components.png)

# Database

The ER Diagram below includes two more tables to contextualize properly tables that were implemented

![ERD](https://github.com/taquiles/nuagesdr/blob/master/docs/ERD-NuagesDR.png)


# Startup the Application

## Database 
  
  * To start the application *settings.py* must updated :
  1. Configure the database name (DATABASES.NAME) in the settings.py file) ;
  2. Update *user* and *password* with right permissions;
  3. On *postgresql* create a database whose name the same as in step 1.
  
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
  
  2. Run the Migration that will create tables and load data:
  
    cd nuagesdr/nuagesdr
    python ./manage.py migrate
    python manage.py loaddata backend/fixtures/initial_data.json 

## Backend

	* Run the following to start the backend application:
	
    cd nuagesdr/frontend
    npm run dev

## Frontend

	* Run the following to start the frontend application:
		 
    cd nuagesdr/nuagesdr
    python manage.py runserver

## Run Test on RESP Api endpoint:

	cd nuagesdr/frontend
	npm test

	




