# Generated by Django 3.1.6 on 2021-02-05 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classify',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classify.category'),
        ),
    ]
