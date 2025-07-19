from django.shortcuts import render


def index(request):
    return render(
        request,
        'blog/pages/index.html',
        {
            'nome': 'Luiz Otávio'
        }
    )


def page(request):
    return render(
        request,
        'blog/pages/page.html',
        {
            'nome': 'Luiz Otávio'
        }
    )


def post(request):
    return render(
        request,
        'blog/pages/post.html',
        {
            'nome': 'Luiz Otávio'
        }
    )