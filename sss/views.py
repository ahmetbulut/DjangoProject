from django.shortcuts import render
from sss.forms import CustomerForm
from sss.models import Customer

def create_customer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            c = Customer(name=name)
            # data saved to the DB
            c.save()
            messages = []
            messages.append(c.name + ' saved!')
            # redirect to a confirmation page if successful
            return render(request, "model_saved.html",
                          {"messages": messages, 'redirect': '/sss'})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomerForm()

    return render(request, 'sss_create_customer.html', {'form': form, 'redirect': '/sss'})

def home(request):
    return render(request, "sss_home.html")

def get_customer(request):
    if request.GET:
        customers = Customer.objects.filter(name=request.GET['name_filter'])
        return render(request, "sss_search_customer.html",
                  context={
                      "user": request.META['USER'],
                      "customers": customers}
                  )
    else:
        return render(request, "sss_search_customer.html")