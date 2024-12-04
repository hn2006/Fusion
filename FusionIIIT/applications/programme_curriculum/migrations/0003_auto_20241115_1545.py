# Generated by Django 3.1.5 on 2024-11-15 15:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0002_moduleaccess'),
        ('programme_curriculum', '0002_course_max_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinstructor',
            name='semester_no',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AddField(
            model_name='courseinstructor',
            name='year',
            field=models.IntegerField(default=2024),
        ),
        migrations.AlterField(
            model_name='courseinstructor',
            name='instructor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.faculty'),
        ),
        migrations.AlterUniqueTogether(
            name='courseinstructor',
            unique_together={('course_id', 'instructor_id', 'year')},
        ),
        migrations.RemoveField(
            model_name='courseinstructor',
            name='batch_id',
        ),
    ]