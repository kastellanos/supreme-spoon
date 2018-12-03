FROM python:3
WORKDIR /experiment/data
ADD requirements.txt .
ADD rsa.key .
ADD flag.txt .
RUN pip install -r requirements.txt

COPY sftpserver.tar.gz .
RUN tar -zxf sftpserver.tar.gz
WORKDIR sftpserver
RUN python setup.py install
WORKDIR /experiment/data
RUN rm -r sftpserver
RUN rm sftpserver.tar.gz
CMD [ "sftpserver", "-k", "rsa.key", "--host", "0.0.0.0", "-l", "DEBUG"]

EXPOSE 3373
