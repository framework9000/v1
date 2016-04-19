import subprocess

hostname = "10.20.16.30"
output = subprocess.Popen(["ping.exe",hostname],stdout = subprocess.PIPE).communicate()[0]

print(output)

if (b'Gesendet' in output):
    print("Offline")