# Generated by Django 2.1.4 on 2019-04-28 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190427_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_brand', models.CharField(max_length=50)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cust', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
            ],
        ),
    ]
