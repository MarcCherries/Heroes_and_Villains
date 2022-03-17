# Generated by Django 4.0.3 on 2022-03-17 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supers_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alter_ego', models.CharField(max_length=255)),
                ('primary_ability', models.CharField(max_length=255)),
                ('secondary_ability', models.CharField(max_length=255)),
                ('catch_phrase', models.CharField(max_length=255)),
                ('super_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supers_type.super_type')),
            ],
        ),
    ]