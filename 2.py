class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            self.index = 0
        result = self.iterable[self.index]
        self.index += 1
        return result
'''

# Пример использования
my_list = [1, 2, 3, 4, 5]
cyclic_iterator = CyclicIterator(my_list)

for _ in range(10):
    print(next(cyclic_iterator))


'''
