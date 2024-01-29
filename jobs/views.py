from django.shortcuts import render
from .models import job

# Create your views here.
def kharak(request):
    jobs=job.objects
    return render(request,'jobs/kharak.html',{'jobs':jobs})

def detail(request, job_id):
    print(job_id)
    return render(request, 'jobs/home.html')

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})
