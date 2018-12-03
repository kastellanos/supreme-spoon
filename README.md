# Steps to reproduce the vulnerability

- First, we need to create a network "test-network", that will be used by the two containers (client and server) to communicate:
```
docker network create "test-network"
```

- Build the docker image with the vulnerable server, the server listens on the port 3373
```
cd server
docker build -t serveur-faille-1 .
docker run  -d --rm --network="test-network" --name serveur-vulnerable serveur-faille-1:latest
```

- Follow the instructions in README.md inside the client folder.

