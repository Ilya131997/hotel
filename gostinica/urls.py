from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rooms/', views.rooms, name='rooms'),
    path('addroom/', views.AddRoom.as_view(), name='addroom'),
    path('room_list/', views.RoomListView.as_view(), name='room_list'),
    path('room_list/<int:pk>/edit/', views.RoomUpdateView.as_view(), name='room_edit'),
    path('room_list/<int:pk>/delete/', views.RoomDeleteView.as_view(), name='room_delete'),
    path('reservation_room/', views.ReservationView.as_view(), name='reservation_room'),
    path('table/', views.table, name='table'),
    path('admin_room_list/', views.AdminRoomListView.as_view(), name='admin_room_list'),
    path('reservation_admin_page', views.AdminReservationList.as_view(), name='reservation_admin_page')
]
