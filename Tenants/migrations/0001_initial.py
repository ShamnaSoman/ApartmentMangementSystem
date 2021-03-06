# Generated by Django 4.0.2 on 2022-02-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Contact', models.TextField()),
                ('No_members', models.IntegerField(blank=True, null=True)),
                ('Apartment_no', models.IntegerField(blank=True, null=True)),
                ('Con_start_date', models.DateField()),
                ('Con_end_date', models.DateField()),
                ('Rental_amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.TextField(max_length=20)),
            ],
        ),
    ]
