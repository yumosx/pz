""""
python 的数据模型
1. python 的数据模型是指这些函数在操作对象的时候会去调用对应的 __func__ 方法
2. 这些 __func__ 函数最终是由解释器去调用的
3. 所以我们可以在上帝视角去为 Python 的class 构造一切
"""

class MetaProp:
    a = 1
    b = 2
    def __len__(self):
        return self.a + self.b