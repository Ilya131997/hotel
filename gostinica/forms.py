from django import forms
from .models import Room, Reservation, TypeRoom, Build_obj


class CreateRoomForm(forms.ModelForm):
    type_room = forms.ModelChoiceField(queryset=TypeRoom.objects.all(), empty_label='Категория не выбрана',
                                       label='Тип номера', widget=forms.Select(attrs={'class': 'form-control'}))
    build = forms.ModelChoiceField(queryset=Build_obj.objects.all(), empty_label='Категория не выбрана',
                                       label='Объект', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Room
        fields = ['build', 'room_number', 'cost_night', 'description', 'type_room', 'photo']

        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_night': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdateRoomForm(forms.ModelForm):
    type_room = forms.ModelChoiceField(queryset=TypeRoom.objects.all(), empty_label='Категория не выбрана',
                                       label='Тип номера', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Room
        fields = ['room_number', 'cost_night', 'description', 'type_room', 'photo']

        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_night': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in_date', 'check_out_date', 'room']

        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }
