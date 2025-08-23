### 如果说一个类型中实现了对应的 hash 方法和eq 方法
from collections import abc

my_dict = {}
isinstance(my_dict, abc.Mapping)
