from django.db import models


class Vehicle(models.Model):
    id = models.IntegerField(unique=True, null=False, blank=False, primary_key=True, verbose_name="Numer ID")
    name = models.CharField(max_length=50, verbose_name="Nazwa pojazdu")

    @property
    def battery_number(self):
        batteries = Battery.objects.filter(vehicle=self)
        active_count = batteries.filter(is_on=True).count()
        all_count = batteries.count()

        return f"{active_count}/{all_count}"

    def __str__(self):
        return self.name

    def add_batteries(self, num):
        for n in range(num):
            Battery.create(vehicle=self)


class Battery(models.Model):
    battery_number = models.IntegerField(null=False, blank=False, verbose_name="Numer baterii")
    battery_id = models.IntegerField(null=False, blank=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    is_on = models.BooleanField(default=True, verbose_name="Włączona")

    class Meta:
        verbose_name_plural = "batteries"

    @classmethod
    def create(cls, vehicle, is_on=True):
        highest_number = Battery.objects.filter(vehicle=vehicle).order_by('battery_number').last()
        highest_id = Battery.objects.filter(vehicle=vehicle).order_by('battery_id').last()
        b_number = highest_number.battery_number + 1 if highest_number else 1
        b_id = highest_id.battery_id + 2 if highest_id else 5

        b = Battery(vehicle=vehicle, is_on=is_on, battery_number=b_number, battery_id=b_id)
        b.save()
