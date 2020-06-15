import smtplib
fromaddr = input('your email: ')
toaddrs = input('Recippent email: ')
msg = input('Msg: ')
username = fromaddr
password =input('Password: ')
server = smtplib.SMTP('smtp.gmail.com:587')
server.set_debuglevel(1)
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
