# Generated by Django 4.0.4 on 2022-04-28 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='foodstuff',
            fields=[
                ('Mfd_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=60)),
                ('UnitPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('UnitsInStock', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
