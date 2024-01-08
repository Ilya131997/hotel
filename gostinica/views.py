import datetime
from calendar import monthcalendar
from datetime import date, timedelta
import calendar
from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView

from .forms import CreateRoomForm, ReservationForm, UpdateRoomForm
from .gostinica_functions.avaibility import check_availability
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


class RoomListView(ListView):
    model = Room
    template_name = 'gostinica/room_list.html'
    context_object_name = 'room_list'


class AddRoom(CreateView):
    form_class = CreateRoomForm
    template_name = 'gostinica/addroom.html'
    success_url = reverse_lazy('home')


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


class AdminRoomListView(ListView):
    """
    Класс AdminRoomListView для вывода списка номеров на странице администратора
    """
    model = Room
    template_name = 'gostinica/admin_room_list.html'
    context_object_name = 'room_list'

    def get_queryset(self):
        """
        В методе get_queryset мы фильтруем номера которые будут доступны по параметру build и открываем их
        """
        build_param = self.request.GET.get('build')
        if build_param:
            return Room.objects.filter(build__title=build_param)


class AdminReservationList(ListView):
    model = Reservation
    template_name = 'gostinica/reservation_admin_page.html'
    context_object_name = 'reservation_list'

    def get_queryset(self):
        # Ваша логика для получения бронирований
        # Например, можно добавить фильтрацию по месяцу, если нужно
        return Reservation.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавьте другие переменные, если нужно
        context['selected_month'] = self.request.GET.get('month', None)
        context['rooms'] = Room.objects.all()  # Ваш список комнат

        # Получаем текущий год и месяц из параметра 'month' или из текущей даты
        selected_month = context['selected_month']
        if selected_month:
            year, month = map(int, selected_month.split('-'))
        else:
            now = datetime.now()
            year, month = now.year, now.month

        # Получаем список дней в текущем месяце
        _, last_day = calendar.monthrange(year, month)
        context['days_in_month'] = list(range(1, last_day + 1))

        return context
    # def get_queryset(self):
    #     # Получите выбранный месяц из параметра запроса
    #     selected_month = self.request.GET.get('month')
    #     if selected_month:
    #         # Преобразуйте строку в объект datetime
    #         selected_month = date.fromisoformat(selected_month + "-01")
    #         # Фильтруйте по выбранному месяцу
    #         queryset = Reservation.objects.filter(check_in_date__month=selected_month.month)
    #         print(queryset)
    #     else:
    #         # Если месяц не выбран, покажите все бронирования
    #         queryset = Reservation.objects.all()
    #
    #     return queryset
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Передача rooms в шаблон для вывода номеров
    #     context['rooms'] = Room.objects.all()
    #     # Установка месяца выбранного
    #     context['selected_month'] = self.request.GET.get('month')
    #
    #     # Структура данных для хранения занятых дней для каждой комнаты
    #     room_reservations = {}
    #     for reservation in context['reservation_list']:
    #         room_id = reservation.room.id if hasattr(reservation, 'room') else None
    #         check_in = reservation.check_in_date if hasattr(reservation, 'check_in_date') else None
    #         check_out = reservation.check_out_date if hasattr(reservation, 'check_out_date') else None
    #
    #         if room_id is not None and check_in is not None and check_out is not None:
    #             if room_id not in room_reservations:
    #                 room_reservations[room_id] = []
    #
    #             # Добавьте проверку на DeferredAttribute перед операцией вычитания
    #             if hasattr(check_in, 'date') and hasattr(check_out, 'date'):
    #                 days_reserved = [check_in.date() + timedelta(days=i) for i in
    #                                  range((check_out.date() - check_in.date()).days + 1)]
    #                 room_reservations[room_id].extend(days_reserved)
    #     context['room_reservations'] = room_reservations
    #
    #     return context
