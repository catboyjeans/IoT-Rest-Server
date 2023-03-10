from channels.generic.websocket import WebsocketConsumer

from random import randint
from time import sleep
import json

from Utilities.parse import parseQuery

from ServerEcho.models import Person

SAMPLING_RATE = 10
TIME_STEP = 1/SAMPLING_RATE

class WSConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        thing_name = self.scope['url_route']['kwargs']['thing_name']
        
        query={}

        if Person.objects.filter(first_name=thing_name).exists():
            query.update({'Debugg State':'Object found in database, value assigned to object'})
            p=Person.objects.filter(first_name=thing_name).first()
            query.update(parseQuery(p)) ##  add state to query

        else:
            query.update({'Debugg State':'Object not found in database, first create object via http'})

        self.send(text_data=json.dumps(query))

        # for i in range(100):
        #     self.send(text_data=json.dumps({'message':'OwO','data':randint(1,100)}))
        #     sleep(1)