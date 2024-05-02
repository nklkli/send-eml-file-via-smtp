import email
import smtplib
from pathlib import Path

path_to_eml_file = Path(__file__).parent / "mail_html.eml"

with open(path_to_eml_file) as f:
    msg = email.message_from_file(f)

smtp = smtplib.SMTP('localhost')

smtp.send_message(msg)
