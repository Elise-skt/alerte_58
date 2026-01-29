import requests
import smtplib
from email.message import EmailMessage
import os

requests.packages.urllib3.disable_warnings()

OBJECTIF = 123_000_000

def recuperer_jackpot():
    url = "https://www.lottoland.com/api/drawings/euromillions"
    donnees = requests.get(url, timeout=10).json()
    return int(donnees["jackpot"]["amount"])


def envoyer_email(jackpot):
    print("👉 Tentative d'envoi de l'email...")

    message = EmailMessage()
    message["Subject"] = "🎉 TEST EuroMillions"
    message["From"] = os.environ["EMAIL_FROM"]
    message["To"] = os.environ["EMAIL_TO"]
    message.set_content(
        f"TEST : email envoyé avec jackpot = {jackpot}"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as serveur:
        serveur.login(
            os.environ["EMAIL_FROM"],
            os.environ["EMAIL_PASSWORD"]
        )
        serveur.send_message(message)

    print("✅ Email envoyé avec succès")


    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as serveur:
        serveur.login(
            os.environ["EMAIL_FROM"],
            os.environ["EMAIL_PASSWORD"]
        )
        serveur.send_message(message)

def main():
    jackpot = recuperer_jackpot()
    if jackpot >= OBJECTIF and jackpot % OBJECTIF == 0:
        envoyer_email(jackpot)

def main():
    envoyer_email(123_000_000)

