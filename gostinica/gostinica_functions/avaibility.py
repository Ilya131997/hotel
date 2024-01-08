
from ..models import Room, Reservation


def check_availability(room, check_in, check_out):
    """
    Функция check_availability проверяет номера
    """
    avail_list = []
    reservation_list = Reservation.objects.filter(room=room)

    # Проверка
    for reservation in reservation_list:
        if reservation.check_in_date > check_out or reservation.check_out_date < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)