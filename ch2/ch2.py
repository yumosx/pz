codes = []
# 普通的写法
symbols = '$¢£¥€¤'
for symbol in symbols:
    codes.append(ord(symbol))

# 这种是python 中特有的
codes2 = [ord(symbol) for symbol in symbols]
code2byMap = list(map(ord, symbols))

codde3 = list(filter(lambda c : c > 127, map(ord, symbols)))

# 同时遍历2个表达式
aList = ['a', 'b', 'c']
bList = ['a1', 'b1', 'c2']
cards = [(a1, b1) for a1 in aList for b1 in bList]

# 对序列做乘法和除法
l = [1, 2, 3, 4]

# 元组拆包
a1, a2, a3 = ("a1", "a2", "a3")


# 如果是对函数参数进行拆包的话，是下面这种
def add(a, b):
    return a + b

p = (1, 2, 3)
add(*p)

# 处理函数的返回值
def rang3():
    return (1, 2, 3)

