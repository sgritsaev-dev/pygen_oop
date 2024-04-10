from math import sqrt
class QuadraticPolynomial:
    def __init__(self,a,b,c) -> None:
        self.a=a
        self.b=b
        self.c=c
    
    @property
    def x1(self):
        if not ((self.b**2 - (4*self.a*self.c))<0):
            return ((-self.b)-(sqrt((self.b**2) - (4*self.a*self.c))))/(2*self.a)
        return None
    @property
    def x2(self):
        if not ((self.b**2 - (4*self.a*self.c))<0):
            return ((-self.b)+(sqrt((self.b**2) - (4*self.a*self.c))))/(2*self.a)
        return None
    @property
    def view(self):
        return f'''{self.a}x^2 {'+' if self.b>=0 else '-'} {abs(self.b)}x {'+' if self.c>=0 else '-'} {abs(self.c)}'''
    @property
    def coefficients(self):
        return self.a, self.b, self.c
    @coefficients.setter
    def coefficients(self, coeffs):
        self.a, self.b, self.c = coeffs

polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)