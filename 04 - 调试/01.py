def SayHello(name):
    print("I want to say hello with your,{0}".format(name))
    print("hello,{0}".format(name))
    print("Done......")

if __name__ == "__main__":
    print("*" * 20)
    name = input("Please input your name: ")
    print(SayHello(name = name))
    print("@" * 20)
