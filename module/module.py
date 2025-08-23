import math as mm
import mymodule
from my import add

def pow(a, b):
    return mm.pow(a, b)

# 导入自己的模块
def my_pow(a, b):
    return mymodule.my_pow(a, b)

def other_module():
    return add.Add(1, 2)


print(pow(1, 2))