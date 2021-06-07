# Generated by Django 3.2.4 on 2021-06-07 21:02

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
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=255)),
                ('plan', models.CharField(max_length=255)),
                ('specialty', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('score', models.IntegerField()),
                ('credits', models.IntegerField()),
                ('entry_period', models.CharField(max_length=255)),
                ('validated_periods', models.IntegerField()),
                ('last_period', models.CharField(max_length=255)),
                ('tutor', models.CharField(max_length=255)),
                ('curp', models.CharField(max_length=255)),
                ('birthdate', models.DateTimeField()),
                ('address', models.CharField(max_length=255)),
                ('home_phone', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('origin_school', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]