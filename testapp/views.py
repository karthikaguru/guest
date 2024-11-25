from django.shortcuts import render,redirect
from testapp.models import Employee
from forms import  Employee_forms

# Create your views here.
def main(request):
    emp=Employee.objects.all()
    return render(request,'testapp/test.html',{'emp':emp})
def form(request):
    form=Employee_forms()
    if request.method=="POST":
        form=Employee_forms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/main')
    return render(request,'testapp/create.html',{'form':form})


