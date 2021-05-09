from django.shortcuts import render


def index(request):
  my_dict = {'testKey': 'Hello. This seems to work dude.'}
  return render(request, 'myauto/index.html', context=my_dict)

# Create your views here.
