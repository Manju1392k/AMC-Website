from django.shortcuts import render
from . forms import StudentForm

# Create your views here.


def Home(request):
    AdminForm = StudentForm
    if request.method == 'POST':
        AdminForm = StudentForm(request.POST)
        if AdminForm.is_valid():
            AdminForm.save()
    return render(request, 'index.html', {'AdminForm': AdminForm})
