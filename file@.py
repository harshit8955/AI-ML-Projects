import smtplib
from email.message import EmailMessage
from pathlib import Path

sender = "harshitgunjan8020@gmail.com"
receiver = "Harshit6549@gmail.com"
password = "vvap ngto rjsv zsst"  # Replace with your actual password or use an app password for Gmail. 


msg = EmailMessage()
msg['Subject'] = "file sending Email"
msg["From"] = sender
msg["To"] = receiver

msg.set_content("This is a test email sent from Python with an attachment.")

with open("file@.py", "rb") as f:
    file_data = f.read()
    file_name = Path(f.name).name
    
msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)
    
print("Email sent successfully with attachment!")