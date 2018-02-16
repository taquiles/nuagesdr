#!/bin/bash

PROJECT_ROOT_PWD=`pwd`
echo ----------------------------------------------
echo ----------------------------------------------
echo PROJECT_ROOT_PWD-$PROJECT_ROOT_PWD
echo

echo ----------------------------------------------
echo ----------------------------------------------
echo Create Python Environment
echo
cd $PROJECT_ROOT_PWD/nuagesdr/
virtualenv --python=python3.6 env
source env/bin/activate

echo ----------------------------------------------
echo ----------------------------------------------
echo 
echo Run the Migration that will create tables and load data:
cd $PROJECT_ROOT_PWD/nuagesdr
python ./manage.py migrate
python manage.py loaddata backend/fixtures/initial_data.json 

echo ----------------------------------------------
echo ----------------------------------------------
echo 
echo Install backend python packages:
cd $PROJECT_ROOT_PWD/nuagesdr
pip install -r requirements.txt
  

echo ----------------------------------------------
echo ----------------------------------------------
echo
echo Install frontend npm packages
cd $PROJECT_ROOT_PWD/frontend
npm install  

