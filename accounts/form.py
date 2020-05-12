from django.forms import ModelForm
from .models import Order # call class Order in model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #import user model bawaan django

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']