#!/usr/bin/python3

import os
import io
import asyncore
import requests               # yum install python-requests
import smtpd
from datetime import datetime

# Optional:
listen_addr = os.environ['SMTP2TG_LISTEN_ADDR'] if 'SMTP2TG_LISTEN_ADDR' in os.environ else 'localhost'
listen_port = os.environ['SMTP2TG_LISTEN_PORT'] if 'SMTP2TG_LISTEN_PORT' in os.environ else 2525
# Required:
bot_token   = os.environ['SMTP2TG_BOT_TOKEN']
chat_id     = os.environ['SMTP2TG_CHAT_ID']

class smtp2tg(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, mail_options=None, rcpt_options=None):
        nowstr   = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        markdown = '=== MAIL FROM: %s\n```\n%s\n```' % (mailfrom, data.decode("utf-8"))
        msgfmt   = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&parse_mode=Markdown&text=%s'
        response = requests.get(msgfmt % (bot_token, chat_id, markdown))
        print(f"{nowstr} -- from={mailfrom} to={rcpttos} status={response.status_code} response={response.text}\n")

server = smtp2tg((listen_addr, int(listen_port)), None)
print("Started on %s:%s..." % (listen_addr, listen_port))

try:
    asyncore.loop()
except KeyboardInterrupt:
    pass
