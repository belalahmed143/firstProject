# Generated by Django 2.2 on 2020-08-13 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0.0)),
                ('descriptionn', models.CharField(max_length=200)),
                ('product_img', models.ImageField(default='no_image.jpg', upload_to='Product_Image')),
            ],
        ),
    ]
