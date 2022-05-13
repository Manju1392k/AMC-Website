from django.shortcuts import redirect, render
from . forms import StudentForm
from django.contrib import messages

# Create your views here.


def Home(request):
    AdminForm = StudentForm
    if request.method == 'POST':
        AdminForm = StudentForm(request.POST)
        if AdminForm.is_valid():
            AdminForm.save()
            messages.success(
                request, 'Your AdminForm has been submitted successfully')
            return redirect('Home')
    return render(request, 'index.html', {'AdminForm': AdminForm})
