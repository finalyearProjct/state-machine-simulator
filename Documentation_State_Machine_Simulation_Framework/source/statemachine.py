class SM:
    """
    Parent Machine and most of the other class inherits from this class
    """                   # Parent Machine and most of the other class inherits from this class  #
    def start(self):
        ##This is act like the constructor

        ## here the self.startState is taken form the class which inherites this super class
        self.state=self.startState
        """
        here the self.startState is taken form the class which inherites this super class
        """

        ## just initialising the input list
        self.inputlist=list([0])

    def step(self,inp): ## function responsible for exciting the machine with a SINGLE INPUT VALUE
        """
        function responsible for exciting the machine with a SINGLE INPUT VALUE

        inp : the input value

        The self.getNextValues() function is defined in the child class, which will define how the machine evolves/operates. This will return both output along with the state/status
        """
        (s, o) = self.getNextValues(self.state,inp)
        # will store the state and return the output
        self.state =s
        return o
    def transduce(self,inputs):
        """
        This function returns the output list when excited with a list of inputs. This works by repeatedly involking the step function

        inputs: list of values as input for driving the machine
        """
        self.start()
        return [self.step(inp) for inp in inputs]
    def run(self,n=10):
        """
        This function is for transducing where we dont require any input stream

        n : number of movements
        """
        return self.transduce([None] * n)
