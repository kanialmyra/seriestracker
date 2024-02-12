from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Kania Almyra Bilqist',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
