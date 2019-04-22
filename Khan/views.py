from django.shortcuts import render, redirect
from django.http import HttpResponse
from .maple import *
from .forms import *
from .serializer import *
from django.contrib import messages
# Create your views here.

def MapleStory(request):
    if request.method == 'POST':
        form = MapleNameForm(request.POST, request.FILES)

        if 'AddDB' in request.POST:
            if form.is_valid():
                MapleName = form.cleaned_data['MapleName']
                Data = MapleData(MapleName)
            else:
                Data = MapleData_GET()

        elif 'DeleteDB' in request.POST:
            DelID = request.POST['DeleteDB']
            Maple = MapleDB.object.get(id=int(DelID))
            Maple.delete()
            Data = MapleData_GET()
            
    else:
        # GET 방식 또는 다른 형식 데이터 처리
        Data = MapleData_GET()

    return render(request, 'Choi/index.html', Data)
