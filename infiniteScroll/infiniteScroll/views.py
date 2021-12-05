from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def home(request):
    numbers_list = range(1, 1000) #Se puede aumentar el numero de paginas sea mayor
    page = request.GET.get('page', 1)
    paginator = Paginator(numbers_list, 20)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'numbers': numbers})