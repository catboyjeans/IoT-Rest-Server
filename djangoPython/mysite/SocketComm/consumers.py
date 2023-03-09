from channels.generic.websocket import WebsocketConsumer

from random import randint
from time import sleep
import json

# from ServerEcho.models import Person

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        a = self.scope['url_route']['kwargs']['id']
        
        self.send(text_data=json.dumps({'message':'OwO','Payload': a}))

        # for i in range(100):
        #     self.send(text_data=json.dumps({'message':'OwO','data':randint(1,100)}))
        #     sleep(1)
