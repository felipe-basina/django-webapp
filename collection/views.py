from django.shortcuts import render

def index(request):
    number = 7
    coisa = "coisa..."
    return render(request, 'index.html', { 'number': number,
                                            'coisa': coisa, })