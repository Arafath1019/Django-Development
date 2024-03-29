# Generated by Django 5.0 on 2024-02-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0008_alter_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class_in',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='class_in',
            field=models.ManyToManyField(related_name='class_set', to='tuition.class_in'),
        ),
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.ManyToManyField(related_name='subject_set', to='tuition.subject'),
        ),
    ]
