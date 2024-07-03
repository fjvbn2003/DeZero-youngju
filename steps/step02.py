from .step01 import Function
import numpy as np

class Square(Function):
    def forward(self, x):
        return x**2
    def backward(self, gy):
        x = self.input.data
        gx = 2*x*gy
        return gx

