# Website Blocker
# Use this to stay away from distraction while working and studying

//---------------------------------Run Scripts -------------------------------//

# For Windows:

Host file location: C:\Windows\System32\drivers\etc\hosts

To Run Python script without console you need pythonw.exe in your installation directory and File should be in .pyw extensions

To change this host file you need administrative privilege

  1.1 open Task Scheduler(built-in app)

  1.2 Create New Task

  1.3 Setup

      //General Tab
      1.3.1 Give Name
      1.3.2 check Run with highest Privileges
      1.3.3 choose your Preferred OS
      //Triggers Tab
      1.3.4 Create  New Trigger
      1.3.5 Select the At the start up in Begin the task
      //Action Tab
      1.3.6 Create New Action
      1.3.6 Locate the Script file
      //Condition Tab
      1.3.7 Uncheck Power options
      1.3.8 Ok


# For Mac and Linux:

Host file location: \etc\hosts

To Run Python script, File should be in .py extensions

To change this host file you need administrative privilege

    2.1 sudo crontab -e

    2.2 Add Following line(Path to the python file or scripts)

        @reboot python3 /home/username/applications/website_blocker.py

//-----------------------Change Time and Block Websites-----------------------//

Open website_blocker.pyw

# To add Websites

Enter new websites in the variable(with quotes)

    3.1 website_to_blocks

# To add Holiday 

Enter the day (3 letters inside the string) in the variable

    4.1 holiday_1
    
    4.2 holiday_2
    
# To change the time

Enter the value in the variable

    5.1 start_time

    5.2 end_time

//--------------------------ToReset the host file----------------------------//

# To Reset Host file

Run the reset.py


