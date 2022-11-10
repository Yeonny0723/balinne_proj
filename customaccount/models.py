from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

# from allauth.socialaccount.models import SocialAccount
# class SocialAccount(SocialAccount, models.Model):
#     age = models.CharField(verbose_name="age", max_length=10)
#     gender = models.CharField(verbose_name="gender", max_length=10)
#     email = models.CharField(verbose_name="email", max_length=50)
#     mobile = models.CharField(verbose_name="mobile", max_length=50)
#     name = models.CharField(verbose_name="name", max_length=50)
#     birthday = models.CharField(verbose_name="birthday", max_length=10)


address_name_choices = (
    ('집','집'),
    ('회사','회사'),
    ('학교','학교'),
    ('친구','친구'),
    ('가족','가족'),
    ('기타','기타'),
)

class Address(models.Model):
    # address_title = models.CharField(max_length=50, choices=address_name_choices, unique=True)
    recipient = models.CharField(max_length=50, null=False)
    phone_1 = models.CharField(max_length=50, null=False)
    phone_2 = models.CharField(max_length=50, null=True, blank=True, default="")
    email = models.CharField(max_length=50, null=True, default="")
    postcode = models.CharField(max_length=50, null=False)
    doromeong_address = models.CharField(max_length=200,null=False)
    detail_address = models.CharField(max_length=200)
    extra_address = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def full_address(self):
        return f'{self.postcode} {self.doromeong_address} {self.detail_address}'

