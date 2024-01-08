from django import template

register = template.Library()

@register.filter(name='is_room_reserved')
def is_room_reserved(room_reservations, room_id, day):
    return room_id in room_reservations and day in room_reservations[room_id]
