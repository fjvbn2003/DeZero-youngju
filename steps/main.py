from .step01 import Variable
from .step02 import Square
from .step03 import Exp
from .step04 import numerical_diff
import numpy as np


if __name__ == "__main__":

    # BackPropagation
    A = Square()
    B = Exp()
    C = Square()

    x = Variable(np.array(0.5))
    a = A(x)
    b = B(a)
    y = C(b)

    y.grad = np.array(1.0)
    b.grad = C.backward(y.grad)
    a.grad = B.backward(b.grad)
    x.grad = A.backward(a.grad)
    print(x.grad) # 3.297442541400256


    # # differential of composite function
    # def f(x):
    #     A = Square()
    #     B = Exp()
    #     C = Square()
    #     return (C(B(A(x))))
    
    # x = Variable(np.array(0.5))
    # dy = numerical_diff(f,x)
    # print("differential of composite function", dy)



    # f = Square()
    # x = Variable(np.array(2.0))
    # dy = numerical_diff(f,x)
    # print("Differential of Square function ",dy)


    # A = Square()
    # B = Exp()
    # C = Square()

    # x = Variable(np.array(0.5))

    # a = A(x)
    # b = B(a)
    # y = C(b)
    # print(y.data)
    # # y = (e^(x^2))^2
    # # 1.648721270700128
