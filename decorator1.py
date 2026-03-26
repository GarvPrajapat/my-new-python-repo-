import time as T

def timer(method):
    def excuter(*args):
        start :float = T.time()
        result = method(*args)
        end :float = T.time()
        print(f"the {method.__name__} took {end - start:.2f} time to complete")
        return result
    return excuter

@timer
def runner(time:int ):
    T.sleep(time)
    print("checking...")

runner(4)