from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)
    cat_desc = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class QuestionModel(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=120)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    question_desc = models.TextField()
    question_votes = models.IntegerField(default=0)
    question_img = models.ImageField(upload_to='QuestionImg', blank=True, null=True)

    def __str__(self):
        return self.title


class AnswerModel(models.Model):
    answered_by = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    answer_desc = models.TextField()
    answer_votes = models.IntegerField(default=0)
    answer_img = models.ImageField(upload_to='AnswerImg', blank=True, null=True)
    is_accepted = models.BooleanField(default=0)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_desc[:15] + "..."
