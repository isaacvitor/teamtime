"""Average"""
def average():
    total = 0.0
    count = 0
    avg = None
    while True:
        in_value = yield avg
        total += in_value
        count += 1
        avg = total/count


my_couroutine = average()
result = next(my_couroutine)  # "prime"
print(f'Coroutine result: {result}')

result = my_couroutine.send(10)  # 10.0
print(f'Coroutine result: {result}')

result = my_couroutine.send(20)  # 15.0
print(f'Coroutine result: {result}')