from django.db import models
from datetime import date
import uuid

class Artist(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    instagram_link = models.CharField(max_length=2000, null=True, blank=True)
    head_shot = models.CharField(max_length=250,null=True, blank=True)
    main_profile = models.CharField(max_length=250,null=True, blank=True)
    insta_image = models.CharField(max_length=250,null=True, blank=True)
    email = models.EmailField(max_length=250,null=True, blank=True)
    image_0 = models.CharField(max_length=250,null=True, blank=True)
    image_1 = models.CharField(max_length=250,null=True, blank=True)
    image_2 = models.CharField(max_length=250,null=True, blank=True)
    image_3 = models.CharField(max_length=250,null=True, blank=True)
    image_4 = models.CharField(max_length=250,null=True, blank=True)
    image_5 = models.CharField(max_length=250,null=True, blank=True)
    image_6 = models.CharField(max_length=250,null=True, blank=True)
    image_7 = models.CharField(max_length=250,null=True, blank=True)
    image_8 = models.CharField(max_length=250,null=True, blank=True)
    image_9 = models.CharField(max_length=250,null=True, blank=True)
    apprentice = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)


    def __str__(self):
        return self.name 
    #image render safe check
    
    # @property
    # def image_url(self):
    #     def get_img_url(img):
    #         if img:
    #             return img.url
    #         else:
    #             return ''
    #     return{
    #             "headshot": get_img_url(self.head_shot),
    #             "img1" :get_img_url(self.image_1),
    #             "img2" : get_img_url(self.image_2),
    #             "img3" : get_img_url(self.image_3),
    #             "img4" : get_img_url(self.image_4),
    #             "img5" : get_img_url(self.image_5)
    #     }
    
    
class GuestArtist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    instagram_link = models.CharField(max_length=2000, null=True, blank=True)
    head_shot = models.ImageField(null=True, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)


    def __str__(self):
        return self.first_name + " " + self.last_name     
    
    @property
    def get_current(self):
        start = self.start_date
        end = self.end_date
        today = date.today()
        # print("-------------------------------")
        # print(self.first_name)
        # print("Start-Date:  ",start)
        # print("End-Date:  ",end)
        # print("Today:  ",today)
        if today < start:
            return False
        elif today >= start and today < end:
             return True                  
        elif today >= end:
                self.delete()
    # @property
    # def get_curr_sec(self):
    #     start = self.start_date
    #     end = self.end_date
    #     today = date.today()
    #     flag = False
    #     while flag:
    #         if today < start:
    #             pass
    #         elif today >= start and today < end:
    #             flag = True
    #             return flag                  
    # @property
    # def get_upcoming_sec(self):
    #     start = self.start_date
    #     end = self.end_date
    #     today = date.today()
    #     flag = False
    #     print("trigg")
    #     while flag:
    #         # print("------------- INside loop--------------")
    #         if today < start:
    #             # print("Found")
    #             flag = True
    #             return flag 
    #         elif today >= start and today < end:
    #             pass 