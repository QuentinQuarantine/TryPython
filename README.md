# Try Python [![Build Status](https://travis-ci.org/IuryAlves/TryPython.svg?branch=master)](https://travis-ci.org/IuryAlves/TryPython) [![Coverage Status](https://coveralls.io/repos/IuryAlves/TryPython/badge.svg?branch=master&service=github)](https://coveralls.io/github/IuryAlves/TryPython?branch=master)  [![For the badge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com/images/badges/built-with-love.svg)


![try-python](try-python.gif)
##### The goal of this project is to teach python to new people. This project is a python version from [try-haskell](tryhaskell.org)

# Table of contents
1. [Installing](#installing)
2. [running](#running)
3. [Contributing](#contributing)

## Installing <a name="installing"></a>

* Install python 2.x on your system
*  Install git
* Clone this repository

```sh
 git clone git@github.com:IuryAlves/TryPython.git
 cd TryPython
 ```

* Install python virtualenv:

``` sh
sudo pip install virtualenv
```

* Create a virtualenv:

```sh
virtualenv venv
source venv/bin/activate
```

* Install project dependencies:

```sh
pip install -r requirements/requirements.txt
```

* Generate a DJANGO_SECRET_KEY [here](http://www.miniwebtool.com/django-secret-key-generator/)

* Create a `.env` file in the home of the project and insert this lines

      DEBUG=True

      DJANGO_SECRET_KEY=the-secret-key-that-you-gerenate

    **Then save and close the file.**

* Run the migrations:

```  sh     
TryPython/manage.py migrate
```

* Load the fixtures of the project

```sh
TryPython//manage.py loaddata steps.json
```

## Running <a name="running"></a>

* Run

```sh       
 TryPython//manage.py runserver 8000
 ```


Now, just access [localhost:8000](localhost:8080)

## Contributing <a name="contributing"></a>

* See the contributing [guide](CONTRIBUTING.md)

* This project uses TravisCI [TryPython on Travis](https://travis-ci.org/IuryAlves/TryPython)
* This project uses [jquery.console](https://github.com/chrisdone/jquery-console)
