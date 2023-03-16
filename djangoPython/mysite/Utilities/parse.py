
def logging():
    print('jijija')

#   Returned a formated dict in the form of {'State Vector': <dict of state vector>}
def parseQuery(modelInstance):

    stateVector = [
        modelInstance.state1,
        modelInstance.state2,
        modelInstance.state3,
        modelInstance.state4,
        modelInstance.state5,
        modelInstance.state6,
        modelInstance.state7
    ]

    query = {'s{}'.format(i) : str(stateVector[i]) for i in range(len(stateVector))}

    return {'Thing name': modelInstance.first_name,
            'State Vector': query}


