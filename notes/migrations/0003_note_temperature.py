# Generated by Django 4.1.7 on 2023-03-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_tag_note_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='temperature',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]