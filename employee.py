from sympy import false


class Employee:
    raise_amt = 1.05
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
# Built in decorator for the property() function in python
# to give special functionality to certain methods to make them 
# act as getter setters or deleters when we define properties in 
# a class
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
