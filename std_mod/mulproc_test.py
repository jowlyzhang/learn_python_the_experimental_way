import Queue
import multiprocessing
from datetime import datetime
import sys
import time

# Tries:
# 1. Main process takes longer, non-daemon, no join.
# Because main takes longer, even though there's no wait. subprocess run completes.
# 2. Main process takes longer, non-daemon, join
# No matter whether main process longer, it has to wait for child process before proceding. so
# subprocess completes run.
# 3 Main process takes longer, daemon, no join
# Because main takes longer, child process completes before needing to run in daemon mode
# 4 Main process takes longer, daemon, join (This combination is redundant)
# Main process wait for child process to finish, so child process completes is guaranteed. no need
# to run in daemon mode.
# 5 Main process finish first, non-daemon, no join.
# Main process finishes first, but the whole process finishes when child process also finishes, so
# it looks like by default, it's not terminated. The difference with join is that main process is
# not continued when child finishes, we can time that.
# 6 Main process finishes first, non-dameon, join
# Main process wait for child process which takes longer to run to finish before proceding
# 7 Main process finishes first, daemon, no join 
# Main process finish and exits the program, child process keep running in the backgroud in daemon
# mode.
# 8 Main process finishes first, daemon, join.
# This is redundant, because main process would wait for the child process to finish anyway, it
# won't get a chance to run in daemon mode.

def worker():
    p = multiprocessing.current_process()
    sys.stdout.flush()
    print 'Starting:', p.name, p.pid
    time.sleep(100)
    sys.stdout.flush()
    print 'Exiting:', p.name, p.pid

def test_process():
    p = multiprocessing.Process(name='non-daemon', target=worker)
    p.daemon = True
    p.start()
    time.sleep(2)

if __name__ == '__main__':
    test_process()

import multiprocessing
import time
import sys

def daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    sys.stdout.flush()
    time.sleep(2)
    print 'Exiting :', p.name, p.pid
    sys.stdout.flush()

def non_daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    sys.stdout.flush()
    print 'Exiting :', p.name, p.pid
    sys.stdout.flush()

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
