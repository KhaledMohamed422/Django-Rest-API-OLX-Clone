# Generated by Django 4.1.7 on 2023-03-05 23:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(choices=[('Mobiles', (('Mobile_Phones', 'Mobile Phones'), ('Tablets', 'Tablets'), ('Accessories', 'Accessories'), ('otherwise', 'otherwise'))), ('Electronics&Appliances', (('Computers&Accessories', 'Computers & Accessories'), ('Tv-Video-Audio', 'Tv - Video - Audio'), ('Games&Entertainment', 'Games & Entertainment'), ('Cameras&Accessories', 'Cameras & Accessories'), ('Fridge_AC_Washing_Machine', 'Fridge - AC - Washing Machine'), ('Kitchen&OtherAppliances', 'Kitchen & Other Appliances'))), ('Cars', (('Spare_Parts', 'Spare Parts'), ('Other_Vehicles', 'Other Vehicles'), ('Spare_Parts', 'Spare Parts'), ('Cameras&Accessories', 'Cameras & Accessories'), ('Fridge_AC_Washing_Machine', 'Fridge - AC - Washing Machine'), ('Kitchen&OtherAppliances', 'Kitchen & Other Appliances'))), ('Bikes', (('Bicycles', 'Bicycles'), ('Scooters', 'Scooters'), ('Spare_Parts', 'Spare Parts'), ('Motorcycles', 'Motorcycles')))], max_length=30)),
                ('view', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='id',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='images',
            field=models.ManyToManyField(to='api.images'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='is_trend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='time_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='Categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.categories'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='Id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
