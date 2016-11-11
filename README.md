Async Task Channels Demo
========================

The demo goes with the talk [Async Tasks with Django
Channels](http://albertoconnor.ca/pycon-canada-2016-talk.html) given
at [PyCon Canada 2016](https://2016.pycon.ca/en/schedule/016-albert-oconnor/)

It is split up into a few different step with tags so you can more
easily see how it was built up.

step1
-----

    git clone https://github.com/albertoconnor/asyncdemo.git
    cd asyncdemo
    git checkout step1

At this point, the code is for a basic Django 1.10 web app. Get into your
favorite type of virtual env and then run the following.

    pip install -r requirements.text
    cd asyncdemo
    python manage.py migrate
    python manage.py runserver

Now you should have the hello_view being served at
http://127.0.0.1:8000/. You can append "?name=yourname" to change the
name displayed.

Meanwhile, there is a simulated slow network call which writes out the
hello message to the console and takes between 5 and 30 seconds to
do it.

step2
-----

    git checkout step2
    python manage.py runserver


This has updated requirements.txt and settings.py and created a
routes.py which is even to get Django to run with Channels. The view
remains unchanged, so it will still be slow when you runserver. You can
see though the output Django produces when you runserver has been
changed.

step 3
------

    git checkout step3
    python manage.py runserver



A "notify" channel has been declared and the view now uses it. When you
runserver the website is more responsive, but if you hammer it those
slow 30 second simulated network calls will gum up the system.

bonusround
----------

    git checkout bonusround

This changes channels to use redis as the broker of messages. Even to
runserver you will need to have redis running locally.

When you do you will get the same behavior of step 3. To get around the
slow down under load we will need to run everything in separate
processes, in separate terminals.

    daphne asyncdemo.asgi:channel_layer --port 8000

This runs the interface server in it's own process. If you try to
connect now it will time out because there are no workers running.

You can run workers in as many separate terminals as you like:

    python manage.py runworker

But the key to trying to maintain throughput is to run a worker which
will never be tied up with a notification task:

    python manage.py runworker --exclude-channels=notify

This worker will ensure that hello_view remains responsive.
