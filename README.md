# Steps to reproduce the vulnerability
# docker run --network host

- First build the docker image with the vulnerable server
```
cd server
docker build .
#take the image name and later
docker run --network host <image name>
```

- Second, follow the instructions in the client folder Readme

docker run -d -p 3373:3373 --name serveur-vulnerable-x <image-name>
