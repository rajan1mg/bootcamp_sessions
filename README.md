# What is this Service?
- Local Debugging Bootcamp session 2024


## Repo Setup

```bash
1. Install python version 3.9.16
2. pip3 install sanic
3. pip3 install pydantic
```

## Run Configurations
- Pycharm 
  - module >> app.server
  - working dir > complete path till "project repo"
- ensure virtual env is activated (venv preferred)
- python3 -m app.server

### Sample Handlers

```shell
curl --location --request POST 'http://localhost:8021/v1/users/signup' \
--header 'Content-Type: application/json' \
--data-raw '{
    "age": 23,
    "email": "rajan.agarwal1@gmail.com",
    "password": "1234323",
    "privacy_policy": "agree"
}'
```