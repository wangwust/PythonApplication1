from HelloWorld import HelloWorld

class Main(object):
    if __name__ == "__main__":
        h = HelloWorld()
        name = raw_input("Please enter your name:")
        h.hello(name)


