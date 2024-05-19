from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
    return render(request, 'search_image/index.html')
