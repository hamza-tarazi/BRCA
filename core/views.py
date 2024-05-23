from django.shortcuts import redirect, render
from core.forms import UserRegisterForm, CustomerForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def audit_coordination(request):
    return render(request, 'core/audit_coordination.html')

def bookkeeping(request):
    return render(request, 'core/bookkeeping.html')

def external_audit(request):
    return render(request, 'core/external_audit.html')

def internal_audit(request):
    return render(request, 'core/internal_audit.html')

def advisory(request):
    return render(request, 'core/advisory.html')

def Taxation_services(request):
    return render(request, 'core/Taxationservices.html')

def program_support(request):
    return render(request, 'core/NTNRegistration.html')

def IncomeTax(request):
    return render(request, 'core/IncomeTax.html')

def contact(request):
    form = CustomerForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} Message sent successfully")
            new_user = authenticate(username=form.cleaned_data['email'], email=form.cleaned_data['email'], subject=form.cleaned_data['message'], message=form.cleaned_data['message'])
            return redirect("core:index")
        else:
            print("Form is not valid")

    context = {
        'form': form,
    }
    return render(request, 'core/contact.html',context)

def ngo_registration_licensing(request):
    return render(request, 'core/ngo_registration_licensing.html')

def corporate_registration_licensing(request):
    return render(request, 'core/corporate_registration_licensing.html')

def company_registration_withscep(request):
    return render(request, 'core/company_registration_withscep.html')