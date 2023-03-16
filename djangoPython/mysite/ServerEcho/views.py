from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Person


# Create your views here----------------------------------------------------------------------------------

#   Utility functions ===================================================================================
#URL request handler
def URL_handler(request):

    temp= request.GET
    #could add handle by checking the dict value per value
    temp_vec=[  
    temp.get('s0',0),
    temp.get('s1',0),
    temp.get('s2',0),
    temp.get('s3',0),
    temp.get('s4',0),
    temp.get('s5',0), 
    temp.get('s6',0),
    ]

    vector_state={'s{}'.format(j):temp_vec[j] for j in range(len(temp_vec))}
    argDict={'Vector State: ' : vector_state}

    return argDict

#Apply changes to database
def apply_changes(Person):

    pass

    # Person.state1 = query['Vector State: ']['s0']
    # Person.state2 = query['Vector State: ']['s1']
    # Person.state3 = query['Vector State: ']['s2']
    # Person.state4 = query['Vector State: ']['s3']
    # Person.state5 = query['Vector State: ']['s4']
    # Person.state6 = query['Vector State: ']['s5']
    # Person.state7 = query['Vector State: ']['s6']
    # Person.last_name = 'Cat goes here'
    
    # Person.save()

#   Actual Pages ===================================================================================

#tutorial page 
def index(request):
    return HttpResponse("Print a nice page with an overall tutorial")

#echo'ing implementation 
def recieve_message(request, thing_name):

    query = URL_handler(request)

    if Person.objects.filter(first_name=thing_name).exists():
        query.update({'Debugg State':'Object found in database, value assigned to object'})
        p=Person.objects.filter(first_name=thing_name).first()

    else:
        query.update({'Debugg State':'Object not found in database, creating object ... '})
        p=Person(first_name=thing_name)

    #   Apply changes to database
    
    p.last_name = 'Cat goes here'

    p.state1 = query['Vector State: ']['s0']
    p.state2 = query['Vector State: ']['s1']
    p.state3 = query['Vector State: ']['s2']
    p.state4 = query['Vector State: ']['s3']
    p.state5 = query['Vector State: ']['s4']
    p.state6 = query['Vector State: ']['s5']
    p.state7 = query['Vector State: ']['s6']

    p.recieved = True
      
    p.save()

    return JsonResponse(query)

def get_data(request, thing_name):

    query={}

    if Person.objects.filter(first_name=thing_name).exists():
        query.update({'Debugg State':'Object found in database!! Values will be displayed'})

        p=Person.objects.filter(first_name=thing_name).first()
        query.update({'s0' : p.state1})
        query.update({'s1' : p.state2})
        query.update({'s2' : p.state3})
        query.update({'s3' : p.state4})
        query.update({'s4' : p.state5})
        query.update({'s5' : p.state6})
        query.update({'s6' : p.state7})

    else:
        query.update({'Debugg State':'Object not found in database... '})

    query.update({'All Data' : 'This is a Placeholder'})
        
    return JsonResponse(query)