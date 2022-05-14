import pyscreenshot
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

pedir = input("Introducir ruta de la carpeta con el nombre y formato de la imagen")
ruta=pedir

imagen = pyscreenshot.grab()
imagen.save(ruta)

msg = MIMEMultipart()
msg['Subject'] = 'Correo con imagen Adjunta'
msg['From'] = 'jalcytestpias@gmail.com'
msg['To'] = 'julioadrianlanderos@gmail.com'

text = MIMEText("test")
msg.attach(text)

file = open(ruta, 'rb').read()
pic = MIMEImage(file)
pic.add_header('Content-Disposition', 'attachment; filename = "screenshot.png"')
msg.attach(pic)

mailServer = smtplib.SMTP('smtp.gmail.com',587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login('jalcytestpias@gmail.com', 'eogomjrkwyrepfsx')
mailServer.sendmail('jalcytestpias@gmail.com', 'julioadrianlanderos@gmail.com', msg.as_string())
mailServer.quit()