from events import Event


class MyEvent(Event):
    def __init__(self, string):
        self.string = string
        print("MyEvent Initialized")