
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assessment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('in_progress', 'In Progress'), ('submitted', 'Submitted')], default='in_progress', max_length=20)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('submitted_at', models.DateTimeField(blank=True, null=True)),
                ('total_marks', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
<<<<<<< HEAD
                ('evaluation_status', models.CharField(choices=[('pending', 'Pending'), ('evaluated', 'Evaluated')], default='pending', max_length=20)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='assessment.assessment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('student', 'assessment'), name='unique_student_assessment_submission')],
            },
=======
                ('evaluation_status', models.CharField(choices=[('in_progress', 'n_progress'), ('evaluated', 'Evaluated')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='assessment.assessment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
>>>>>>> fc9adb5b9c61b114a12be41a3c4f2bdb79850c5a
        ),
    ]
