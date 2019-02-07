import time
from datetime import datetime as dt

HostPath = r"C:\Windows\System32\drivers\etc\hosts"
#HostPath = r"\etc\hosts"
redirect = "127.0.0.1"

website_to_blocks = ["www.facebook.com","facebook.com","youtube.com","www.youtube.com"]

start_time = 8
end_time = 16

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,start_time) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end_time):
        print("working hours.....")
        with open(HostPath, "r+") as file:
            content = file.read()
            for website in website_to_blocks:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(HostPath,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_to_blocks):
                    file.write(line)
                file.truncate()
        print("fun hours.....")
    time.sleep(5)
