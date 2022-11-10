from allauth.socialaccount.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from customaccount.models import Address

class MyCustomSocialSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSocialSignupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ('username', 'email')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('postcode', 'doromeong_address', 'detail_address', 'extra_address',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields['postcode'].widget.attrs['id'] = 'address_postcode'
            self.fields['doromeong_address'].widget.attrs['id'] = 'doromeong_address'
            self.fields['detail_address'].widget.attrs['id'] = 'detail_address'
            self.fields['extra_address'].widget.attrs['id'] = 'extra_address'