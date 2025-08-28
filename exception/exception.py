def get_application_fee(change):
    # 使用 guard 条件语句来让错误处理更加的健壮
    # 1. 当程序没有达到我们预期的结果的时候我们会让它返回
    # 2. 其次使用这种可以让我们知道错误出现在什么地方
    # 3. 显示的错误流, 比如如果出现非预期的情况
    if not change:
        raise ValueError("not change")