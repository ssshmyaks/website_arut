from django.shortcuts import render

from app.forms import AddForm


def main(request):
    return render(request, 'index.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def contact(request):
    form = AddForm()
    return render(request, 'contact.html', {'form': form})
