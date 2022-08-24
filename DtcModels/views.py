from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm

# def news_feeds(request):
#     # if this is a POST request we need to process the form data
#     photo = Photo.objects.all()
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#         context = {'photo' : photo }
#     # return render(request, 'formstemplateko.html', {'form': form})
#     render(request, 'accounts/newsfeeds.html', context)

def home(request, pk='POGI!'):
    return render (request=request, template_name="formstemplateko.html", context={"pk":pk})