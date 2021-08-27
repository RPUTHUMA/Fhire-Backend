# Fhire-Backend

### Pyenv setup
For more details please visit [pyenv website](https://github.com/pyenv/pyenv)
OR
[linux pyenv setup](https://www.tecmint.com/pyenv-install-and-manage-multiple-python-versions-in-linux/)

### Instructions for Mac OS
`brew install pyenv`

### Installing python 3.7.x

```
pyenv install 3.7.3
echo "export PATH=~/.pyenv/versions/3.7.3/bin:$PATH" >> ~/.bash_profile
source ~/.bash_profile
```

### Create database
Create a database 'fhire' using PSQL Admin.

# Install Fhire-backend

## clone repository
`git clone

## create symlinks
#### Run this step one directory behind Fhire-backend directory
`mkdir -p /usr/local/opt`
`ln -s $(pwd)/Fhire-Backend /usr/local/opt/`

## install Fhire-Backend
`cd Fhire-Backend`

## create directory logs
`mkdir logs`

## create a blank log file
`touch logs/Fhire-Backend.log`

## virtual environment setup
`virtualenv --python={python path} env`

## activate virtual environment
`source env/bin/activate`

##install the pip packages
`make install`

## Running application


### run flask development server (for development)
`make run`
### run gunicorn server (for production)
`make gunicorn`


open `http://localhost:5000/` in browser to access the application
open `http://localhost:5000/fhire/api/docs#/` in browser to access Flasgger

### Running test cases

```
make test  # run test cases using pytest
```

### Running docker images

```
docker login docker_registry
docker pull image-tag:xxxx
docker run --publish 5000:5000 image-tag:xxxx
```

Note: replace xxxx with the version before running
