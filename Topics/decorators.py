def smart_div_dec(original_fun):
    def smart_div(a,b):
        if a<b:
            a,b=b,a
        return original_fun(a,b)
    return smart_div

@smart_div_dec
def div(a,b):
    print (a/b)

print(div(2,4))


class smart_div_dec_class():
    def __init__(self,original_func):
        self.original_func = original_func
    def __call__(self, a,b):
        if a<b :
            a,b =b,a
        return self.original_func(a,b)

@smart_div_dec_class
def div(a,b):
    print (a/b)

print(div(2,4))