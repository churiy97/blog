# Generated by Django 3.0.6 on 2020-07-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_image', models.ImageField(upload_to='event_images/')),
                ('event_text', models.CharField(max_length=300)),
            ],
        ),
    ]
