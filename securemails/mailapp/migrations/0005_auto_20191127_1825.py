# Generated by Django 2.2.7 on 2019-11-27 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailapp', '0004_userprofileinfo_userpubkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgsdata',
            name='value',
            field=models.TextField(max_length=1000),
        ),
        migrations.CreateModel(
            name='SessionKeysEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyEncA', models.TextField()),
                ('keyEncB', models.TextField()),
                ('userA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
                ('userB', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
