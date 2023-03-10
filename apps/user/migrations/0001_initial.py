# Generated by Django 4.1.4 on 2022-12-17 17:35

import apps.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('username', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('profile_info', models.TextField(blank=True, max_length=255, null=True)),
                ('age', models.CharField(blank=True, choices=[('18+', '18+'), ('Age Restricted', 'Age Restricted')], max_length=14, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('verified', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('location', models.CharField(blank=True, max_length=128, null=True)),
                ('picture', models.ImageField(blank=True, default='user/user_default_profile.png', null=True, upload_to=apps.user.models.user_profile_directory_path, verbose_name='Picture')),
                ('banner', models.ImageField(blank=True, default='user/user_default_bg.jpg', null=True, upload_to=apps.user.models.user_banner_directory_path, verbose_name='Banner')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('total_earnings', models.IntegerField(default=0)),
                ('sales', models.IntegerField(default=0)),
                ('total_spent', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
