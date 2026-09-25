import smtplib
from email.message import EmailMessage


sender="Harshitgunjan8020@gmail.com"
receiver="Harshit6549@gmail.com"
password="vvap ngto rjsv zsst"  # Replace with your actual password or use an app password for Gmail.


msg=EmailMessage()
msg['Subject']="Test Email"
msg['From']=sender
msg['To']=receiver

msg.set_content("This is a test email sent from Python.")


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)
    
    
print("Email sent successfully!")