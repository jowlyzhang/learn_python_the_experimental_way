"""Sucks, python thread sucks so hard!
"""
import Queue
import threading
from datetime import datetime
import time

def test_a_number(i, q):
    time.sleep(10)
    data = i * i
    results = q.get()
    results[i] = data
    q.put(results)

def main():
    start_time = datetime.now()
    q = Queue.Queue()
    results = {}
    q.put(results)
    threads = []
    for i in range(0, 5):
        t = threading.Thread(target=test_a_number, args=(i, q,))
        threads.append(t)
        t.start()
        t.join()

    results = q.get()
    print results
    end_time = datetime.now()
    print 'time spent: {}'.format(end_time - start_time)

if __name__ == '__main__':
    main()

