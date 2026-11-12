from django.db import models
from submission.models import Submission
from question.models import Question


# Create your models here.

class Answer(models.Model):
    submission=models.ForeignKey(Submission,on_delete=models.CASCADE,related_name='answer')
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answer')
    answer_text=models.TextField()
    awarded_marks=models.FloatField(default=0)
    feedback=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.submission}-{self.question}"


    # this change is from abhina 
