import time

from datetime import datetime as dt



#For Windows

#HostPath = r"C:\Windows\System32\drivers\etc\hosts"

#For Mac and Linux

HostPath = "/etc/hosts"

redirect = "127.0.0.1"



website_to_blocks = ["www.facebook.com","facebook.com","youtube.com","www.youtube.com"]



holiday_1 = "Sat"

holiday_2 = "Sun"

start_time = 8

end_time = 20



def add_hosts():

    with open(HostPath, "r+") as file:

        content = file.read()

        for website in website_to_blocks:

            if website in content:

                pass

            else:

                file.write(redirect+" "+website+"\n")

def reset_hosts():

    with open(HostPath,"r+") as file:

        content = file.readlines()

        file.seek(0)

        for line in content:

            if not any(website in line for website in website_to_blocks):

                file.write(line)

                file.truncate()



# //mainprogram starts here

while True:

    if dt.now().strftime("%a") != (holiday_1.title() or holiday_2.title()):

         if dt(dt.now().year,dt.now().month,dt.now().day,start_time) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end_time):

             add_hosts()

             print("working hours.....")

         else:

             reset_hosts()

             print("fun hours.....")

    else:

         reset_hosts()

         print("HoliDays.....")

time.sleep(5)
