from django.contrib import admin
from bloodbanks.models import Donor


@admin.register(Donor)
class DonorsAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['first_name', 'last_name', 'blood_group',
                    'genotype', 'will_donate', 'state', 'phone_number']
    list_editable = ['phone_number']
    list_per_page = 10
    list_filter = ['blood_group', 'genotype', 'state']
    list_select_related = ['user']
    search_fields = ['blood_group']
