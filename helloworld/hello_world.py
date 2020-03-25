class HelloWorld(object):
    """ Hello world class """

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return "Hello " + self.name + "!!"
