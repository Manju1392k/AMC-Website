
from django.forms import ModelForm
from .models import StudentDetails
from django import forms


class StudentForm(ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['Name', 'Age', 'Father_Name',
                  'Group', 'Location', 'Mole_One', 'Mole_One']

    Name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    Age = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    Father_Name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Group = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    Location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Mole_One = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Mole_One = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
