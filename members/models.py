from django.db import models
from django.contrib.auth.models import User
from projects.models import UserProjects

"""
"
" Licensed under what is outlined in LICENSE in the application root 
" Purpose - To define the replationships for a hackerspace user
"
"""

class MemberInterests(models.Model):
    '''
    used to track what hackers are interested in
    '''
    name = models.CharField(max_length=32,unique=True,help_text="Name of this interest")
    notes = models.TextField(null=True,blank=True,help_text="Optional Notes")

class MemberLevel(models.Model):
    '''
    used to define member levels for various users
    '''
    name = models.CharField(max_length=64, unique=True, help_text="Membership Level Name")
    fee = models.PositiveIntegerField(help_text="fee for this level of membership")
    notes = models.TextField(null=True, blank=True, help_text="Optional Notes")

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    '''
    extending the default User model
    '''

    user = models.OneToOneField(User)
    account_number = models.CharField(max_length=16, help_text="unique number for each member")
    is_active = models.BooleanField(default=True, help_text="whether or not you are active within the space currently")
    level = models.ForeignKey(MemberLevel, unique_for_month="membership_change_date")
    membership_change_date = models.DateField(auto_now=True, help_text="you can chanage your membership type once each calendar month")
    projects = models.ManyToManyField(UserProjects)
    interests = models.ManyToManyField(MemberInterests)
    rsa_key = models.TextField(null=True, blank=True, help_text="optional RSA Public Key")
    pgp_key = models.TextField(null=True, blank=True, help_text="optional PGP Key")
    avatar = models.ImageField(null=True, blank=True, help_text="optional avatar (jpg,gif,png)")
    
    def __unicode__(self):
        return str(self.user)
