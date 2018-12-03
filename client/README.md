## Requirements

- Python 3
  - paramiko library

## Set-up

- 1) We will build and run the client container and get bash inside it.
```
cd client/
docker rm -f client-para .
docker run -it --network="test-network" --rm  --name client-para client-para:latest
```

- 2) We run this command to execute the client script which will display the contents of the directory /experiment/data on the server.
```
python client.py
```
Doing that we succeeded in getting the contents of a directory on the server without any authentication.

- We can exit the client container by pressing Ctrl+D.

- Now it's up to you to find how to get the content of the flag.txt file.
If you need help, you can see the documentation: http://docs.paramiko.org/en/2.4/api/sftp.html
If you don't arrive to solve the problem, replace "print(sftp.listdir('.'))" in client.py with "sftp.get('flag.txt',"solve.txt")".

- We rebuild and run the client image (steps 1) and 2)), and we execute (inside the client container), the command:
```
cat solve.txt
```
We've just moved the flag.txt file to the client side (solve.txt) without any authentication.
