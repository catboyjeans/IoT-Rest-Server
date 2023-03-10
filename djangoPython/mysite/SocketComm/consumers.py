from channels.generic.websocket import WebsocketConsumer

from time import sleep
import json

from Utilities.parse import parseQuery

from ServerEcho.models import Person, BooleanFlag

import threading

SAMPLING_RATE = 10
TIME_STEP = 1/SAMPLING_RATE

class WSConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

        if BooleanFlag.objects.filter(NAME='unique').exists():
            print('Bool Flag found !!')
            b=BooleanFlag.objects.filter(NAME='unique').first()

        else:
            print('Bool Flag not found, creating one ...')
            b=BooleanFlag(NAME='unique')

        b.save()

        thing_name = self.scope['url_route']['kwargs']['thing_name']
        
        query={}

        if Person.objects.filter(first_name=thing_name).exists():
            query.update({'Debugg State':'Object found in database, value assigned to object'})
            p=Person.objects.filter(first_name=thing_name).first()
            b.LOOP_FLAG = True  #   If found, start looping
            b.save()
            query.update(parseQuery(p)) ##  add state to query
            print('b.LOOP_FLAG = ',b.LOOP_FLAG)

            self.stop = False
            self.thread = threading.Thread(target=self.listening_requests,args=(query,thing_name))
            self.thread.start()


        else:
            query.update({'Debugg State':'Object not found in database, first create object via http'})
            self.send(text_data=json.dumps(query))

    def listening_requests(self,query,thing_name):
        while not self.stop:
                p=Person.objects.filter(first_name=thing_name).first()
                b=BooleanFlag.objects.filter(NAME='unique').first()

                if p.recieved:
                    print(query)
                    p.recieved = False
                    p.save()
                    self.send(text_data=json.dumps(query))

                print('Loop Flag...', b.LOOP_FLAG)   
                sleep(.2)

    def disconnect(self,message):
        print('DISCONNECTING!!!')
        self.stop = True
        del self.thread
        b=BooleanFlag.objects.filter(NAME='unique').first()
        b.LOOP_FLAG = False
        b.save()