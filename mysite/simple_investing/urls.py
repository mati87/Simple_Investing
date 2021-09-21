from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'simple_investing'

urlpatterns = [
    path('', TemplateView.as_view(template_name='simple_investing/main.html')),
    path('concepts/', TemplateView.as_view(template_name='simple_investing/concepts.html')),
    path('create_comp/', views.create_comp, name='create_company'),
    path('companies_list/', views.companies_list, name='companies_list'),
    path('details/<int:pk>/', views.detail_comp, name='company_details'),
    path('update_comp/<int:pk>/', views.update_company, name='update_company'),
    path('delete_comp/<int:pk>/', views.delete_company, name='delete_company'),
    path('register_user/', views.register_page, name='register'),
    path('api_y/<company_symbol>/', views.api_y, name= 'yahoo_api'),
    path('symbol/', views.symbol, name= 'symbol'),          

]

urlpatterns += staticfiles_urlpatterns()