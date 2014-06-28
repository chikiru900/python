__author__ = 'TOANTV'
import math


class Solver:
    def demo(self, a, b, c):
        d = b * b - 4 * a * c
        if d > 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            print (root1, root2)
        else:
            raise Exception

    def demo_sum(self, a, b, c):
        try:
            sum_number = a + b + c
            return sum_number
        except:
            return 'Arg is not number'

    def IsOdd(self, n):
        return n % 2 == 1
