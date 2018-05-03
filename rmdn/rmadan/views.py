from django.shortcuts import render, redirect


# Create your views here.
def UserPage(request, name):
    contect = {'name': name}
    return render(request, 'name.html', contect)


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        url = '/'+name
        return redirect(url)
    else:
        return render(request, 'index.html')
