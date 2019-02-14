# Generated by Django 2.0.6 on 2018-10-29 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_auto_20181029_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appform1',
            name='add1',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='add2',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='brno',
            field=models.CharField(default=0, max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='fathc',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='fathna',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='fatho',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='fname',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='lname',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='mark',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='mothc',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='mothna',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='motho',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='padd1',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='padd2',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='pcity',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='pcountry',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='photo',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='ppincode',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='pstate',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='ques',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='appform1',
            name='sign',
            field=models.FileField(upload_to='images/'),
        ),
    ]
