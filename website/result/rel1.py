try:
    from website.calculation import add, sub
except Exception as e:
    print(e)

def add_result(x,y):
    # print('add result ::')
    a = add(x,y)
    # print(a)
    return a
    

def sub_result(x,y):
    print('sub_result ::')
    b = sub(x,y)
    return b