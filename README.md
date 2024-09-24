#keylogger software : 
I created a Python script that runs in the command prompt and sends key logging information to the email address I specify. This way, we can monitor how someone else is using our system.
Keylogger Features and Implementation

##**This keylogger project implements several features, including:**
Keystroke Recording: Captures keystrokes typed on the target system.
Remote Monitoring: Allows for monitoring the keylogger's activity from a remote location.
Web History Logging: Records websites visited by the user.
Screenshot History: Takes periodic screenshots of the target system's screen.
Invisible Mode & Password Protection: Ensures the keylogger operates discreetly and requires a password for access.
Application Monitoring and File Tracking: Tracks running applications and file activity on the target system.
Email Reports: Sends regular reports of captured data to a specified email address.

##**Modules Used:**
smtplib: Used for sending email reports.
threading: Provides multi-threading capabilities for efficient operation.
pynput: Allows for monitoring and controlling keyboard and mouse input.
