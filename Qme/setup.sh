#!/bin/bash

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

pip install -r requirements.txt


python manage.py makemigrations
python manage.py migrate

pythin manage.py runserver