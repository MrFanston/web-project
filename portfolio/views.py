from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Portfolio
from .forms import PortfolioForm
from django.contrib.auth.decorators import login_required


def portfolio_list(request):
    items = Portfolio.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {'items': items})


@login_required
def create_portfolio(request):
    existing_portfolio = Portfolio.objects.filter(user=request.user).exists()
    if existing_portfolio:
        return HttpResponse("Вы уже создали портфолио.")
    
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('portfolio_list')  # Поменяйте на соответствующий URL
    else:
        form = PortfolioForm()
    
    return render(request, 'portfolio/create_portfolio.html', {'form': form})

def my_portfolio(request: HttpRequest):
    portfolio = Portfolio.objects.first()
    return render(request, 'portfolio/my_portfolio.html', {'portfolio': portfolio})

@login_required
def edit_portfolio(request):
    portfolio = Portfolio.objects.filter(user=request.user).first()

    if not portfolio:
        return HttpResponse("У вас нет доступа к этому портфолио или оно не существует.")

    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('my_portfolio')
    else:
        form = PortfolioForm(instance=portfolio)
    
    return render(request, 'portfolio/edit_portfolio.html', {'form': form})

def details(request: HttpRequest, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)

    return render(request, 'portfolio/details.html', {'portfolio': portfolio})