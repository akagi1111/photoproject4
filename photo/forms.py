# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:44:05 2023

@author: S_akagi
"""

from django.forms import ModelForm
from .models import PhotoPost

class PhotoPostForm(ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['category','title','comment','image1','image2']