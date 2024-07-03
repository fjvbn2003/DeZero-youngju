from .step01 import Variable
from .step02 import Square
from .step03 import Exp
import numpy as np


# y = (e^(x^2))^2
A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))

a = A(x)
b = B(a)
y = C(b)
print(y.data)
# 1.648721270700128
