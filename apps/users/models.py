from django.db import models
from apps.common.models import BaseModel
from django.contrib.auth.hashers import make_password,check_password

class CustomUser(BaseModel):
    email=models.EmailField(unique=True)
    login=models.CharField(max_length=125)
    parol=models.CharField(max_length=225)
    
    def set_password(self,raw_password):
        self.password=make_password(raw_password)
    
    def check_password(self,raw_password):
        return check_password(raw_password,self.password)
    
    def __str__(self):
        return self.login
    


    