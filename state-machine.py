from matplotlib import pyplot as plt
import numpy as np


class SM:                                      # Parent Machine  #
    def start(self):
        self.state=self.startState
        self.inputlist=list([0])
    def step(self,inp):
        (s, o) = self.getNextValues(self.state,inp)
        self.state =s
        return o
    def transduce(self,inputs):
        self.start()
        return [self.step(inp) for inp in inputs]
    def run(self,n=10):
        return self.transduce([None] * n)


class Delay(SM):
    def __init__(self, v0):
        self.startState = v0
    def getNextValues(self, state, inp):
        return (inp, state)
    def __str__(self):
        return "R"


class Accumulator(SM):                          #   Accumulator  #
    def __init__(self, initialValue):
        self.startState = initialValue
    def getNextValues(self, state,inp):
        if inp=='undefined':
            return ('undefined','undefined')
        else:
            return state + inp, state + inp
    def __str__(self):
        return "Accumulator"


class Two_Dimen_Accumulator(SM):
    def __init__(self, initialValue):
        self.startState = initialValue
    def getNextValues(self, state, inp):
        return ((state[0] + inp[0],state[1] + inp[1]),(state[0] + inp[0],state[1] + inp[1]))


class increamenter(SM):
    def __init__(self,increment_value):
        self.increament_value=int(increment_value)
        self.startState=0
    def getNextValues(self, state, inp):
        if inp=='undefined':
            return ('undefined','undefined')
        else:
            return (inp+self.increament_value,inp+self.increament_value)
    def __str__(self):
        return "Incrementer"


class Gain(SM):                                 # Amplifier     #
    def __init__(self,k):
        self.k=k
        self.startState=1
    def getNextValues(self,state,inp):
        if inp=='undefined':
            return ('undefined','undefined')
        else:
            return inp*self.k,inp*self.k
    def __str__(self):
        return "Amplifier"


class MovingAvg2(SM):
    def __init__(self,initialValue):
        self.startState=initialValue
    def getNextValues(self,state,inp):
        self.inputlist.append(inp)
        return inp,(self.inputlist[len(self.inputlist)-1]+self.inputlist[len(self.inputlist)-2])/2
    def __str__(self):
        return "Moving Average-2"


class MovingAvg3(SM):
    def __init__(self,initialValue):
        self.startState=initialValue
        self.inputlist=list([0,0])
    def getNextValues(self,state,inp):
        self.inputlist.append(inp)
        return inp,(self.inputlist[len(self.inputlist)-1]+self.inputlist[len(self.inputlist)-2]+self.inputlist[len(self.inputlist)-3])/3
    def __str__(self):
        return "Moving Average-3"


class UpDownCounter(SM):
    def __init__(self):
        self.startState=0
    def getNextValues(self,state,inp):
        if inp=='u':
            return state+1,state+1
        else:
            return state-1,state-1
    def __str__(self):
        return "Up/Down Counter"


class NOT_GATE(SM):
    def __init__(self):
        self.startState=True
    def getNextValues(self, state, inp):
        if inp=='undefined':
            return ('undefined','undefined')
        else:
            return (state, not(inp))
    def __str__(self):
        return "NOT-Gate"


class NAND_GATE(SM):
    def __init__(self):
        self.startState=None
    def getNextValues(self, state, inp):
        if inp[0]=='undefined' or inp[1]=='undefined':
            return ('undefined','undefined')
        else:
            return (state,not(bool.__and__(inp[0],inp[1])))
    def __str__(self):
        return "NAND-Gate"


class NOR_GATE(SM):
    def __init__(self):
        self.startState=None
    def getNextValues(self, state, inp):
        if inp[0]=='undefined' or inp[1]=='undefined':
            return ('undefined','undefined')
        else:
            return (state,not(bool.__or__(inp[0],inp[1])))
    def __str__(self):
        return "NOR-Gate"


class XOR_GATE(SM):
    def __init__(self):
        self.startState=None
    def getNextValues(self, state, inp):
        if inp[0]=='undefined' or inp[1]=='undefined':
            return ('undefined','undefined')
        else:
            return (state,bool.__xor__(inp[0],inp[1]))
    def __str__(self):
        return "XOR-Gate"


class SR_Flipflop(SM):
    def __init__(self,startState,enable_bit):
        self.startState=startState
        self.enable_bit=enable_bit
    def TurnIt_ON(self):
        self.enable_bit=True
    def TurnIt_OFF(self):
        self.enable_bit=False
    def getNextValues(self,state,inp):
        if inp[0]=='undefined' or inp[1]=='undefined':
            return ('undefined','undefined')
        else:
            S=inp[0]
            R=inp[1]
            if self.enable_bit is True:
                if (S is False) and (R is False):
                    return (state,state[0])
                elif (S is True) and (R is False):
                    return ((True,False),True)
                elif (S is False) and (R is True):
                    return ((False,True),False)
                else:
                    self.Reset()
            else:
                return (state,state[0])
    def __str__(self):
        return "SR-FlipFlop"
    def Reset(self):
        self.state=(False,True)


class JK_Flipflop(SM):
    def __init__(self,startState,enable_bit):
        self.startState=startState
        self.enable_bit=enable_bit
    def TurnIt_ON(self):
        self.enable_bit=True
    def TurnIt_OFF(self):
        self.enable_bit=False
    def getNextValues(self,state,inp):
        if inp[0]=='undefined' or inp[1]=='undefined':
            return ('undefined','undefined')
        else:
            J=inp[0]
            K=inp[1]
            if self.enable_bit is True:
                if (J is False) and (K is False):
                    return (state,state[0])
                elif (J is True) and (K is False):
                    return ((True,False),True)
                elif (J is False) and (K is True):
                    return ((False,True),False)
                else:
                    return ((not(state[0]),not(state[1])),not(state[0]))
            else:
                return (state,state[0])
    def __str__(self):
        return "JK-Flipflop"
    def Reset(self):
        self.state=(False,True)


class D_Flipflop(SM):
    def __init__(self,startState,enable_bit):
        self.startState=startState
        self.enable_bit=enable_bit
    def TurnIt_ON(self):
        self.enable_bit=True
    def TurnIt_OFF(self):
        self.enable_bit=False
    def getNextValues(self,state,inp):
        if inp=='undefined':
            return ('undefined','undefined')
        else:
            D=inp
            if self.enable_bit is True:
                if D is True:
                    o=True
                else:
                    o=False
                return ((o,not(o)),o)
            else:
                return (state,state[0])
    def __str__(self):
        return "D-Flipflop"
    def Reset(self):
        self.state=(False,True)


class T_Flipflop(SM):
    def __init__(self,startState,enable_bit):
        self.startState=startState
        self.enable_bit=enable_bit
    def TurnIt_ON(self):
        self.enable_bit=True
    def TurnIt_OFF(self):
        self.enable_bit=False
    def getNextValues(self,state,inp):
        if inp=='undefined':
            return ('undefined','undefined')
        else:
            toggle=inp
            if self.enable_bit is True:
                if toggle is True:
                    o=not(state[0])
                else:
                    o=state[0]
                return ((o,not(o)),o)
            else:
                return (state,state[0])
    def Reset(self):
        self.state=(False,True)
    def __str__(self):
        return "T FlipFlop"


class TriState_Buffer(SM):
    def __init__(self,enable_bit):
        self.startState=None
        self.enable_bit=enable_bit
    def getNextValues(self,state,inp):
        if inp=='undefined':
            return ('undefined','undefined')
        else:
            if self.enable_bit is True:
                return (state,inp)
            else:
                return (state,'undefined')
    def __str__(self):
        return "Tristate-Buffer"
    def TurnIt_ON(self):
        self.enable_bit=True
    def TurnIt_OFF(self):
        self.enable_bit=False


class Parallel (SM):                      # parallel=>Single inp but different o/p
    def __init__(self, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.startState = (sm1.startState, sm2.startState)
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), (o1, o2))
    def __str__(self):
        return "single i/p differetial o/p combination of  "+ self.m1.__str__()+"  and  "+self.m2.__str__()


class Cascade(SM):
    def __init__(self, sm1, sm2):
        self.startState = (sm1.startState, sm2.startState)
        self.sm1 = sm1
        self.sm2 = sm2
    def getNextValues(self, state, inp):
        (newstate1, output1) = self.sm1.getNextValues(state[0],inp)
        (newstate2, output2) = self.sm2.getNextValues(state[1],output1)
        return ((newstate1,newstate2), output2)
    def __str__(self):
        return "Cascade combination of  "+ self.sm1.__str__()+"  and  "+self.sm2.__str__()


class Parallel2 (Parallel):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (i1, i2) = (inp[0],inp[1])
        (newS1, o1) = self.m1.getNextValues(s1, i1)
        (newS2, o2) = self.m2.getNextValues(s2, i2)
        return ((newS1, newS2), (o1, o2))
    def __str__(self):
        return "differetial i/p differetial o/p combination of  ,"+ self.m1.__str__()+"  ,  "+self.m2.__str__()


class Feedback (SM):
    def __init__(self, sm):
        self.m = sm
        self.startState = self.m.startState
    def getNextValues(self, state, inp):
        (ignore, o) = self.m.getNextValues(state,"undefined")
        (newS, ignore)=self.m.getNextValues(state, o)
        return (newS, o)


class Feedback2 (Feedback):
    def getNextValues(self, state, inp):
        (ignore, o) = self.m.getNextValues(state,(inp,"undefined"))
        (newS, ignore) = self.m.getNextValues(state, (inp, o))
        return (newS, o)
def SafeAdd(inp1,inp2):
    if inp1=='undefined' or inp2=='undefined':
        return 'undefined'
        print("Hoi")
    else:
        return inp1+inp2
def SafeSub(inp1,inp2):
    if inp1=='undefined' or inp2=='undefined':
        print("Hoi")
        return 'undefined'
    else:
        return inp1-inp2
def SafeMul(inp1,inp2):
    if inp1=='undefined' or inp2=='undefined':
        return 'undefined'
    else:
        return inp1*inp2


class Adder(SM):
    def __init__(self):
        self.startState=None
    def getNextValues(self, state, inp):
        (i1, i2) =(inp[0],inp[1])
        return (None,SafeAdd(i1, i2))


class Sub(SM):
    def __init__(self):
        self.startState=None
    def getNextValues(self, state, inp):
        (i1, i2) =(inp[0],inp[1])
        return (None,SafeSub(i1, i2))


class Multiplier(SM):
    def __init__(self):
        self.startState=None
    def getNextValues(self, state, inp):
        (i1, i2) =(inp[0],inp[1])
        return (None,SafeMul(i1, i2))


class FeedbackAdd(SM):
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        self.startState=(self.m1.startState,self.m2.startState)
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (ignore, o1) = self.m1.getNextValues(s1,0)
        (ignore, o2) = self.m2.getNextValues(s2, o1)
        (newS1, output) = self.m1.getNextValues(s1, SafeAdd(inp, o2))
        (newS2, o2) = self.m2.getNextValues(s2, output)
        return ((newS1, newS2), output)


class FeedbackSub(SM):
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        self.startState=(self.m1.startState,self.m2.startState)
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (ignore, o1) = self.m1.getNextValues(s1,0)
        (ignore, o2) = self.m2.getNextValues(s2, o1)
        (newS1, output) = self.m1.getNextValues(s1, SafeSub(inp, o2))
        (newS2, o2) = self.m2.getNextValues(s2, output)
        return ((newS1, newS2), output)


class Wire(SM):
    def __init__(self,):
        self.startState=1
    def getNextValues(self,state,inp):
        if inp=='undefined':
            return ('undefined','undefined')
        else:
            return inp,inp
    def __str__(self):
        return "Wire"
def Plotter(A0, A1):
    fig = plt.figure()
    ax_1 = fig.add_subplot(211)
    ax_2 = fig.add_subplot(212)
    a=ax_1.stem(np.arange(len(A0)), A0)
    b=ax_2.stem(np.arange(len(A1)), A1)
    return a,b
def Differentiator_Back(T):
    Differentiator_Back=Cascade(Parallel(Gain(1*(1/T)),Cascade(Gain(-1*(1/T)),Delay(0))),Adder())
    return Differentiator_Back
def Integrator_Back(T):
    Integrator_Back = Cascade(Gain(T), FeedbackAdd(Wire(), Delay(0)))
    return Integrator_Back
def Integrator_Forward(T):
    Integrator_Forward = Cascade(Gain(T), FeedbackAdd(Delay(0), Wire()))
    return Integrator_Forward
short_unit_impulse=[1,0,0,0,0,0,0]
while len(short_unit_impulse)<50:
    short_unit_impulse.append(0)
unit_impulse=short_unit_impulse
short_unit_impulse=list([1])
while len(short_unit_impulse)<150:
    short_unit_impulse.append(1)
unit_step=short_unit_impulse
gain=8
delta=.1
frst=Cascade(Gain(3),Gain(2))
# print(Cascade(frst,Gain(2)).transduce([1,0,0,0,0]))




#This is an example showing how to stimulate state machines


# input = [1, 2, 3, 4, 5]
# print("Input values")
# print(input)
# print("\n")
# machine = Cascade(Gain(3), Gain(4))
# output = machine.transduce(input)
# print("Output values")
# print(output)
