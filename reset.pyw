import ctypes, sys
HostPath = r"C:\Windows\System32\drivers\etc\hosts"
#HostPath = r"\etc\hosts"
website_to_blocks = ["www.facebook.com","facebook.com","youtube.com","www.youtube.com"]
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    with open(HostPath,"r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_to_blocks):
                file.write(line)
                file.truncate()
    print("Script reseted")
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
