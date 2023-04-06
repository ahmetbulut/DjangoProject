from django.shortcuts import render

# Create your views here.

def blog_view(request):
    # query your data store and get the objects you need.
    books = ["Skin in the Game", "Antifragile", "Da Vinci's Code", "Blink", "Tesla"]
    return render(request, "blog_post.html", context = {"user": request.META['USER'],
                                                        "books": books})