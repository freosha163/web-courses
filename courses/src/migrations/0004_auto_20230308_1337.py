# Generated by Django 3.2.18 on 2023-03-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_alter_teacher_webinar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='course',
        ),
        migrations.AddField(
            model_name='teacher',
            name='course',
            field=models.ManyToManyField(null=True, to='src.Course', verbose_name='Курсы преподавателя'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='webinar',
            field=models.ManyToManyField(null=True, to='src.Webinar', verbose_name='Вебинары преподавателя'),
        ),
    ]