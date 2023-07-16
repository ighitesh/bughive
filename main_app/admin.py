from django.contrib import admin
from .models import Bug_Query
from .models import Bug_Solution
from .models import Bug_Priority
from .models import Bug_Status

# Register your models here.
admin.site.register(Bug_Query)
admin.site.register(Bug_Solution)
admin.site.register(Bug_Priority)
admin.site.register(Bug_Status)