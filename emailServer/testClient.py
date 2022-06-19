#! /usr/bin/env python

from smtplib import SMTP as Client
from mainServer import controller

client = Client(controller.hostname, controller.port)
r = client.sendmail('a@example.com', ['b@example.com'], """\
From: Anne Person <anne@example.com>
To: Bart Person <bart@example.com>
Subject: A test
Message-ID: <ant>
Hi Bart, this is Anne.
""")

