from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Person
# Create your views here----------------------------------------------------------------------------------

#URL request handler
def URL_handler(request):

    temp= request.GET
    #could add handle by checking the dict value per value
    temp_vec=[  
    temp.get('s1',0),
    temp.get('s2',0),
    temp.get('s3',0),
    temp.get('s4',0),
    temp.get('s5',0),
    temp.get('s6',0), 
    temp.get('s7',0),
    ]

    vector_state={'element{}'.format(j):temp_vec[j] for j in range(len(temp_vec))}
    argDict={'Vector State: ' : vector_state}

    return argDict

#tutorial page 
def index(request):
    return HttpResponse("Print a nice page with an overall tutorial")

#echo'ing implementation 
def recieve_message(request, thing_name):

    query = URL_handler(request)

    if Person.objects.filter(first_name=thing_name).exists():
        query.update({'Debugg State':'Object found in database, value assigned to object'})

        # Change database value

    else:
        query.update({'Debugg State':'Object not found in database, creating object ... '})
        p1=Person(first_name=thing_name)
        p1.state1 = query['element0']
        p1.state2 = query['element1']
        p1.state3 = query['element2']
        p1.state4 = query['element3']
        p1.state5 = query['element4']
        p1.state6 = query['element5']
        p1.state7 = query['element6']
        p1.last_name = 'Cat goes here'

        #apply changes to database
        p1.save()
    
    p=Person.objects.filter(first_name=thing_name).first()  
    query.update({'Thing Name' : p.first_name})
    query.update({'All Data' : 'This is a Placeholder ^_^'})
        
    return JsonResponse(query)

def get_data(request, thing_name):

    query={}

    if Person.objects.filter(first_name=thing_name).exists():
        query.update({'Debugg State':'Object found in database!! Values will be displayed'})

        p1=Person.objects.filter(first_name=thing_name).first()
        query.update({'element0' : p1.state1})
        query.update({'element1' : p1.state2})
        query.update({'element2' : p1.state3})
        query.update({'element3' : p1.state4})
        query.update({'element4' : p1.state5})
        query.update({'element5' : p1.state6})
        query.update({'element6' : p1.state7})

    else:
        query.update({'Debugg State':'Object not found in database... '})

    query.update({'All Data' : 'This is a Placeholder'})
        
    return JsonResponse(query)
