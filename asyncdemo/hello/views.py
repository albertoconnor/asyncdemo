import time
from django.shortcuts import render


def delay():
    while True:
        for i in [5, 5, 5, 30]:  # Simulate unreliability
            yield i


delay_generator = delay()


def send_notification(message):
    time.sleep(next(delay_generator))
    print(message)  # Simulate sending to slack etc.


def hello_view(request, template="hello.html"):
    name = request.GET.get('name', 'World')
    message = 'Hello, {}!'.format(name)

    send_notification(message)

    return render(
        request,
        template,
        dict(message=message),
    )
