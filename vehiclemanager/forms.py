from django.forms import ModelForm, IntegerField, inlineformset_factory
from .models import Vehicle, Battery


class VehicleForm(ModelForm):
    batteries = IntegerField(label="Liczba baterii")

    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'batteries']


class VehicleEditForm(ModelForm):

    class Meta:
        model = Vehicle
        fields = ['name']
