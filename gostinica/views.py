from django.shortcuts import render

from .models import *


def index(request):
    room_list = Room.objects.all()
    context = {
        'room_list': room_list,
    }
    return render(request, 'gostinica/index.html', context=context)


def rooms(request):
    # room_list = Room.objects.all()
    # context = {
    #     'room_list': room_list,
    # }
    room_type = request.GET.get('room_type', 'all')

    if room_type == 'all':
        filtered_rooms = Room.objects.all()
    else:
        filtered_rooms = Room.objects.filter(typeroom=room_type)
    return render(request, 'gostinica/rooms.html', {'filtered_rooms': filtered_rooms})
