class QuadraticPolynomial:
    def __init__(self,a,b,c) -> None:
        self.a=a
        self.b=b
        self.c=c

    @classmethod
    def from_iterable(cls, iterable):
        x,y,z = iterable
        return cls(x,y,z)
    
    @classmethod
    def from_str(cls, string):
        x,y,z = string.split()
        return cls(float(x),float(y),float(z))

