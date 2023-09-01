from django.shortcuts import render

# Create your views here.

from app.models import *

def insert_school(request):
    if request.method=='POST':
        scn = request.POST['scn']
        scp = request.POST['scp']
        scl = request.POST['scl']
        sco = School.objects.get_or_create(ScName=scn, ScPrincipal=scp, ScLocation=scl)[0]
        sco.save()
        
        QLSC = School.objects.all()
        d = {'QLSC': QLSC}
        return render(request, 'display_school.html', d)
    
    
    return render(request, 'insert_school.html')


def insert_student(request):
    if request.method=='POST':
        
        #fetching data using keys from request.post dict where the submitted data is wrapped
        scn = request.POST['scn']
        sn = request.POST['sn']
        sid = request.POST['sid']
        
        sco = School.objects.get(ScName=scn)
        
        sto = Student.objects.get_or_create(ScName=sco, StudName=sn, SID=sid)[0]
        sto.save()
        
        QLST = Student.objects.all()
        d = {'QLST': QLST}
        return render(request, 'display_student.html', d)
    
    
    return render(request, 'insert_student.html')
        

