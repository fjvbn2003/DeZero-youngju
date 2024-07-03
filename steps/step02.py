from .step01 import Function
import numpy as np

class Square(Function):
    def forward(self, x):
        return x**2

