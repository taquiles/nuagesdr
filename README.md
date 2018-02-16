
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


# Requisites and Configuration

  1. To run this showcase, and for better compliance with tests done, verify if the following versions are installed:
  
  * Python and pip: 6.3.1
  * node : 6.10.3
  * *virtualenv* installed

  2. In order to configure database access *settings.py* must updated
  
  	2.1. Configure the database name (*DATABASES.NAME*);
  	2.2. Update *user* and *password* with right permissions  (*DATABASES.USER* and *DATABASES.PASSWORD*);
  	2.3. On *postgresql* create a database whose name the same as in step 1:
  	
  		e.g.
  		CREATE DATABASE otherdb;
    
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
  
  3. Create Python Environment:
  	
  		cd <project_root> # that would be nuagesdr
  		cd nuagedr
  		virtualenv --python=python3.6 env
  		source env/bin/activate
  		
  
  4. Run the Migration that will create tables and load data:
  
    cd nuagesdr/nuagesdr
    python ./manage.py migrate
    python manage.py loaddata backend/fixtures/initial_data.json 

  
  5. Install backend python packages:
  
		cd <project_root> # that would be nuagesdr
		pip install -r requirements.txt
  
  6. Install frontend npm packages:
  
		cd <project_root> # that would be nuagesdr
		cd frontend
		npm install  


# Startup the Application

## Backend

	* Run the following to start the backend application:
	
	 cd <project_root> # that would be nuagesdr
	 cd nuagesdr
    python manage.py runserver
	

## Frontend

	* Run the following to start the frontend application:
		     
     cd <project_root> # that would be nuagesdr
     cd frontend
     npm run dev	

## Run Test on RESP Api endpoint:

	cd nuagesdr/frontend
	npm test

	




