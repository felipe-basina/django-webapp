from django.shortcuts import render, redirect

from collection.forms import ThingForm
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
    
def thing_detail(request, slug):
    # Recuperar o objeto
    thing = recuperar_objeto_por_slug_param(slug)
    
    return render(request, 'things/thing_detail.html', { 'thing': thing, })
    
def edit_thing(request, slug):
    # Recuperar o objeto
    thing = recuperar_objeto_por_slug_param(slug)
    
    form_class = ThingForm
    
    # Caso o formulario seja submetido com o metodo POST
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=thing)
        
        if form.is_valid():
            form.save()
            return redirect('thing_detail', slug=thing.slug) # Redireciona
    else:
        form = form_class(instance=thing)
    
    return render(request, 'things/edit_thing.html', { 'thing': thing, 
                                                        'form': form, })
    
    
####################
# Funcoes diversas #
####################
def recuperar_objeto_por_slug_param(slug):
    return Thing.objects.get(slug=slug)