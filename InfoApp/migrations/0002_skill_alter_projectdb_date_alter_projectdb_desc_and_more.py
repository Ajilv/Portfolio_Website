# Generated by Django 5.1.6 on 2025-03-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='projectdb',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdb',
            name='desc',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='projectdb',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='projectdb',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='projectdb',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='projectdb',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='projectdb',
            name='skills',
        ),
        migrations.AddField(
            model_name='projectdb',
            name='skills',
            field=models.ManyToManyField(to='InfoApp.skill'),
        ),
    ]
