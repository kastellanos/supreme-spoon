import paramiko

host = '127.0.0.1'
port = 3373


trans = paramiko.Transport((host, port))
trans.start_client()

# If the call below is skipped, no username or password is required.
#trans.auth_password('username', 'password')

sftp = paramiko.SFTPClient.from_transport(trans)
print(sftp.listdir('.'))
sftp.close()
