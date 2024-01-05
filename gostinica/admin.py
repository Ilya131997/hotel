from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

@admin.register(Build_obj)
class BuildObjAdmin(admin.ModelAdmin):
    """
    Класс BuildObjAdmin для создания объектов в админке
    """
    list_display = ('title', 'address')
    fields = ['title', 'address']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """
    Класс RoomAdmin служит созданию комнат в админке
    """
    list_display = ('build', 'room_number', 'room_photo', 'cost_night', 'typeroom', 'description')
    readonly_fields = ['room_photo']
    list_filter = ('cost_night', 'typeroom')
    fields = ['build', 'room_number', 'room_photo', 'cost_night', 'typeroom', 'description']
    list_display_links = ['room_number', 'cost_night']

    @admin.display(description='Изображение')
    def room_photo(self, room):
        """
        Функция room_photo для отображения фотографий в админке
        """
        if room.photo:
            return mark_safe(f"<img src='{room.photo.url}' width=90>")
        return "Без фото"


@admin.register(TypeRoom)
class TypeRoomAdmin(admin.ModelAdmin):
    """
    Класс TypeRoomAdmin для создания типа комнат
    """
    list_display = ('title',)
