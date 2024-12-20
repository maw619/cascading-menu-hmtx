from django.shortcuts import render
from .models import Llibros ,Lcapitulos, Lversiculos



def index(request):
    book = Llibros.objects.all()
    return render(request, 'index.html', {'books':book}) 

def chapter(request):
    chapter_select = request.GET.get('chapter_select') 
    book = Llibros.objects.get(l_idlibro=chapter_select) 
    v = Lversiculos.objects.raw(f"SELECT * FROM lversiculos WHERE V_IdCapitulo = {chapter_select};")
    for verse in v:
        print(verse.contenido)


    if chapter_select: 
            chapters = Lcapitulos.objects.filter(c_idlibro=chapter_select) 
    else:
         chapters = None
    context = {
        'chapters': chapters,
        'book':book.l_book
    }
    return render(request, 'partials/chapter.html', context)

def verse(request):
    verse_select = request.GET.get('verse_select')
    print(verse_select)
    if verse_select:
         verses = Lversiculos.objects.filter(v_idcapitulo=verse_select)
    else:
         verses = None
    context = {
         "verses":verses,
    }
    return render(request, "partials/verse.html", context)