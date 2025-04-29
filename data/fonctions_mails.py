import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
import socket


def EnvoyerMail():
	json_file = open("data\config.json")   #données du fichier json : a changer selon l'adresse mail utilisée
	gmail_cfg = json.load(json_file)


	msg = MIMEMultipart()
	msg["To"] = gmail_cfg["email"]
	msg["From"] = gmail_cfg["email"]
	msg["Subject"] = "Data"
	message = f"Données récoltées par le jeu memory île aux fractions le {datetime.datetime.now().strftime('Le %d-%m-%Y à %HH%M')} depuis l'IP {socket.gethostbyname(socket.gethostname())}"

	msg.attach(MIMEText(message, "plain"))

	fichier_a_attacher = "data.xlsx"

	with open(fichier_a_attacher, "rb") as attachment:
				part = MIMEBase("application", "octet-stream")
				part.set_payload(attachment.read())

	# Encoder la pièce jointe en Base64
	encoders.encode_base64(part)
	part.add_header(
		"Content-Disposition",
		f"attachment; filename={fichier_a_attacher}",
	)
	msg.attach(part)

	try:
		with smtplib.SMTP_SSL(gmail_cfg["server"],gmail_cfg["port"]) as smtp : 
			smtp.login(gmail_cfg["email"], gmail_cfg["pwd"])
			smtp.send_message(msg)
			return "envoyé"
	except smtplib.SMTPException as e:
		return "Échec de l'envoi du message :", e
	
		
