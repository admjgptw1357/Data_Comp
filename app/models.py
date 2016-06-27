#-*-coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Competitioのデータベースモデル
class Competition(models.Model):
    SCORING_CHOICES = (
        (u'MSE', u'MSE'),
        (u'RMSE', u'RMSE'),
        (u'Correlation', u'CORRELATION'),
        (u'Accuracy', u'ACCURACY'),
        (u'F1', u'F1'),
        (u'Adjusted Rand Score', u'ADJUSTED RAND SCORE'),

    )

    CONTEST_CHOICES=(
        (u'Regression','regression'),
        (u'Classification', 'classification'),
        (u'Clustering', 'clustering'),
    )

    name = models.CharField("competition name",max_length=255,unique=True)
    description = models.TextField('description', blank=True)
    contest_type = models.CharField("contest type",choices=CONTEST_CHOICES,max_length=20,default="regression")
    scoring = models.CharField("scoring method",choices=SCORING_CHOICES,max_length=20,default="RMSE")
    data_number = models.IntegerField("answer data size")
    answer = models.TextField('answer')
    mid_test_s = models.IntegerField("start index of mid test",default=0)
    mid_test_e = models.IntegerField("end index of mid test",default=0)
    f_test_s = models.IntegerField("start index of final test",default=0)
    f_test_e = models.IntegerField("end index of final test",default=0)
    end_date =  models.DateTimeField()
    max_submission = models.IntegerField("Max submission per day",default=2)


    def __str__(self):
        return self.name


# Submissionのデータモデル
class Submission(models.Model):
    competition_name = models.ForeignKey(Competition,verbose_name="Competition name",related_name="submission")
    user = models.ForeignKey(User)
    mid_result = models.DecimalField("mid result",max_digits=12, decimal_places=6)
    f_result = models.DecimalField("final result",max_digits=12, decimal_places=6)
    submission_date = models.DateTimeField()
    short_comment = models.CharField("Short Comment",max_length=255,blank=True)
    is_expired = models.IntegerField("is_expired",default=0)

    def __str__(self):
        return User.objects.get(id=self.user_id).username


