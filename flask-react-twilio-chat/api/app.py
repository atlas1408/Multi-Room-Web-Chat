import os
import click
from dotenv import load_dotenv
from flask import Flask, request, abort
from flask.cli import AppGroup
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

load_dotenv()
twilio_client = Client()

app = Flask(__name__)

chatrooms_cli = AppGroup('chatrooms',help='Manage your chat rooms.')
app.cli.add_command(chatrooms_cli)

@chatrooms_cli.command('list',help='list all chat rooms')
def list():
	conversations = twilio_client.conversations.conversations.list()
	for conversation in conversations:
		print(f'{conversation.friendly_name} ({conversation.sid})')