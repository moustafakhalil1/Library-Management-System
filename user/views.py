from django.shortcuts import render,redirect
from .form import ctreateuserform
# Create your views here.
def register(request):
    if request.method=='POST':
        form=ctreateuserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form=ctreateuserform(request.POST)
        
    context={
        'form':form,
     }
    return render(request,'user/register.html',context)
