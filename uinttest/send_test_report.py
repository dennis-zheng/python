
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os
import sys

def sendEmail(filiList):
    message = MIMEMultipart("alternative")

    for filePath in filiList:
        with open(filePath) as fp:
            html = fp.read()
            message.attach(MIMEText(html, "html", 'utf-8'))

            att1 = MIMEText(html, 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            att1["Content-Disposition"] = 'attachment; filename="%s"'%filePath
            message.attach(att1)
        message.attach(MIMEText("<html>-------------------------------------------------------------------</html>", "html"))

    mail_host = "smtp.exmail.qq.com"
    mail_port = 465
    mail_user = "dennis@qq.com"
    mail_pass = 'password'

    sender = mail_user
    to_receivers = [mail_user]
    cc_receivers = [mail_user]
    receivers = to_receivers + cc_receivers

    message['Subject'] = 'Test Report, Send by Unittest Auto'
    message['From'] = mail_user
    message['To'] = ";".join(to_receivers)
    message['Cc'] = ";".join(cc_receivers)

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.close()
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

def get_report(testreport):
    filiList = []
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + './' + fn))
    for filePath in lists:
        file = os.path.join(testreport, filePath)
        if os.path.isfile(file):
            filiList.append(file)
        #print(file)
    return filiList

if __name__ == '__main__':
    print('enter')
    test_report = './report'
    argTmp = sys.argv[0]
    if len(sys.argv) > 1:
        test_report = sys.argv[1]
        sys.argv = []
        sys.argv.append(argTmp)
    fileList = get_report(test_report)
    #print(fileList)
    sendEmail(fileList)
    print('exit')