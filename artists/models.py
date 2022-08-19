from django.db import models
import uuid

class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    instagram_link = models.CharField(max_length=2000, null=True, blank=True)
    head_shot = models.ImageField(null=True, blank=True)
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_3 = models.ImageField(null=True, blank=True)
    image_4 = models.ImageField(null=True, blank=True)
    image_5 = models.ImageField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)


    def __str__(self):
        return self.first_name + " " + self.last_name     
    #image render safe check
    
    @property
    def image_url(self):
        def get_img_url(img):
            if img:
                return img.url
            else:
                return ''
        return{
                "headshot": get_img_url(self.head_shot),
                "img1" :get_img_url(self.image_1),
                "img2" : get_img_url(self.image_2),
                "img3" : get_img_url(self.image_3),
                "img4" : get_img_url(self.image_4),
                "img5" : get_img_url(self.image_5)
        }
    
    
class GuestArtist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    instagram_link = models.CharField(max_length=2000, null=True, blank=True)
    head_shot = models.ImageField(null=True, blank=True)
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_3 = models.ImageField(null=True, blank=True)
    image_4 = models.ImageField(null=True, blank=True)
    image_5 = models.ImageField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)


    def __str__(self):
        return self.first_name + " " + self.last_name     
    #image render safe check
    @property
    def imgURL(self):
        try:
            h_url = self.head_shot.url,
            img1 = self.image_1.url
            img2 = self.image_2.url
            img3 = self.image_3.url
            img4 = self.image_4.url
            img5 = self.image_5.url

        except:
            h_url = ''
            img1 = ''
            img2 = ''
            img3 = ''
            img4 = ''
            img5 = ''

        return h_url,img1,img2,img3,img4,img5
        # try:
        #         headshot = self.head_shot.url
        #         img1 = self.image_1.url
        #         img2 = self.image_2.url
        #         img3 = self.image_3.url
        #         img4 = self.image_4.url
        #         img5 = self.image_5.url
        # except:
        #     headshot = ''
        #     img1 = ''
        #     img2 = ''
        #     img3 = ''
        #     img4 = ''
        #     img5 = ''
        # return headshot, img1, img2, img3, img4, img5