from events import EventListener
from .events import MyEvent


class MyListener(EventListener):
    listensFor = [
        MyEvent,
    ]

    def handle(self, event):
        print("Caught a event: {}".format(event))
