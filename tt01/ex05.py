"""Asyncio"""
from asyncio import coroutine, get_event_loop
from random import randint


@coroutine
def my_coroutine():
    print(f'Random: {randint(1,10)}')


print(type(my_coroutine))
print(type(my_coroutine()))

loop = get_event_loop()
loop.run_until_complete(my_coroutine())