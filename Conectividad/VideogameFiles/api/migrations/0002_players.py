# Generated by Django 4.1.7 on 2023-04-07 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grupo', models.PositiveIntegerField()),
                ('Numero_de_Lista', models.PositiveIntegerField()),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
