from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from modelcluster.fields import ParentalManyToManyField
from wagtail.snippets.models import register_snippet

@register_snippet
class ServiceCategory(models.Model):
  name = models.CharField(max_length=255)
  panels = [
      FieldPanel('name'),
  ]

  def __str__(self):
      return self.name


class ServiceListingPage(Page):
    subtitle = models.CharField(max_length=255, blank=True)
    content_panels=Page.content_panels + [
        FieldPanel("subtitle"),
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Organize services by category for the template

        services_by_category = {}
        for service in ServicePage.objects.live().public(): # Or filter how you need
            category = service.bottom_text  # Changed to bottom_text
            if category not in services_by_category:
                services_by_category[category] = []
            services_by_category[category].append(service)


        context["services_by_category"] = services_by_category
        return context


class ServicePage(Page):
    description=models.TextField(blank=True,max_length=255)
    internal_page=models.ForeignKey('wagtailcore.Page',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    external_page=models.URLField(blank=True)
    bottom_text=models.TextField(max_length=255,blank=True,help_text="BOOKS,BOOKS CHAPTERS,RESEARCH PUBLICATIONS (PEER-REVIEWED JOURNALS)")
    service_image=models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    service_image1=models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    service_image2=models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    service_image3=models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    description1=models.TextField(blank=True,max_length=255)
    description2=models.TextField(blank=True,max_length=255)
    description3=models.TextField(blank=True,max_length=255)
    content_panels=Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("internal_page"),
        FieldPanel("external_page"),
        FieldPanel("bottom_text"),
        FieldPanel("service_image"),
        FieldPanel("service_image1"),
        FieldPanel("service_image2"),
        FieldPanel("service_image3"),
        FieldPanel("description1"),
        FieldPanel("description2"),
        FieldPanel("description3"),
        
    ]
class ServiceIndexPage(Page):
    
    description=models.TextField(blank=True,max_length=255)
    internal_page=models.ForeignKey('wagtailcore.Page',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    external_page=models.URLField(blank=True)
    bottom_text=models.TextField(max_length=255,blank=True)
    service_image=models.ForeignKey('wagtailimages.Image',null=True,blank=False,on_delete=models.SET_NULL,related_name='+')
    content_panels=Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("internal_page"),
        FieldPanel("external_page"),
        FieldPanel("bottom_text"),
        FieldPanel("service_image"),
 
        
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Organize services by category for the template

        services_by_category = {}
        for service in ServiceCollectionsPage.objects.live().public(): # Or filter how you need
            category = service.bottom_text  # Changed to bottom_text
            if category not in services_by_category:
                services_by_category[category] = []
            services_by_category[category].append(service)


        context["services_by_category"] = services_by_category
        return context

class ServiceCollectionsPage(Page):
    category = models.ForeignKey('services.ServiceCategory', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    description=models.TextField(blank=True,max_length=255)
    internal_page=models.ForeignKey('wagtailcore.Page',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    external_page=models.URLField(blank=True)
    bottom_text=models.TextField(max_length=255,blank=True,help_text="CHALLENGES ORGANIZED||International Events (Participation and Attended)||NATIONAL / INTERNATIONAL CONFERENCES||KEY NOTE ADDRESSES –NATIONAL / INTERNATIONAL CONFERENCES||TECHNICAL TALKS||SEMINAR, CONFERENCE, WORKSHOP ORGANISED||SEMINAR, WORKSHOP ATTENDED in TLP||SEMINAR, CONFERENCE, WORKSHOP ATTENDED in CORE AREA||SPONSORED Conferences/ STTP/ FDPs")
    service_image=models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    service_image1=models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    service_image2=models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    service_image3=models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    description1=models.TextField(blank=True,max_length=255)
    description2=models.TextField(blank=True,max_length=255)
    description3=models.TextField(blank=True,max_length=255)
    content_panels=Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("internal_page"),
        FieldPanel("external_page"),
        FieldPanel("bottom_text"),
        FieldPanel("service_image"),
        FieldPanel("service_image1"),
        FieldPanel("service_image2"),
        FieldPanel("service_image3"),
        FieldPanel("description1"),
        FieldPanel("description2"),
        FieldPanel("description3"),
        
    ]
class ServiceIndividualPage(Page):
    description=models.TextField(blank=True,max_length=255)
    internal_page=models.ForeignKey('wagtailcore.Page',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    external_page=models.URLField(blank=True)
    bottom_text=models.TextField(max_length=255,blank=True)
    service_image=models.ForeignKey('wagtailimages.Image',null=True,blank=False,on_delete=models.SET_NULL,related_name='+')
    services = ParentalManyToManyField("services.ServicePage", blank=True, related_name="service_index_pages")
    
    content_panels=Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("internal_page"),
        FieldPanel("external_page"),
        FieldPanel("bottom_text"),
        FieldPanel("service_image"),
        
        
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Organize services by category for the template

        services_by_category = {}
        for service in ServiceSeparatePage.objects.live().public(): # Or filter how you need
            category = service.bottom_text  # Changed to bottom_text
            if category not in services_by_category:
                services_by_category[category] = []
            services_by_category[category].append(service)


        context["services_by_category"] = services_by_category
        return context
class ServiceSeparatePage(Page):
    description=models.TextField(blank=True,max_length=255)
    internal_page=models.ForeignKey('wagtailcore.Page',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    external_page=models.URLField(blank=True)
    bottom_text=models.TextField(max_length=255,blank=True,help_text="FACULTY INTERSHIP||CONSULTANCY PROJECT||MOOC DEVELOPMENT||CERTIFICATE||ACHIEVEMENTS")
    service_image=models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    service_image1=models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    service_image2=models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    service_image3=models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    description1=models.TextField(blank=True,max_length=255)
    description2=models.TextField(blank=True,max_length=255)
    description3=models.TextField(blank=True,max_length=255)
    content_panels=Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("internal_page"),
        FieldPanel("external_page"),
        FieldPanel("bottom_text"),
        FieldPanel("service_image"),
        FieldPanel("service_image1"),
        FieldPanel("service_image2"),
        FieldPanel("service_image3"),
        FieldPanel("description1"),
        FieldPanel("description2"),
        FieldPanel("description3"),
    ]

