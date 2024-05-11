#Bai54
'''import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(smtp_server, sender_email, passwd, recipient_email, subject):
    #tao doi tuong MIMEMultipart
    msg = MIMEMultipart()

    #Thiet lap thong tin nguoi gui, nhan and chu de mail
    msg['Subject'] = subject
    msg['to'] = recipient_email
    msg['From'] = sender_email

    #nhap noi dung email, ket  thuc bang dong duy nhat chua 1 dau '.'
    print("Nhap noi dung email:")
    lines = [] #them tu vao chuoi
    while True:
        line = input()
        if line == '.':
            break
        lines.append(line)
    message = '\n'.join(lines)

    #tao doi tuong MIMEText cho phan van ban email
    body = MIMEText(message, 'plain') #plain kieu du lieu van ban (them phan giua la noi dung email)

    #them phan van ban (them tat ca user mail gui nhan, no la lon nhat) cuar email
    msg.attach(body)

    smtp_port = 587 #port

    #tao smpt session
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.ehlo()
    smtp.starttls()

    smtp.ehlo()
    smtp.login(sender_email, passwd)
    print("login success!!")
    smtp.sendmail (sender_email, recipient_email, msg.as_string())
    print('Email send!!')


#tham so dau vao
smtp_server = input('Nhap dia chi IP cua SMTP Server: ')
sender_email = input('Nhap dia chi email nguoi gui: ')
passwd = input('nhap passwd: ')
recipient_email = input('Nhap dia chi nguoi nhan: ')
subject = input('Nhap chu de email: ')

#gui email
send_email(smtp_server, sender_email, passwd, recipient_email, subject)
'''
#Bai55





