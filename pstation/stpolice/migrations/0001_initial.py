# Generated by Django 2.2.4 on 2019-08-03 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dps', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Psstate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mps', models.CharField(max_length=30)),
                ('pname', models.CharField(max_length=20)),
                ('noofemp', models.IntegerField()),
                ('dps1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stpolice.Distps')),
            ],
        ),
        migrations.AddField(
            model_name='distps',
            name='pss',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stpolice.Psstate'),
        ),
    ]
