import math as mm
import mymodule

def pow(a, b):
    return mm.pow(a, b)

# 导入自己的模块
def my_pow(a, b):
    return mymodule.my_pow(a, b)


print(pow(1, 2))