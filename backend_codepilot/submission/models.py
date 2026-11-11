from django.db import models

from user.models import User

from assessment.models import Assessment

class Submission(models.Model):

    STATUS_CHOICES = [

        ('in_progress', 'In Progress'),

        ('submitted', 'Submitted'),
    ]

    EVALUATION_STATUS_CHOICES = [

        ('pending', 'Pending'),

        ('evaluated', 'Evaluated'),

    ]

    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name='submissions')

    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE,related_name='submissions')

    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='in_progress')

    started_at = models.DateTimeField(auto_now_add=True)

    submitted_at = models.DateTimeField(null=True,blank=True)

    total_marks = models.DecimalField(max_digits=7,decimal_places=2,default=0)

    evaluation_status = models.CharField(max_length=20,choices=EVALUATION_STATUS_CHOICES,default='pending')

    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=['student', 'assessment'],
                name='unique_student_assessment_submission')
        ]

    def __str__(self):

        return f"{self.student.username} - {self.assessment.title}"

