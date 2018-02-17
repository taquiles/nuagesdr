
This showcase implements a platform (or a feature subset) which allow to retrieve, from the backend, a Form so Insurance Careers may customize data to be collected per insurance.


# Use Case

The Use case is depicted below.

![Use Case](https://github.com/taquiles/nuagesdr/blob/master/docs/Use_Case-Nuages.png)


# Architecture

The prerequisites included Python and Vue (ES6 flavor).

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

2. Edit *settings.py* to configure database access
  
	2.1. Configure the database name (*DATABASES.NAME*);
	
	2.2. Update *user* and *password* with right permissions  (*DATABASES.USER* and *DATABASES.PASSWORD*);
	
	2.3. On *postgresql* create a database whose name is the same as in step 1:
  	
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
  
3. After database access configuration, you may choose to run
  
		chmod -x install_all.sh
		./install.sh
  		
which will perfom all the remaining steps.
  
4. Create Python Environment:

		cd <project_root> # that would be nuagesdr
		cd nuagedr
		virtualenv --python=python3.6 env
		source env/bin/activate
  		  
5. Install backend python packages:
 
		cd <project_root> # that would be nuagesdr
		pip install -r requirements.txt
	
6. Run the Migration that will create tables and load data:
 
		cd nuagesdr/nuagesdr
		python ./manage.py migrate
		python manage.py loaddata backend/fixtures/initial_data.json 
  
7. Install frontend npm packages:
  
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

* The above performs the following tests:

1. Site is up
2. REST endpoint is up and returns a JSON file
3. Retrieves a single record from REST API
4. Retrieves all records from REST API.
	




