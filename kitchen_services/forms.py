from django import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen_services.models import Cook


class CookCreationForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_of_experience", )
