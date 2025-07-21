# Linked Learning - Python Code Challenges
# 22 Jul, 2025
# Schedule a function to run at a specific time
import datetime
import time


def schedule_function(t, fun, *args):
    now = datetime.datetime.now()

    while now < t:
        time.sleep(1)
        now = datetime.datetime.now()

    fun(*args)


def run(message):
    print(f'Running: {message}')


target_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
schedule_function(target_time, run, 'Hello, World!')

