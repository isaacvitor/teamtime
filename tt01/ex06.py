"""Asyncio"""
from asyncio import (
    coroutine, get_event_loop, gather
)
from random import randint


@coroutine
def subgenerator():
    return randint(1, 50)


@coroutine
def my_coroutine():
    val1 = yield from subgenerator()
    val2 = yield from subgenerator()
    return val1 + val2


loop = get_event_loop()
group = gather(my_coroutine(), my_coroutine(), my_coroutine())
result = loop.run_until_complete(group)
print(result)