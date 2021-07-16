## Digital#######
from SM import SM
class  NOT_GATE(SM): # Class to implement NOT gate with SM structure
    """
    Class to implement NOT gate with SM structure. Inherited from parent state machine"""
    def __init__(self):# There is no constructor
        self.startState=True  # This value will have no impact since NOT gate is not a sequential circuit.
    def getNextValues(self, state, inp):
        """
        Function  which provide the logic which connect the
        # Function  which provide the logic which connect the future state with present input and and present state,But here the past have no impact. for NOT gate : just negate the input value"""

        if inp=='undefined': # 'undefined 'is equilvalent to tristate in electronics,equivalent to nothing
            return ('undefined','undefined')
        else:   # just negate the input value
            return (state, not(inp))
    def __str__(self):
        return "NOT-Gate"
class  NAND_GATE(SM):
    """
    Class to implement NAND gate with SM structure. Inherited from parent state machine"""
    def __init__(self):# There is no constructor
        self.startState=None   # This value will have no impact since NAND gate is not a sequential circuit.
    def getNextValues(self, state, inp):
        """Function  which provide the logic which connect the future state with present input and and present state,But here the past have no impact. for NAND gate : just (A.B)"""

        if inp[0]=='undefined' or inp[1]=='undefined':# 'undefined 'is equilvalent to tristate in electronics,equivalent to nothing
            return ('undefined','undefined')
        else:# just apply the logic
            return (state,not(bool.__and__(inp[0],inp[1])))
    def __str__(self):
        return "NAND-Gate"
class NOR_GATE(SM):
    """ Class to implement NOR gate with SM structure. Inherited from parent state machine"""
    def __init__(self):# There is no constructor
        self.startState=None # This value will have no impact since NOR  gate is not a sequential circuit.
    def getNextValues(self, state, inp):
        """Function  which provide the logic which connect the future state with present input and and present state,But here the past have no impact. for NOR gate : just (A+B)"""

        if inp[0]=='undefined' or inp[1]=='undefined': # 'undefined 'is equilvalent to tristate in electronics,equivalen
            return ('undefined','undefined')
        else: # just apply the logic
            return (state,not(bool.__or__(inp[0],inp[1])))
    def __str__(self):
        return "NOR-Gate"
class XOR_GATE(SM):
    """
     Class to implement XOR gate with SM structure. Inherited from parent state machie"""
    def __init__(self):# There is no constructor
        self.startState=None# This value will have no impact since NOR  gate is not a sequential circuit.
    def getNextValues(self, state, inp):
        """Function  which provide the logic which connect the  future state with present input and and present state,But here the past have no impact. for NOR gate : just xor(A,B)"""

        if inp[0]=='undefined' or inp[1]=='undefined':# 'undefined 'is equilvalent to tristate in electronics,equivalent to nothing
            return ('undefined','undefined')
        else:# just apply the logic
            return (state,bool.__xor__(inp[0],inp[1]))
    def __str__(self):
        return "XOR-Gate"
