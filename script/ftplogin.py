from ftplib import FTP
ftp = FTP('dftp.debian.org')     # connect to host, default port
if ftp.login():
    print ('logged in')                     # user anonymous, passwd anonymous@
    ftp.retrlines('LIST')           # list directory contents
    ftp.retrbinary('RETR README', open('README', 'wb').write)
    ftp.quit()
else:
    print ('nothing')

# ftp.cwd('debian')               # change into "debian" directory

