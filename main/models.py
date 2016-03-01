from django.db import models
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

DURATION = (
    ('2', '2 Weeks'),
    ('8', '8 Weeks'),
)

class Course(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 300)
    instructor = models.CharField(max_length = 100)
    course_length = models.CharField(max_length=30, choices=DURATION, default=DURATION[0][0])
    art = models.ImageField(upload_to='uploads/')
