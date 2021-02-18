"""Simple coroutine"""

def simple_coroutine():
    print('1 - coroutine started')
    x = yield 
    print(f'2 - coroutine received x: {x}')

my_couroutine = simple_coroutine()
print(my_couroutine) # <generator object simple_coroutine at ...>

next(my_couroutine) # Start coroutine. Will stop in the yield

my_couroutine.send(10) # Send a value to generator and go to the next yield or StopIteration
