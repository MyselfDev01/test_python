# fastapi-test_task

A test_task of using Fast API in Python.

## Preconditions:

- Python 3



## Run local


### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn main:app --reload
```


### Mongodb connection


```
sudo service mongodb start

```

## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```


### Libraries

Fastapi- pip install fastapi 
### Referencelink 
https://fastapi.tiangolo.com/

### Purpose to use
FastAPI allow  asynchronous execution and pydantic schema web applications to be written efficiently in clean, modern Python code with type hints.

odmantic- pip install odmantic
### Referencelink 

https://art049.github.io/odmantic/

### Purpose to use
Sync and Async ODM (Object Document Mapper) for MongoDB based on standard python type hints. Built on top of pydantic for model definition and validation.
