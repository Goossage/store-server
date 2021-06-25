from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')

def test_context(request):
    context = {
        'title':'Store',
        'header':'Welcome',
        'username':'Anton Antano',
        'products': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2340,00'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13590,00'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2890,00'},
        ],
    }
    return render(request, 'products/test-context.html', context)