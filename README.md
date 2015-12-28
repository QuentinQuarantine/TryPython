# Try Python [![Build Status](https://travis-ci.org/IuryAlves/TryPython.svg?branch=master)](https://travis-ci.org/IuryAlves/TryPython)

## Try python is a project inspired by [try-haskell](tryhaskell.org)


![try-python](try-python.gif)
##### The goal of this project is to introduce python for new people by let they use a python REPL( Read, Eval, Print, Loop) in the browser.

## Getting Started

* Install python 2.x on your system
*  Install git
* Clone this repository
 
        git clone git@github.com:IuryAlves/TryPython.git
        cd TryPython

* Install python virtualenv: 
 
        sudo pip install virtualenv

* Create a virtualenv:
 
        virtualenv venv
        source venv/bin/activate

* Install project dependencies:

        pip install -r requirements.txt

* Cd again ;)

        cd TryPython

* Sync the database

        ./manage.py syncdb

* Make the migrations

        ./manage.py makemigrations

* Run the migrations:
        
        ./manage.py migrate

* Load the fixtures of the project

        ./manage.py loaddata steps.json

* Run
        
        export DJANGO_SECRET_KEY=<your-secret-key> 
        ./manage.py runserver 8000


Now, just access localhost:8000 =D

## Contributing

* See the contributing [guide](CONTRIBUTING.md)
    
* This project uses TravisCI [TryPython on Travis](https://travis-ci.org/IuryAlves/TryPython)
* This project uses [jquery.console](https://github.com/chrisdone/jquery-console)
