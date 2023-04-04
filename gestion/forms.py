from django.forms import ModelForm,DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class addorder(ModelForm):
    class Meta:
        widgets = {'date_debut':DateInput()}
        model = order
        fields = '__all__'


class addcustomer(ModelForm):
    class Meta:
        model = client
        fields = '__all__'

class addoffer(ModelForm):
    class Meta:
        model = Place
        fields = '__all__'


