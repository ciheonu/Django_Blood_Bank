from .models import Donor
from django import forms


class DonorUpdateForm(forms.ModelForm):

    class Meta:
        model = Donor
        fields = ['blood_group', 'genotype', 'date_of_birth', 'address', 'city', 'state', 'country', 'zipcode', 'phone_number',

                  'will_donate', 'sex']

        labels = {
            'date_of_birth': 'Date Of Birth',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

