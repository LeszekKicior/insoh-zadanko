from django.forms import ModelForm, IntegerField
from .models import Vehicle


class VehicleForm(ModelForm):
    batteries = IntegerField(label="Liczba baterii")

    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'batteries']


class VehicleEditForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name']
