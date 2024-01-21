import smtplib
from email.message import EmailMessage

email_content = '''Dear Sir/Ma\'am,

I am Akshat. How are you ? I'm Fine.

Regards
Akshat Parakh
'''

email = EmailMessage()

email['Subject'] = 'Test Message'
email['From'] = 'you@gmail.com'
email['To'] = 'someoneelse@gmail.com'

email.set_content(email_content)

smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_connector.starttls()
# smtp_connector.login('akakak@gmail.com','akakakaka')

smtp_connector.send_message(email)
smtp_connector.quit()
