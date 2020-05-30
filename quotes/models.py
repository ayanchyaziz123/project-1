from django.db import models
from datetime import datetime, date

# Create your models here.

class tbl_category(models.Model):
    cat_name = models.CharField(max_length=200)

    def __str__(self):
          return self.cat_name

class tbl_adminPost(models.Model):
    ap_postTitle = models.CharField(max_length=200)
    ap_postPost = models.TextField()
    ap_postDateTime = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    ap_postAuthor = models.CharField(max_length=200)
    ap_postImage = models.ImageField(null=True, blank=True)



    post_cat = models.ForeignKey(
        'tbl_category',
        on_delete= models.CASCADE

    )

    def get_photo_url(self):
        if self.ap_postImage and hasattr(self.ap_postImage, 'url'):
            return self.ap_postImage.url
        else:
            return "/static/aya.jpeg"



    def __str__(self):
        if len(self.ap_postTitle)> 50 :
            return self.ap_postTitle[:50] + "..."
        else:
            return self.ap_postTitle

