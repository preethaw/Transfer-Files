import paramiko
import errno
import os
import stat


def connect():	
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect('192.168.137.61', username='pi', password='raspberry')
    ssh.connect('10.0.0.32', username='pi', password='raspberry')
    print ("connected successfully!")
    remote_dir = "/home/pi/openDR/fundus.py/"
    local_dir = "/test_files"
    download_files(ssh,remote_dir,local_dir)

def download_files(ssh,remote_dir, local_dir):

    print("Getting files from",remote_dir)
    sftp_client = ssh.open_sftp()
    if not exists_remote(sftp_client, remote_dir):
        print("Invalid directory name")
        return
    
    if not os.path.exists(local_dir):
        os.mkdir(local_dir)
        print("making dir",local_dir)

    print(sftp_client.listdir(remote_dir))
    for filename in sftp_client.listdir(remote_dir):
        print("Copying... ",remote_dir,filename)
		
        if stat.S_ISDIR(sftp_client.stat(remote_dir + filename).st_mode):
            # uses '/' path delimiter for remote server
            download_files(ssh, remote_dir + filename + '/', os.path.join(local_dir, filename))
        else:
            if not os.path.isfile(os.path.join(local_dir, filename)):
                sftp_client.get(remote_dir + filename, os.path.join(local_dir, filename))
                	
			

def exists_remote(sftp_client, path):
    try:
        sftp_client.stat(path)
    except IOError as e:
        if e.errno == errno.ENOENT:
            return False
        raise
    else:
        return True
		
		
