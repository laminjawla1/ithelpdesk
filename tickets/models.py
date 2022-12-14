from django.db import models
import time
import django

# Create your models here.
cycle_list = (
    ('Pending', 'Pending'),
    ('Open', 'Open'),
    ('Progress', 'Progress'),
    ('Closed', 'Closed'),
)

category_list = (
    ('Software', 'Software'),
    ('Hardware', 'Hardware'),
    ('Liveware', 'Liveware'),
    ('Server', 'Server'),
)

status_list = (
    ('Low', 'Low'),
    ('Mid', 'Mid'),
    ('High', 'High'),
    ('Very High', 'Very High'),
)

level_list = (
    ('Beginner', 'Beginner'),
    ('Amateur', 'Amateur'),
    ('Intermediate', 'Intermediate'),
    ('Advance', 'Advance'),
    ('Pro', 'Pro'),
)

class Zones(models.Model):
    class Meta:
        verbose_name_plural = "Zones"
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class Branches(models.Model):
    class Meta:
        verbose_name_plural = "Branches"
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class Specialization(models.Model):
    field = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.field

class Expert(models.Model):
    image = models.ImageField(
        upload_to='expert_pics/', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    specialization = models.ManyToManyField(Specialization, blank=True)
    level = models.CharField(max_length=100, null=True,
                             choices=level_list, default=level_list[0][0], blank=True)
    bio = models.TextField(null=True, blank=True)
    
    # social media
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Ticket(models.Model):
    branch_list = [
        item for item in Branches.objects.all().values_list('name', 'name').order_by('name')
    ]
    zone_list = [
        item for item in Zones.objects.all().values_list('name', 'name').order_by('name')
    ]


    zone = models.CharField(choices=zone_list, max_length=100)
    branch = models.CharField(choices=branch_list, max_length=100)
    issue = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(
        max_length=100, blank=True, choices=status_list, default=status_list[0][0])
    date = models.DateField(null=True)
    date_submitted = models.DateTimeField(default=django.utils.timezone.now)
    username = models.CharField(max_length=100)
    submitter_name = models.CharField(max_length=120, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=False, null=False)
    image = models.ImageField(
        upload_to='ticket_pics', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    anydesk = models.CharField(max_length=9, blank=True, null=True)
    assigned_to = models.ManyToManyField(Expert)
    time = models.TimeField(default=time.strftime("%H:%M:%S"))
    cycle = models.CharField(
        max_length=100, choices=cycle_list, default=cycle_list[0][0])  # admin
    category = models.CharField(
        max_length=100, choices=category_list, default=category_list[0][0])  # admin
    verification = models.BooleanField(blank=True, null=True)  # admin
    date_closed = models.DateTimeField(null=True, blank=True)  # admin
    documentation = models.TextField(blank=True)

    def __str__(self):
        return self.username
