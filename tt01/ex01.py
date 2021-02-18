"""Using yield as a primitive coroutine"""
from collections import deque


def counter_up(stop):
    count = 1
    while count <= stop:
        yield count
        count += 1


def counter_down(start):
    while start >= 1:
        yield start
        start -= 1


class Scheduler:
    def __init__(self):
        self.queue = deque()

    def add_new(self, coroutine):
        self.queue.append(coroutine)

    def run(self):
        while self.queue:
            task = self.queue.popleft()
            try:
                result = next(task)
                print(f'task={task.__name__}: result={result}')

                self.queue.append(task)
            except StopIteration:
                print('Opss!')


s = Scheduler()
s.add_new(counter_up(10))
s.add_new(counter_down(15))
#s.run()