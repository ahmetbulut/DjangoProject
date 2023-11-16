from django.shortcuts import render
from library.models import Author, Book
from library.forms import AuthorForm, BookForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

# def home_form(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = AuthorForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             firstname = form.cleaned_data['firstname']
#             lastname = form.cleaned_data['lastname']
#             a = Author(firstname=firstname, lastname=lastname)
#             a.save()
#             # redirect to a new URL:
#             #return HttpResponseRedirect('/library/success')
#             return render(request, "model_saved.html",
#             {'messages': [str(a) + ' saved!'], "redirect": '/library'})
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = AuthorForm()
#
#     return render(request, 'home_form.html', {'form': form})


def home_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            title = form.cleaned_data['title']
            numpages = form.cleaned_data['numpages']
            publisher = form.cleaned_data['publisher']
            b = Book(title=title, numpages=numpages, publisher=publisher)
            b.save()
            # redirect to a new URL:
            #return HttpResponseRedirect('/library/success')
            return render(request, "model_saved.html",
                          {'messages': [str(b) + ' saved!'], "redirect": '/library'})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookForm()

    return render(request, 'home_form.html', {'form': form})
