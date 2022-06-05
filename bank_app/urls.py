from django.contrib import admin
from django.urls import path
from . import views

app_name = 'bank_app'


urlpatterns = [
   path('', views.index, name='index'),
   path('home/', views.home, name='home'),
   path('accounts/', views.accounts, name='accounts'),
   path('transfer/', views.transfer, name='transfer'),
   path('loans/', views.loans, name='loans'),
   path('loan_details/', views.loan_details, name='loan_details'),
   path('loan_details/<int:id>/', views.loan_details, name='loan_details'),
   path('profile/', views.profile, name='profile'),
   path('staff/', views.staff, name='staff'),
   path('staffAccountView/', views.staffAccountView, name='staffAccountView'),
   path('staffCustomerView/', views.staffCustomerView, name='staffCustomerView'),
   path('staff_customer_details/<int:id>', views.staff_customer_details, name='staff_customer_details'),
   path('staffNewCustomer', views.staffNewCustomer, name='staffNewCustomer'),
   path('staffNewAccount', views.staffNewAccount, name='staffNewAccount'),
   path('staffTransfers', views.staffTransfers, name='staffTransfers'),
   ]
