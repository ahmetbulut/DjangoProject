from django.shortcuts import render
from library.models import Author

# Create your views here.

def home(request):
    return render(request, "home.html")

def save_author(request):
    messages = []
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        a = Author(firstname=firstname, lastname=lastname)
        a.save()
        messages.append(str(a) + ' saved!')

    return render(request, "author_saved.html", context={"messages" : messages})
