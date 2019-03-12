'''
This python file contains all functions and classes I come up with as I read Linear Algebra 
Done Right complete with in-depth annotations for the meaning of each function as I understand it.
I hope that this helps deepen my understanding of linear algebra and that it can be used by others
to help in their understanding as well.
'''
class InputError(Exception):
    def __init__(self):
        super().__init__("Check that your inputs are of the expected types")

class Complex():
    '''
    i is the square root of -1, by using it we can define the class of complex numbers,
    which are written as a + bi, a being the real part, and b being the complex part.
    By defining multiplication and addition as follows, they enjoy the same properties
    as the Real numbers.
    '''
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary
    
    def __str__(self):
        return f"{self.real} {'+-'[self.imaginary<0]} {abs(self.imaginary)}i"
    
    def __mul__(self, b):
        real_part = self.real * b.real - self.imaginary * b.imaginary
        imaginary_part = self.real * b.imaginary + self.imaginary * b.real
        return Complex(real_part, imaginary_part)

    def __add__(self, b):
        real_part = self.real + b.real
        imaginary_part = self.imaginary + b.imaginary
        return Complex(real_part, imaginary_part)

    def __sub__(self, b):
        real_part = self.real - b.real
        imaginary_part = self.imaginary - b.imaginary
        return Complex(real_part, imaginary_part)
    
class Vector():
    '''
    Vectors are collections of elements in which, unlike sets, order and repetitions matter.
    Their addition and multiplications are defined when both vectors are of the same size,
    and are performed mostly element-wise.
    '''
    def __init__(self, elements):
        self.elements = elements
        self.size = len(elements)
    
    def __str__(self):
        elmts = ""
        for x in self.elements:
            elmts += str(x) + " "
        return "[" + elmts[0:-1] + "]"
    
    def __mul__(self, scalar):
        '''implements scalar multiplication of a vector'''
        res = [a*scalar for a in self.elements]
        return Vector(res)

    def __add__(self, vector):
        if not (type(self) == Vector and type(vector) == Vector):
            raise InputError
        res = [self.elements[x] + vector.elements[x] for x in range(len(self.elements))]
        return Vector(res)

    def __sub__(self, vector):
        if not (type(self) == Vector and type(vector) == Vector):
            raise InputError
        res = [self.elements[x] - vector.elements[x] for x in range(len(self.elements))]
        return Vector(res)    

    
    __rmul__ = __mul__

    

if __name__ == "__main__":
    v = Vector([1,2,3])
    print(v)
    print(v * 4)
    print(12 * v)
    print(Vector([4,5,6]) + v)
    print(v-v, 2*v-v-3*v)