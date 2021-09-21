from django.db import models
from django.contrib.auth.models import User
import decimal
from decimal import Decimal

# Create your models here.

class Company(models.Model):
    #Link to User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    #Company data    
    company_name = models.CharField(max_length=100)
    outstanding_shares = models.IntegerField()
    share_price = models.DecimalField(max_digits= 5, decimal_places=2)
    revenue = models.IntegerField()
    expenses = models.IntegerField()
    total_assets = models.IntegerField()
    total_liabilities = models.IntegerField()
    current_assets = models.IntegerField()
    current_liabilities = models.IntegerField()
    operating_cashflows = models.IntegerField()
    capex = models.IntegerField()    
    
    #Date of creation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)    
        
    def __str__(self):
        return self.company_name

    #Company methods        
    def net_income(self):        
        return self.revenue - self.expenses

    def net_assets(self):
        return self.total_assets - self.total_liabilities

    def price_to_earnings(self):
        try:
            return round(self.net_income() / self.outstanding_shares, 2)
        except:
            return 0
    def return_on_equity(self):
        try:
            return round(self.net_income() / self.net_assets(), 2) 
        except:
            return 0
    def debt_to_equity(self):
        try:
            return round(self.total_liabilities / self.net_assets(), 2)
        except:
            return 0
    def current_ratio(self):
        try:
            return self.current_assets / self.current_liabilities
        except:
            return 0
    def free_cashflow(self):
        return self.operating_cashflows - self.capex # net cash from operating activities - capex

    def market_cap(self):
        return self.share_price * self.outstanding_shares 

    def price_to_sales(self):
        try:
            return round(self.market_cap() / self.revenue , 2)
        except:
            return 0
    def book_value_per_share(self):
        try:
            result = decimal.Decimal(self.net_assets() / self.outstanding_shares)
            return result.quantize(Decimal('0.01'))
        except:
            return 0                            

    def price_to_book(self):
        try:
            return round(self.share_price / self.book_value_per_share(),2)
        except:
            return 0    