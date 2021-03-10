import os
import time

num_threads = 1

while (1):
    os.system("py job_manager.py %s" % num_threads)
    time.sleep(4)
