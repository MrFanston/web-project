from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.portfolio_list, name='portfolio_list'),
    path('create/', views.create_portfolio, name='create_portfolio'),
    path('my-portfolio/', views.my_portfolio, name='my_portfolio'),
    path('edit-portfolio/', views.edit_portfolio, name='edit_portfolio'),
    path('edit-portfolio/<int:portfolio_id>/', views.details, name='details_portfolio'),
]
