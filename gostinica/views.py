from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView

from .forms import CreateRoomForm, ReservationForm, UpdateRoomForm
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


class AddRoom(CreateView):
    form_class = CreateRoomForm
    template_name = 'gostinica/addroom.html'
    success_url = reverse_lazy('home')


class RoomListView(ListView):
    model = Room
    template_name = 'gostinica/room_list.html'
    context_object_name = 'room_list'


class RoomUpdateView(UpdateView):
    model = Room
    template_name = 'gostinica/room_edit.html'
    form_class = UpdateRoomForm
    success_url = reverse_lazy('room_list')

    def get_form_kwargs(self):
        """
        Метод get_form_kwargs что бы при обновления номера, сохранялось прежнее значение type_room
        """
        kwargs = super(RoomUpdateView, self).get_form_kwargs()
        kwargs['initial']['type_room'] = self.object.typeroom
        return kwargs

class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'gostinica/room_delete.html'
    success_url = reverse_lazy('room_list')


class ReservationView(CreateView):
    template_name = 'gostinica/reservation_form.html'
    form_class = ReservationForm
    success_url = reverse_lazy('rooms')

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(f'Check-in Date: {form.cleaned_data["check_in_date"]}')
        print(f'Check-out Date: {form.cleaned_data["check_out_date"]}')
        print(f'Room: {form.cleaned_data["room"]}')
        print(f'User: {form.instance.user}')
        form.instance.status = 'c'
        return super().form_valid(form)
def table(request):
    return render(request, 'gostinica/eventcalendar_month-view.html')
