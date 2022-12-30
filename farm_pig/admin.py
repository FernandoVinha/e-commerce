from django.contrib import admin

from .models import ReproductionStage,Pig,Birth

# Register your models here.

admin.site.register(ReproductionStage)
admin.site.register(Pig)
admin.site.register(Birth)