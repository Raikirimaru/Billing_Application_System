from django.contrib import admin
from .models import *

class AdminCustomer(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'sexe', 'age', 'city', 'zip_code')
    
class AdminInvoice(admin.ModelAdmin):
    list_display = ('customer', 'save_by', 'incoice_date_time', 'total', 'last_update_at', 'paid', 'invoice_type')
    
admin.site.register (Customer, AdminCustomer)
admin.site.register (Invoice, AdminInvoice)
admin.site.register (Article)