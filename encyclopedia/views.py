# Variables
from random import randint
from turtle import title
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django import forms
from markdown2 import Markdown

from . import util


# Create your views here.
class NewEntryForm(forms.Form):
  title = forms.CharField(
    required=True,
    label="",
    widget=forms.TextInput(
      attrs={"placeholder": "Title", "class": "mb-4"}
    ),
  )
  content = forms.CharField(
    required=True,
    label="",
    widget=forms.Textarea(
      attrs={
        "class": "form-control mb-4",
        "placeholder": "Content (markdown",
        "id": "new_content",
      }
    ),
  )


def index(request):
  return render(
    request, "encyclopedia/index.html", {"entries": util.list_entries()}
  )