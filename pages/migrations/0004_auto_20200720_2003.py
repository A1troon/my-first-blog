# Generated by Django 3.0.8 on 2020-07-20 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='favour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('length', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='interest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.favour'),
        ),
    ]