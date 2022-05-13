
from django.forms import ModelForm
from .models import StudentDetails

class StudentForm(ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['Name', 'Age', 'Father_Name', 'Group', 'Location', 'Mole_One', 'Mole_Two']