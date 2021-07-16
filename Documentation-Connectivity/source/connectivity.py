## Connectivity####
from SM import SM
class Parallel_SIMO(SM):
    """
    Class which is responsible to connect two different machine which accepts the same input and produce two different output. Inherited from parent state machine

    parameters:sm1, sm2

        sm1 and sm2=machine1 and machine2
    """
    # Class which is responsible to connect two different machine which accepts the same input and produce two different output
    # parallel_SIMO=>Single inp but different o/p

    def __init__(self, sm1, sm2):# The constructors are machine_0,machine_1
        self.m1 = sm1
        self.m2 = sm2
        self.startState = (sm1.startState, sm2.startState)  #  Just initiatlise the newSystem's  startstate with
        # the startstate of the constituent machines.

    def getNextValues(self, state, inp):
        """
        The function which tells what to connect where to take state and apply common input ,then do what the machine is instructed to do.
        Then provide multiple output"""
        # Take state and apply common input ,then do what the machine is instructed to do
        # Then provide multiple output
        # Here it is..
        #          ---->(Machine_1)---->
        #  inp---->
        #            ---->(Machine_2)---->
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), (o1, o2))
    def __str__(self):
        return "single i/p differetial o/p combination of  "+ self.m1.__str__()+"  and  "+self.m2.__str__()
class Cascade(SM):    # Class which is responsible to connect two different machine in a cascade manner
    """
    Class which is responsible to connect two different machine in a cascade manner. Inherited from parent state machine

    parameters:sm1, sm2

        sm1 and sm2= machine1 and Machine2
    """
    #cascade==>> inp-->(Machine_1 )-->(Machine_2)-->output
    def __init__(self, sm1, sm2):# The constructors are machine_0,machine_1
        self.startState = (sm1.startState, sm2.startState)
        #  Just initiatlise the newSystem's  startstate with the startstate of the constituent machines.
        self.sm1 = sm1
        self.sm2 = sm2
    def getNextValues(self, state, inp):# The function which tells what to connect where
        """
        Defines the connection configurations. ie the connection is done in a cascade manner here.
        """
        # Here it is
        ###  =>> inp-->(Machine_1 )-->(Machine_2)-->output

        (newstate1, output1) = self.sm1.getNextValues(state[0],inp)
        (newstate2, output2) = self.sm2.getNextValues(state[1],output1)
        return ((newstate1,newstate2), output2)
    def __str__(self):
        return "Cascade combination of  "+ self.sm1.__str__()+"  and  "+self.sm2.__str__()
class Parallel_MIMO (Parallel_SIMO):# This class inherites from the Parallel_SIMO class
    """
    This class inherites from the Parallel_SIMO class. And is responsible to connect two different machine which accepts the two different input and produce two different output
    """
    # parallel_MIMO=>different inp but different o/p
    def getNextValues(self, state, inp):
        """
        Defines the connection configuration. Take state and apply different input to each machine ,then do what the machine is instructed to do and provide multiple output"""
        # The function which tells what to connect where
        # Take state and apply different input to each machine ,then do what the machine is instructed to do
        # Then provide multiple output
        # This is what it is   ::
        #  inp_0  ---------->(Machine_0)-------> out_0
        #
        #    inp_1  ---------->(Machine_1)-------> out_1
        (s1, s2) = state
        (i1, i2) = (inp[0],inp[1])
        (newS1, o1) = self.m1.getNextValues(s1, i1)
        (newS2, o2) = self.m2.getNextValues(s2, i2)
        return ((newS1, newS2), (o1, o2))
    def __str__(self):
        return "differetial i/p differetial o/p combination of  ,"+ self.m1.__str__()+"  ,  "+self.m2.__str__()
