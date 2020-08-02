# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:28:24 2020

@author: Saurav
"""

#!/usr/bin/env python3

import email.message
import mimetypes
import smtplib
import os

def generate_email(sender, receiver, subject, body):
    
    attachment_path = "/tmp/processed.pdf"
    
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)
    
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype = mime_type,
                               subtype = mime_subtype,
                               filename = attachment_filename)
    return message
    
def send_email(message):
    
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
