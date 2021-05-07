from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
     # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]