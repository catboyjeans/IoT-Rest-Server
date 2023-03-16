#   testing utility functions

class TestClass:
    state1=1
    state2=2
    state3=3
    state4=4
    state5=5
    state6=6
    state7=7

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

    query = {'s{}'.format(i) : stateVector[i] for i in range(len(stateVector))}
    return {'State Vector': query}

this = TestClass()

a = parseQuery(this)

print(a)