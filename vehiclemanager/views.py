from django.shortcuts import render, get_object_or_404
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from .models import Vehicle, Battery
from .forms import VehicleForm, VehicleEditForm


def index(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehiclemanager/vehicle_list.html', {'vehicles': vehicles})


def edit_vehicle(request, vehicle_id):
    BatteryFormSet = inlineformset_factory(Vehicle, Battery, fields=('is_on',), extra=0)

    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    if request.method == "POST":
        form = VehicleEditForm(request.POST, instance=vehicle)
        bform = BatteryFormSet(request.POST, instance=vehicle)
        vehicle.add_batteries(int(request.POST['addbats']))
        if form.is_valid():
            form.save()
            bform.save()
            return HttpResponseRedirect('/')

    else:
        form = VehicleEditForm(instance=vehicle)

    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    bformset = BatteryFormSet(instance=vehicle)

    return render(request, 'vehiclemanager/edit_vehicle.html',
                  {'vehicle': vehicle, 'form': form.as_p(), 'bformset': bformset})


def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()

            vehicle = Vehicle.objects.get(id=form.cleaned_data['id'])
            vehicle.add_batteries(form.cleaned_data['batteries'])

            return HttpResponseRedirect('/')

    else:
        form = VehicleForm()

    return render(request, 'vehiclemanager/add_vehicle.html', {'form': form.as_p()})


def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    batteries = Battery.objects.filter(vehicle=vehicle)
    batteries.delete()
    vehicle.delete()
    return HttpResponseRedirect('/')
