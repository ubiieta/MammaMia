from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['npersonas', 'hora', 'fecha', 'email']
        widgets = {
            'npersonas': forms.NumberInput(attrs={
                'class': 'form-control form-control-lg custom-form-control',
                'placeholder': 'NUMERO DE COMENSALES',
                'max': 20,
                'min': 1,
            }),
            'hora': forms.TimeInput(attrs={
                'class': 'form-control form-control-lg custom-form-control',
                'type': 'time',  # Asegura que sea un campo HTML <input type="time">
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control form-control-lg custom-form-control',
                'type': 'date',  # Asegura que sea un campo HTML <input type="date">
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg custom-form-control',
                'placeholder': 'EMAIL',
            }),
        }
