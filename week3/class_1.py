class ComplexNumber:
    '''This class is customized to complex numbers'''

    def __init__(self,real,imag):
        '''This is the initializer'''
        self.real = real
        self.imag = imag 
    
    def __doc__():
        '''This gives the document string'''
        statement= 'This class is customized to complex numbers'
        return statement
    
    
    def __str__(self):
        x=str(self.real)+ '+'+str(self.imag)+'j'
        return x + '--> Complex number'
 
    def __repr__(self):
        ''' This method defines the string to be returned'''
        x=str(self.real)+ '+'+str(self.imag)+'j'        
        return x

    def __add__(self_1,self_2):
        real = self_1.real +self_2.real
        imag = self_1.imag +self_2.imag
        return ComplexNumber(real,imag)