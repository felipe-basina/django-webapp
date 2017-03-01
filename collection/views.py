from django.shortcuts import render
from collection.models import Thing

def index(request):
    '''
    number = 7
    coisa = "coisa..."
    return render(request, 'index.html', { 'number': number,
                                            'coisa': coisa, })
    '''
    things = Thing.objects.all()
    #things = Thing.objects.filter(name__contains="Hello")
    
    return render(request, 'index.html', { 'things': things, })