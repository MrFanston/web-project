from django.shortcuts import render, redirect
from .models import Portfolio
from .forms import PortfolioForm
from django.contrib.auth.decorators import login_required


def portfolio_list(request):
    items = Portfolio.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {'items': items})


@login_required
def create_portfolio(request):
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
