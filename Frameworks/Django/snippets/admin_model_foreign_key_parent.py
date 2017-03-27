"""
Impliments a Admin Page for a concrete style class (without being concrete).

Unlike concrete inheritance in django models it does not automatically prefetch the parents data
This is useful when you have a structure of a similar type that you will want to get a large set of.
If you want to get everything in one request:
    `Class.objects.select_related('landingpage').get(pk=16)`
"""
from django.contrib import admin
from django import forms

from hubble.admin import BaseAdmin
from landingpages.models import LandingPage

class LandingPageForm(forms.ModelForm):

    c_name = forms.CharField(label='Name')
    c_url = forms.CharField(label='Url')
    c_title = forms.CharField(label='Page Title')
    c_meta_title = forms.CharField(label='Meta Title')
    c_meta_desc = forms.CharField(
        label='Meta Description',
        widget=forms.Textarea(attrs={'rows': 10})
        )

    def get_core_fields(self):
        return [k for k, v in self.fields.items() if k[:2] == 'c_']

    def get_core_data(self):
        fields = self.get_core_fields()
        return {k[2:]: v for k, v in self.cleaned_data.items() if k in fields}


class LandingPageAdmin(BaseAdmin):
    pagetype = None

    def get_form(self, request, obj=None, **kwargs):
        """
        Gets the form, and then adds on our core fields
        """
        form = super(LandingPageAdmin, self).get_form(request, obj, **kwargs)
        return self.get_core_form(obj, form)


    def get_core_form(self, obj, form):
        """
        Gets the fields from the form class, adds the core fields details to the form
        """
        if obj is None:
            return form

        fields = [k[2:] for k in form.base_fields.keys() if k[:2] == 'c_']
        for field in fields:
            form.base_fields['c_' + field].initial = getattr(obj.landingpage, field)
        return form


    def save_core_model(self, form, user):
        """
        Saves the core landingpage data
        """
        c_data = form.get_core_data()
        c_data = dict(user, {'author': user, 'pagetype': self.pagetype})
        # DOES NOT IMPLEMENT UPDATE!
        landing_page = LandingPage(**c_data)
        landing_page.save()
        return landing_page

    def save_model(self, request, obj, form, change):
        """
        Saves the core page model and links the new landingpage obj
        """
        landing_page = self.save_core_model(form, request.user)
        obj.landingpage = landing_page
        super(LandingPageAdmin, self).save_model(request, obj, form, change)





