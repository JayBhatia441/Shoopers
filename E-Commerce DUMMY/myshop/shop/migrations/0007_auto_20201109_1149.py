# Generated by Django 2.2.5 on 2020-11-09 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryClothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryElectronics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('model_no', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryFootwear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('size', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='categoryfootwear',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='categoryelectronics',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='categoryclothes',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='categorybooks',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]