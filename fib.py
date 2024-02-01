from functools import lru_cache
import time

def timer(x = int) -> int:
    end_time_time = time.time() - x
    return end_time_time

@lru_cache
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    start_time = time.time()
    for i in range(0, 101, 1):
        print( f"Finished in {timer(start_time)} s: f({i}) -> {fib(i)}")
        