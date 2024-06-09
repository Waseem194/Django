from django.contrib import admin
from .models import ChaiVariety, ChaiReview, Store, ChaiCertificate

# Register your models here.

class ChaiRewiewInLine(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiRewiewInLine]


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'Location')
    filter_horizontal = ('Chai_Varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issued_date', 'valid_date')

admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
