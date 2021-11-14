import pytesseract as tsc
import os 
import re
import smtplib
from decouple import config
#Definir ruta de las imagenes 
ruta=r"C:\Users\loicp\OneDrive\Escritorio\RankFighters\frames"
frames=os.listdir(ruta)
print(frames)
NombreImpresora=""

for elemento in frames:
    if elemento.split(".")[-1] in ('PNG','jpg','jpeg','tiff'):
        textoDeImagen = tsc.image_to_string(ruta+'\\'+elemento)
        lista=[textoDeImagen]

dataList = re.split(r',|\.| ',textoDeImagen) # split the string
print(dataList)
print(dataList[9])
if dataList[9]=='100%\n\nEO':
    message="ALERTA TU IMPRESION A FINALIZADO CORRECTAMENTE"
    subject="ALERTA TU IMPRESION A FINALIZADO CORRECTAMENTE, de la impresora"+NombreImpresora
    message= 'Subject: {}\n\nn{}'.format(subject, message)
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('correo',config('contraseñacorreo'))
    server.sendmail('correodelqueenvia,correalquellega',message)
    server.quit()
if dataList[13]=='Temp\n\n215/205C':
    message="ALERTA TU IMPRESION ESTA A UNA TEMPERATURA PELIGROSA"
    subject="LERTA TU IMPRESION ESTA A UNA TEMPERATURA PELIGROSA, de la impresora"+NombreImpresora
    message= 'Subject: {}\n\nn{}'.format(subject, message)
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('correo',config('contraseñacorreo'))
    server.sendmail('correodelqueenvia,correalquellega',message)
    server.quit()

