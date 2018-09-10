from django.contrib import admin
from .models import Quotation
from .models import UserQuote, Approver, userRole
# Register your models here.
admin.site.register(Quotation)
admin.site.register(UserQuote)
admin.site.register(Approver)
admin.site.register(userRole)