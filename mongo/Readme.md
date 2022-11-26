# Fetch database 

## 1. Obtain docker image

### Option 1: (no build - required DockerHub account)
Login in DockerHub with your credwntials
```shell
docker login
```
Pull the image
```
docker pull emartp/pyday-mongo 
``` 

### Option 2: (build - no account require)
```shell
docker build -t emartp/pyday-mongo .
```

## 2. Run the docker compose
Run the docker-compose 
```shell
docker-compose up
``` 

The database should be accessible at `localhost:27019`. The port is different to the default one (`27019`) to avoid conflict with possible local MongoDB instances.
