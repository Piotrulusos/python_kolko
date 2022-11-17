val = 256

from random import randint

n = 1000  # Liczba elementów do wylosowania
digits_example = [randint(-1000, 1000) for _ in range(n)]

from typing import List


def f(val: int, digits: List[int]) -> bool:
    if val in digits:
        return True
        pass
    else:
        return False


pass


print(digits_example)
print(val)
print(f(val, digits_example))


