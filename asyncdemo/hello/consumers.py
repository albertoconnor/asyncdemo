import time


def delay():
    while True:
        for i in [5, 5, 5, 30]:
            yield i


delay_generator = delay()


def notify(message):
    time.sleep(next(delay_generator))
    print(message['message'])
