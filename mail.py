import smtplib
import codecs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PASSWORD = 'ElectromagneticRadiation'


def send_email(sender, receivers, message):

    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(sender, PASSWORD)

        html_file = codecs.open('test.html', 'r', 'utf-8')
        html_text = html_file.read()
        html_file.close()

        html_as_string = ''
        for line in html_text:
            html_as_string += line

        msg = MIMEText(html_text)
        # Subject, From, To are the information, which the receiver will see
        # It's no problem, if you use a fake address here. That's the way, how phishing mail or spam mail works
        msg['Subject'] = 'Index oglasi'
        msg['From'] = sender
        msg['To'] = receivers[0]

        smtpserver.sendmail(sender, receivers, msg.as_string())
        print("Email sent!")
        smtpserver.quit()

    except Exception:
        print("Error: unable to send email")
