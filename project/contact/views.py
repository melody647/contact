from .models import ContactInfo
from django.shortcuts import render,HttpResponse

# Create your views here.

def contact_info(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        detail=request.POST.get("detail")

        try:
            contact_details= ContactInfo.objects.create(name=name,email=email,phone_no=phone,body=detail)
            contact_details.save()
            return HttpResponse("Your request send successfully")
        except Exception as e:
            return HttpResponse("Your information you entered is incorrect")
        
    return render(request,'contact/index.html')