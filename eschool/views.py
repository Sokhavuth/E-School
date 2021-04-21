from django.shortcuts import render
from django.http import HttpResponse
from .models import Lesson

context = {'site_title': 'E-School'}

def index(request):
    lessons = Lesson.objects.all()[:4]
    video_ids = [lesson.video_id for lesson in lessons]
    context['video_ids'] = video_ids

    return render(request, 'index.html', context=context)