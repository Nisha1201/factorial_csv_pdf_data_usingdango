# Generated by Django 3.2.18 on 2023-04-07 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('factorial', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='factmulti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multifactorial', models.TextField()),
                ('photo', models.ImageField(upload_to='pics/')),
                ('factorial_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='testdemo.fact')),
            ],
        ),
    ]
