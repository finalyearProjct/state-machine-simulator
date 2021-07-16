from SM import SM
class Two_Dimen_Accumulator(SM):
    """This class is for implementing accumulator in 2 -D. Inherited class from parent state machine

    parameters:

        intialValue= setting the intial conditions
    """
    def __init__(self, initialValue=[0,0]):# The constructor is for setting the initial conditions
        self.startState = initialValue
    def getNextValues(self, state, inp):# This function which is responsible for giving out next value
        # given present state and present input.
        """
        This function which is responsible for giving out next value given present state and present input. It contain the logic which connect the
        future state with present input and and present state for 2D_accumulator : new_state_0=state_0+input_0,new_state_1=state_1+input_1.
        """
        ## It contain the logic which connect the
        # future state with present input and and present state
        # for 2D_accumulator : new_state_0=state_0+input_0,new_state_1=state_1+input_1

        return ((state[0] + inp[0],state[1] + inp[1]),(state[0] + inp[0],state[1] + inp[1]))



class increamenter(SM):# This class is used to increament the input value by a certain_value
    """
    This class is used to increament the input value by a certain_value. Inherited class from parent state machine

    parameters:incremente_values

        incremente_values=incrementer value"""
    def __init__(self,increment_value):# In the constructor user can set the increamenter value
        self.increament_value=int(increment_value)
        self.startState=0       # Here start state have no relevence
    def getNextValues(self, state, inp):# The function increaments the input sample by a certain value
        """
        The function increaments the input sample by a certain value.
        """

        if inp=='undefined':# 'undefined 'is equilvalent to tristate in electronics
            return ('undefined','undefined')
        else:# Do what the machine is intended to do
            return (inp+self.increament_value,inp+self.increament_value)
    def __str__(self):
        return "Incrementer"

class Gain(SM):  # This class is more like an amplifier in electronics,it will scale the input value by a cetain value
    """
    This class is more like an amplifier in electronics,it will scale the input value by a cetain value

    parameters:k

        k= gain value
    """
    def __init__(self,k):# The constructor is for initialising the gain value,ie the scaling factor
        self.k=k
        self.startState=1 ## Initial  state have no such relevance
    def getNextValues(self,state,inp):# This function is used to scale the input stream by a factor of k
        """
        This function is used to scale the input stream by a factor of k
        """
        if inp=='undefined':# 'undefined 'is equilvalent to tristate in electronics
            return ('undefined','undefined')
        else:# Do what the machine is intended to do,here amplify
            return inp*self.k,inp*self.k
    def __str__(self):
        return "Amplifier"

class MovingAvg2(SM):# This  class is used to compute the moving average of order 2 from a stream of numbers
    """
    This  class is used to compute the moving average of order 2 from a stream of numbers. Inherited class from parent state machine

    parameters:intialValue

        initialValue=intial value is given Here
    """
    def __init__(self,initialValue):# The initial value is given here
        self.startState=initialValue
    def getNextValues(self,state,inp):
        """
        Function  which provide the logic which connect the future state with present input and and
        present state for Moving average 2 it is (((present_sample)+(past_sample))/2)
        """
        # Function  which provide the logic which connect the
        #  future state with present input and and present state
        # for Moving average 2 it is (((present_sample)+(past_sample))/2)
        self.inputlist.append(inp)
        return inp,(self.inputlist[len(self.inputlist)-1]+self.inputlist[len(self.inputlist)-2])/2
    def __str__(self):
        return "Moving Average-2"

class MovingAvg3(SM):# This  class is used to compute the moving average of order 3 from a stream of numbers
    """
    This  class is used to compute the moving average of order 3 from a stream of numbers. Inherited class from parent state machine

    parameters:initialValue

        intialValue=intial value is given Here
    """
    def __init__(self,initialValue):# The initial value is given here
        self.startState=initialValue
        self.inputlist=list([0,0]) # This is important because we want to access the past 2 samples
    def getNextValues(self,state,inp):
        """
        Function  which provide the logic which connect the future state with present input and and present state
        for Moving average 3 it is (((present_sample)+(past_sample)+(past_sample))/3)
        """
        # Function  which provide the logic which connect the
        #  future state with present input and and present state
        # for Moving average 3 it is (((present_sample)+(past_sample)+(past_sample))/3)
        self.inputlist.append(inp)
        return inp,(self.inputlist[len(self.inputlist)-1]+self.inputlist[len(self.inputlist)-2]+self.inputlist[len(self.inputlist)-3])/3
    def __str__(self):
        return "Moving Average-3"
class updowncounter(SM):# This class is used  to implement updown counter based on the input [1,0]
    """
    This class is used  to implement updown counter based on the input [1,0]. Inherited class from parent state machine

    parameters:init_state

        Intial state of the system is passed
    """
    # the state of the system is increamented or decreamented.
    def __init__(self,init_state):# The constructor is  the initail_state of the sytem
        self.startState=init_state
    def getNextValues(self,state,inp):
        """
        Function  which provide the logic which connect the future state with present input and and present state
        for updown counter : if input is 1: increament the state,else decreament the state
        """
        # Function  which provide the logic which connect the
        #  future state with present input and and present state
        # for updown counter : if input is 1: increament the state,else decreament the state

        if inp==1:
            return state+1,state+1
        else:
            return state-1,state-1
    def __str__(self):
        return "Up/Down Counter"
