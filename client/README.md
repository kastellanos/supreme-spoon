## Requirements

- Python 3
  - paramiko library

## Set-up

- To execute the client it's better to create a virtual environment for that
use the following command:
```
python -m virtualenv venv
source venv/bin/activate
```

- Following install the needed python library
```
pip install -r requirements.txt
```

With that you can execute the python script to connect to the vulnerable server
```
python client.py
```
Doing that it's upon you to find how to get the content of the flag.txt file.

If you need help you can see the documentation http://docs.paramiko.org/en/2.4/api/sftp.html

If you don't arrive to have solve the problem, change the listdir command by
```
sftp.get('flag.txt',"solve.txt")
With that nothing will be printed but you can see the file now with the flag content.
```
