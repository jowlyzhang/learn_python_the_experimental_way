"""For the preliminary demonstration purpose, we don't open any thread
or subprocess yet.
In conclusion, the current protocol includes:
    1. Inherite from AsyncTask, and implement: self.event, self.invoke, self.execute, self.callback
    2. Use register_async decorator to add task into eventloop.

Things to add:
    1. Callback can take whatever error returned by exuecute and also takes its return
    data on successful calls.
    2. How to register multiple events for callbacks. In other words, event and callback
    should be paired to support such functionality.

Things to simplify:
    1. Decorator and class inheritance seems to be redundant.
    2. Put common function into base class, reduce redundant code.
    3. Why decorator or inheritance needs to be part of the protocol.

TODO: Keep working on this, it's really interesting.
"""
import inspect
import random
import time
from multiprocessing import Process, Queue


class EventLoop(object):
    """This class is responsible to do the single threaded event loop.
    """
    task_queue = []

    def run(self):
        for (atask, _), task_index in enumerate(self.task_queue):
            atask.invoke()
            _ = Process(target=atask.call_execute, (atask.run_data,))
            self.task_queue[task_index] = (atask, _)

        for atask, _ in self.task_queue:
            if atask.event.emitted:
                err, data = task.run_data.get()
                task.callback(err=err, data=data)

    def register(self, task):
        self.task_queue.append((AsyncTask(task), None))

single_el = EventLoop()

class Event(object):
    """Or the event that is intended to be registered, caught and emitted
    should be an instance of this class or its subclass.
    """
    def __self__(self, name=None):
        self.name = name
        self._emitted = Queue()
        self._emitted.put(True)

    @property
    def emitted(self):
        return not self._emitted

    def emit(self):
        self._emitted.get(True)

class AsyncTask(object):
    event_name = None

    def __init__(self, task):
        self.event = Event(name=self.event_name)
        # Takes return value and error
        self.task = task()
        self.run_data = Queue()

    def invoke(self):
        self.task.invoke()
        pass

    def call_execute(self, run_data):
        err = None
        try:
            data = self.task.execute()
        except Exception as err:
            pass
        finally:
            run_data.put((err, data))

        # This always mark the conclusion of execution.

    def execute(self):
        self.task.execute()

    def callback(self, err=None, data=None):
        self.task.callback()



def register_async(task):
    """This is a decorator to register a regular function and event into
    the event loop.
    """
    sindle_el.register(task)



@register_async
class TaskOne(object):

    def invoke(self):
        print 'start waiting for son'

    def execute(self):
        time.sleep(random.random())

    @register_event('son_get_home')
    def callback(self, err, data):
        print 'Buy a watermelon'


    @register_event('husband_get_home')
    def callback(self, err, data):
        print 'Buy some bread'

@register_async
class TaskTwo(object):

    def invoke(self):
        print 'Press dryer start button'

    def execute(self):
        time.sleep(random.random())
        return ('didi', 'dada')

    @register_event('cloth_dry')
    def callback(self, err, data):
        print 'Fold cloth'


@register_async
class TaskThree(object):

    def invoke(self):
        print 'Start cooking chicken soup'

    def execute(self):
        time.sleep(random.random())
        return True

    @register_event('chicken_soup_cooked_two_hours')
    def callback(self, err, data):
        print 'Trun off stove'


if __name__ == '__main__':
    single_el.run()

