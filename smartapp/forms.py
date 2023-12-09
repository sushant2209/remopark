# forms.py

from django import forms

class BookingForm(forms.Form):
    available_slots = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple(attrs={'class': 'slot-checkbox'}))
    
    def __init__(self, *args, **kwargs):
        slot_info = kwargs.pop('slot_info')
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['available_slots'].choices = [(str(key), f"{slot_info[key]}") for key in slot_info.keys()]
# forms.py


from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
   