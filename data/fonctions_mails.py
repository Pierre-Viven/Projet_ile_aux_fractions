import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def envoyerMail():
	json_file = open("data\config.json")
	gmail_cfg = json.load(json_file)


	msg = MIMEMultipart()
	msg["To"] = gmail_cfg["email"]
	msg["From"] = gmail_cfg["email"]
	msg["Subject"] = "test"
	message = "lalakshdhdjddn"
	msg.attach(MIMEText(message, "plain"))

	fichier_a_attacher = "data/lalalala.xlsx"

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


	with smtplib.SMTP_SSL(gmail_cfg["server"],gmail_cfg["port"]) as smtp : 
		smtp.login(gmail_cfg["email"], gmail_cfg["pwd"])
		smtp.send_message(msg)
		print("c ok")