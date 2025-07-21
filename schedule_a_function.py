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


# instructor's solution:
import sched


def schedule_function2(event_time, function, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(event_time, 1, function, argument=args)
    print(f'{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}')
    s.run()


schedule_function2(time.time() + 1, print, 'Howdy!')
