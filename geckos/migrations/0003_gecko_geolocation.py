# Generated by Django 4.2.2 on 2023-07-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geckos', '0002_gecko_discovered'),
    ]

    operations = [
        migrations.AddField(
            model_name='gecko',
            name='geoLocation',
            field=models.CharField(default=(-21.25, 165.3), max_length=200),
            preserve_default=False,
        ),
    ]
