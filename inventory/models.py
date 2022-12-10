from django.db import models

# Create your models here.
category_list = (
    ('CPUs', 'CPUs'),
    ('Monitors', 'Monitors'),
    ('Peripherals', 'Peripherals'),
    ('Laptop', 'Laptop'),
    ('Printers', 'Printers'),
    ('Adapters', 'Adapters')
)

status_list = (
    ('Deployed and Working', 'Deployed and Working'),
    ('Not deployed but working', 'Not deployed but working'),
    ('Not Working', 'Not Working'),
    ('Under Repair', 'Under Repair'),
)


class Inventory(models.Model):
    class Meta:
        verbose_name_plural = "Assets"

    model = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(
        max_length=50, blank=True, null=True, choices=category_list)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(
        max_length=50, blank=True, null=True, choices=status_list)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.model
