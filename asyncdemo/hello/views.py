from django.shortcuts import render
from channels import Channel


def hello_view(request, template="hello.html"):
    name = request.GET.get('name', 'World')

    message = 'Hello, {}!'.format(name)
    Channel('notify').send(
        dict(
            message=message,
        )
    )

    return render(
        request,
        template,
        dict(message=message),
    )
