# Generated by Django 4.1.3 on 2022-12-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockapi', '0002_pool_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='pool',
            name='reward_rate',
            field=models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=25, null=True),
        ),
    ]