
import smtplib
fromaddr = input('Input your Gmail address: ')
toaddrs  = input('Input recipient email address: ')
msg = input('Write the msg: ')
username = formaddr
password = input('Input Password')
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
