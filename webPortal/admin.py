from django.contrib import admin
from .models import Quotation
from .models import UserQuote
# Register your models here.
admin.site.register(Quotation)
admin.site.register(UserQuote)