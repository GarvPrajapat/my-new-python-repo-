
def debug(method):
    def opener(*args):
        argsInString = ", ".join(str(i) for i in args)
        print(f"calling {method.__name__} function with arguments -> {argsInString}")
        result = method(*args)
        return result
    return opener

@debug
def greeting(name: str , greeting: str = "hello "):
    print(f"{greeting} {name}")

greeting("Garv","yoo")