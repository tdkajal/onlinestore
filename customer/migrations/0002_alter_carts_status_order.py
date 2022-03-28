# Generated by Django 4.0.2 on 2022-03-28 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('owner', '0003_books_image'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carts',
            name='status',
            field=models.CharField(choices=[('incart', 'incart'), ('cancelled', 'cancelled'), ('orderplaced', 'orderplaced')], default='incart', max_length=120),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('order_placed', 'order_placed'), ('dispatched', 'dispatched'), ('intransit', 'intransit'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='order_placed', max_length=120)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.books')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
