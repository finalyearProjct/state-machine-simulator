from SM import SM
class Delay(SM):
    """
    Class for the Delay machine. Inherited from parent State machine

    parameters:V0

        V0= intial value of the delay box
    """
    def __init__(self, v0=0):# constructor is the initail value of the delay box
        # default value is 0
        self.startState = v0
    def getNextValues(self, state, inp):
        """
        The logic which connect the future state with present input and and present state
        """
        return (inp, state)
    def __str__(self):# This function is the default __str__ method in python class
        return "R"



class Accumulator(SM):     ## Class for the Accumulator machine in 1D
    """
    Class for the Accumulator machine in 1D. Inherited from parent state machine

    parameters:initialValue

        initialValue=intial value of the delay box is given"""
    # This is inherited from SM
    def __init__(self, initialValue=0):# constructor is the initail value of the delay box
        # default value is 0
        self.startState = initialValue
    def getNextValues(self, state,inp):
        """
        The logic which connect the future state with present input and and present state, for accumulator : new_state=state+input"""

        if inp=='undefined':# 'undefined 'is equilvalent to tristate in electronics
            return ('undefined','undefined')
        else: # Do what the machine is intended to do
            return state + inp, state + inp
    def __str__(self): # This function is the default __str__ method in python class
        return "Accumulator"
