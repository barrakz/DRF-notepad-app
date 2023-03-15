import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

from notes.models import Note

API_KEY = "ea679c42e69243953ce83f1851ae7a4d"


def get_temperature():
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Sopot&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']

    return temperature


@receiver(post_save, sender=Note)
def add_temperature(sender, instance, created, **kwargs):
    if created:
        temperature = get_temperature()
        instance.temperature = temperature
        instance.save()