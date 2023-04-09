from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]
    
    # TODO: 글 삭제시 media파일 삭제 구현
