import time as T 

def cache(func):
    cacheMemory = {}
    print(cacheMemory)
    def track(*args):
        if args in cacheMemory:
            return cacheMemory[args]
        result = func(*args)
        cacheMemory[args] = result
        return result
    return track

@cache
def sleep(time: int) -> int:
    start = int(T.time())
    T.sleep(time)
    end = int(T.time())
    return end - start 

print(sleep(2))
print(sleep(4))
print(sleep(5))
print(sleep(2))
print(sleep(4))

