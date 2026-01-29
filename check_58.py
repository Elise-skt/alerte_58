import requests
import smtplib
from email.message import EmailMessage
import os

OBJECTIF = 123_000_000

def recuperer_jackpot():
    url = "https://media.lfdj.com/draws/euromillions.json"
    donnees = requests.get(url).json()
    return int(donnees["last"]["jackpot"])


def envoyer_email(jackpot):
    message = EmailMessage()
    message["Subject"] = "🎉 EuroMillions à jouer !"
    message["From"] = os.environ["EMAIL_FROM"]
    message["To"] = os.environ["EMAIL_TO"]
    message.set_content(
        f"Le jackpot EuroMillions est de {jackpot:,} €.\n"
        f"C'est un multiple de 58 millions."
    )

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

main()
