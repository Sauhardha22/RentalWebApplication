from django.contrib import admin
from . models import Admin,Vehicle,Payment,ApprovalRequest,Client
# Register your models here.

admin.site.register([Admin,Vehicle,Payment,ApprovalRequest,Client])
