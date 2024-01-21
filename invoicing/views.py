from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib import messages

# Create your views here.

class HomeView(View):
    """_summary_

    Args:
        View (Home): template home
    """
    template_name = 'index.html'
    invoices = Invoice.objects.select_related('customer', 'save_by').all()
    
    context = {
        'invoices': invoices
    }
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

class AddCustomerView(View):
    """_summary_

    Args:
        View (AddCustomer): add new customer
    """
    template_name = 'add_customer.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'sexe': request.POST.get('sex'),
            'age': request.POST.get('age'),
            'zip_code': request.POST.get('zip'),
            'address': request.POST.get('address'),
            'city': request.POST.get('city'),
            'save_by': request.user
        }
        
        try:
            
            created = Customer.objects.create(**data)
            if created:
                messages.success(request, 'Customer created successfully')
            else:
                messages.error(request, 'Sorry, there was an error in adding the customer')
                
        except Exception as e:
            messages.error(request, f"Sorry, our application is detected the following error {e}.")
        
        return render(request, self.template_name)