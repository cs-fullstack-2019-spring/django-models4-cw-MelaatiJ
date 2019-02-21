from django.contrib import admin


# Register your models here.

# files needed so it will show on my admin page.
#from models import the class mom

from .models import Mom
admin.site.register(Mom)

#from models import child class
from . models import Child
admin.site.register(Child)


