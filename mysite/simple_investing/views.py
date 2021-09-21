from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CompanyForm, UserForm, UserLogin,CompanySymbol
from django.views import View
from .models import Company
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import requests, json

def create_comp(request):      
    form = CompanyForm()
    if request.method == 'POST':
        print(request.POST)
        form = CompanyForm(request.POST)  
        user = request.user      
        if form.is_valid():                       
            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/companies_list/')           
    else:          
        context = {'form': form}    
        return render(request, 'simple_investing/create_company.html', context)    

def companies_list(request):
    companies = Company.objects.all()
    context = {'companies' : companies} 
    return render(request, 'simple_investing/companies_list.html',context)

def detail_comp(request, pk):    
    company_obj = Company.objects.get(id=pk)
    context = {'company' : company_obj} 
    return render(request, 'simple_investing/detail.html',context)


def update_company(request,pk):
    company_obj = Company.objects.get(id=pk)
    form = CompanyForm(instance=company_obj)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/companies_list/')
    else:
        context = {'form' : form}
        return render(request, 'simple_investing/create_company.html',context)

def delete_company(request,pk):
    company_obj = Company.objects.get(id=pk)    
    if request.method == 'POST':
        company_obj.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000/companies_list/')
    
    else:
        context = {'company' : company_obj}
        return render(request, 'simple_investing/delete_company.html',context)    

def register_page(request):
    form = UserForm
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()            
            return HttpResponseRedirect('http://127.0.0.1:8000/login/')    
    else:
        context = {'form' : form}
        return render(request,'simple_investing/register.html', context)

def api_y(request, company_symbol):    
    url = "https://rest.yahoofinanceapi.com/v6/finance/quote"
    querystring = {"symbols":"{},BTC-USD,EURUSD=X".format(company_symbol)}
    headers = {
    'x-api-key': "duF5YZeWnp1qO62u9g5AI8t6RUjLXTCc4JwDClLx"    
    }
    response = requests.request("GET", url, headers=headers, params=querystring)    
    dic_json = json.loads(response.text) #create a json dictionary in order to grab values
    company = dic_json['quoteResponse']['result'][0] #enter the data of the company by indexing 
    is_company= True
    if 'displayName' not in company: #check to see if there was a retrieval of the company.
        is_company= False            #if false, print a message to re enter the ticket symbol.
    
    context = {'company' : company, 'is_company' : is_company}
    return render(request,'simple_investing/yahoo_api.html', context )

def symbol(request):
    form = CompanySymbol
    if request.method == 'POST':
        form = CompanySymbol(request.POST)
        print(request.POST)
        if form.is_valid():
            company_symbol = form.cleaned_data['company_symbol']
            return HttpResponseRedirect('http://127.0.0.1:8000/api_y/'+company_symbol+'/')
    else:
        context = {'form' : form}
        return render(request,'simple_investing/symbol.html',context )



