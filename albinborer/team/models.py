from django.db import models
from django.forms import ModelForm

class Designation(models.Model):
    designation = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.designation

class Member(models.Model):
    designation		= models.ForeignKey(Designation, on_delete=models.CASCADE,)
    name			= models.CharField(max_length=264, unique=False)
    board_member	= models.CharField(max_length=220, blank=True, null=True)
    board_detail	= models.CharField(max_length=220, blank=True, null=True)
    email_url		= models.URLField()
    tele_phone		= models.CharField(max_length=12, null=True)
    tele_fax		= models.CharField(max_length=10, null=True)
    location		= models.CharField(max_length=264, null=True)
    image			= models.ImageField(null=True, blank=True, upload_to="Member_profile_upload/")

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Member, on_delete=models.CASCADE,)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
