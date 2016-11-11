from channels.routing import route

from hello import consumers


channel_routing = [
    route('notify', consumers.notify),
]
