from django.views import generic
from .events import MyEvent

def event_caller():
    MyEvent.Dispatch("Just a sample event")

# Dispatching the event here works, because is not inside any class.
# By calling the event here, the event will display on console before System Check results
# To test it, uncomment the following line and start the server
event_caller()


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'context'

    def get_queryset(self):
        return None

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)

        # Dispatching the event here doesn't work because is inside a class method.
        # Here the event will be dispatched but not listened to.
        # To test it, uncomment the following line and navigate to http://localhost:8000
        # event_caller()

        return context
