# Generated by Django 4.0.5 on 2022-06-10 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(choices=[('Mwiki - 6:22 AM', 'Mwiki - 6:22 AM'), ('Maji Mazuri - 6:24 AM', 'Maji Mazuri - 6:24 AM'), ('Kamutini -  6:27 AM', 'Kamutini - 6:27 AM'), ('Sunton - 6:30 AM', 'Sunton - 6:30 AM'), ('Hunters - 6:33 AM', 'Hunters - 6:33 AM')], max_length=50, null=True)),
                ('date', models.DateField()),
                ('amount', models.CharField(choices=[('Ksh. 0.00', 'Ksh. 0.00'), ('Ksh. 50.00', 'Ksh. 50.00')], default='Ksh. 50.00', max_length=30, null=True)),
                ('no_of_trips', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=50, null=True)),
                ('booked_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-booked_on'],
            },
        ),
    ]
