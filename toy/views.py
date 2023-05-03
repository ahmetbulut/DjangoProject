from django.shortcuts import render
from django.http import HttpResponse
import datetime


# a request to display the current time on a web page
def current_datetime(request):
    now = datetime.datetime.now()

    response = """ 
    <html>
     <title>The current time</title>
     <body>
     <h1> It's %s. </h1>  
     </body>  
    </html>
    """

    response = response % (now,)

    return HttpResponse(response)


def carousel_view(request):
    return render(request, "carousel.html")

# demonstration of the contents of request objects
def display_request(request):
    for key in request.META:
        if key in ['SERVER_PROTOCOL', 'USER', 'PATH_INFO', 'QUERY_STRING', 'HTTP_USER_AGENT']:
            print(key, request.META[key])

        # if 'Chrome' in request.META['HTTP_USER_AGENT']:
        #     do X
        # elif 'Safari' in request.META['HTTP_USER_AGENT']:
        #     do Y
        # ...

    response = "Cooking ..."
    return HttpResponse(response)
