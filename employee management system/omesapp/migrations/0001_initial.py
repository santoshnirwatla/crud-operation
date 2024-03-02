# Generated by Django 4.1.2 on 2023-04-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('dept', models.CharField(max_length=30)),
                ('salary', models.IntegerField()),
                ('mobile', models.DateField()),
                ('add', models.CharField(max_length=30)),
            ],
        ),
    ]