# Swagger generated server

## Overview
This application implements a Swagger server created using the Swagger Codegen.
The Swagger server exposes a REST API that implements the requirements listed in the [instructions](https://bpdts-test-app.herokuapp.com/instructions).
The REST API consumes data returned by the [bpdts-test-app REST API](https://bpdts-test-app.herokuapp.com) and produces a list of users who either live in London or their current location is within 50 miles from it.

## Requirements
[Python 3.5.2+](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

## Install the server
To install the server, clone this repository and change directory into the main folder:
```
git clone https://github.com/wp1234567/wp-app
cd wp-app
```

### Install the server using Python
To run the server, execute the following:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

### Install the server using Docker
To run the server on a Docker container, execute the following:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```

## Browse the API definition
To see the API definition, open the Swagger UI:
```
http://localhost:8080//ui/
```

Or retrieve the Swagger json definition:
```
http://localhost:8080//swagger.json
```

## Invoke the REST API
You can use tools like curl or Postman to invoke the REST API.
Here it is an example on how to invoke the REST API using curl:

```
curl -X GET --header 'Accept: application/json' 'http://localhost:8080/londoners'
```

## Run the tests
### Using tox:
```
sudo pip3 install tox
tox
```
**Note:** You may hit the following error when running tox:
```
  File "/home/richard/wp-app/.tox/py38/lib/python3.8/site-packages/flask_testing/utils.py", line 29, in <module>
   from werkzeug import cached_property
ImportError: cannot import name 'cached_property' from 'werkzeug' (/home/richard/wp-app/.tox/py38/lib/python3.8/site-packages/werkzeug/__init__.py)
```
To work-around the error, edit the file `/home/richard/wp-app/.tox/py38/lib/python3.8/site-packages/flask_testing/utils.py` and replace the line 29th with the following value:
```
from werkzeug.utils import cached_property
```
Then restart tox.  
**Note:** You may see errors in the output of the tox command like this:
```
ERROR:  py37: InterpreterNotFound: python3.7
```
Those error messages can be ignored as they do not cause issues to the execution of the test.

### Using Python
```
sudo pip3 install flask_testing
python3 -m unittest
```
