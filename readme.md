# Running the server
```
uvicorn main:app --host 127.0.0.1 --port 80
```
# Building docker container
```
docker build -t landsbjorg_sar_image .
```
# Start the container
```
docker run -d --name landsbjorg_sar_container -p 80:80 landsbjorg_sar_image
```
# Push to Azure
```
az login
az acr login --name landsbjorgsar.azurecr.io

docker tag landsbjorg_sar_image landsbjorgsar.azurecr.io/landsbjorg_sar_container:v1
docker push landsbjorgsar.azurecr.io/landsbjorg_sar_container:v1
```
