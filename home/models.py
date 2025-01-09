from django.db import models

from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel ,InlinePanel
# models.py
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField
class Event(Orderable):  # Inheriting from Orderable for sorting
    page = ParentalKey('home.HomePage', related_name='events', on_delete=models.CASCADE) # Relate to HomePage
    date = models.DateField("Event Date")
    title = models.CharField(max_length=255)
    description = RichTextField(blank=True)  # Optional description field
    panels = [
        FieldPanel('date'),
        FieldPanel('title'),
        FieldPanel('description'),  # Include if you added the description field
    ]

    def __str__(self):
        return self.title
class HomePage(Page):
    lead_text = models.TextField(
    max_length=1000, 
    blank=True,
    help_text="This text will appear in bold on the home page",
    )
    button=models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Select an optional page to link to",
    )
    button_text=models.CharField(
        max_length=50,
        default="Read more",
        blank=False,
        help_text="Text to display on the button. Max length is 50 characters",
    )
    banner_background_image=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The banner background image",
    )
    banner_background_image1=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The banner background image",
    )
    banner_background_image2=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The banner background image",
    )
    banner_background_image3=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The banner background image",
    )
    banner_background_image4=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The banner background image",
    )
    banner_background_image5=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The banner background image",
    )
    banner_background_image6=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The banner background image",
    )
    banner_background_image7=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The banner background image",
    )
    banner_background_image8=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The banner background image",
    )
    banner_background_image9=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The banner background image",
    )
    banner_background_image10=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The banner background image",
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('lead_text'),
        FieldPanel('button'),
        FieldPanel('button_text'),
        FieldPanel('banner_background_image'),
        FieldPanel('banner_background_image1'),
        FieldPanel('banner_background_image2'),
        FieldPanel('banner_background_image3'),
        FieldPanel('banner_background_image4'),
        FieldPanel('banner_background_image5'),
        FieldPanel('banner_background_image6'),
        FieldPanel('banner_background_image7'),
        FieldPanel('banner_background_image8'),
        FieldPanel('banner_background_image9'),
        FieldPanel('banner_background_image10'),
        InlinePanel('events', label="Events"),
    ]
    
