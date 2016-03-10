"""Understanding the basics of process from the linux kernel point of view. And it's difference from
a thread. Linux does treat threads and processes differently, but as a user, those are details that
can be ignored. This module is about learning the support that python has for interprocess
communication for a multiprocessing application.
"""
import multiprocessing

class MyFancyClass(object):
    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print 'Doing something fancy in %s for %s!' %(proc_name, self.name)


def worker(q):
    obj = q.get()
    obj.do_something()

if __name__ == '__main__':
    # Create a multiprocessing queue, let's review what queue is, queue is an abstract
    # data structure that is used to stored data, it's open on both sides, allowing element
    # entering on one side, which is called queueing, and exiting on the other side, which
    # is called dequeueing. An intuitive understanding for a multiprocessing queue could be
    # that it's stored in a shared memory area which promises accesses from different processes
    # and should act the same way as a regular queue does.
    queue = multiprocessing.Queue()

    # Create another process with the multiprocessing module. This API class allows the creation
    # of processes that apprears to the user lives in paralism of the main process. It provides
    # interfaces such as kick off the process, and a whole set of operations for a process. The
    # protocol for creating this process, it to provide it an entry point, which is the function
    # entity to run in this subprocess, and the arguments for this function. As we want
    # communication between different processes, we provide this process an argument that is
    # a multiprocess queue, allowing us to access information about this process from another
    # process.
    p = multiprocessing.Process(target=worker ,args=(queue, ))
    # start this process
    p.start()

    # Put something in the shared queue from the main process. The function that runs in the
    # other process needs resource from the queue to operate on. And in this case, it's python
    # objects that's being passing around directly. It's very cool, we can try out the pickled
    # objects option later.
    queue.put(MyFancyClass('Fancy Dan'))

    queue.close()
    queue.join_thread()
    # This is a set of concepts that closely relates to the successful running of multiprocesses.
    # For a thread or subprocess, joining is a very critical idea and I had problem understanding
    # it before. By default, subprocess, upon being spawned or started, is completely running in
    # parallel from user's point of view. When you finish your work in the main process and it ends,
    # python would interrupt whatever status those subprocess has and terminate it and the whole
    # program ends. That is not preferable for things you want to keep running no matter what
    # happened in the main process. But since it's not really possible to predict running time of
    # any subprocess, one option is to set a subprocess as a daemon process where its running status
    # is non related to the exiting of main process, such process ends when it ends, thus the
    # lifespan of the whole application also follows. The other option is to join a thread which
    # ensures that a subprocess is finished but sacrificed parallism because it blockes the main
    # process indefinitely before this waiting proceedure comes to a conclusion. However, you can
    # pass a timeout argument to join to adjust the maximum wait time. These are two
    # options to ensure the completence of a subprocess, but they surely have their respective use
    # cases to best fit in, make your own judgement.
    p.join()

