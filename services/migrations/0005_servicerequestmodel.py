# Generated by Django 3.2.9 on 2021-11-30 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20211130_0900'),
        ('services', '0004_services_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('request', models.TextField()),
                ('service', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='services.services')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='profiles.userprofile')),
            ],
        ),
    ]
