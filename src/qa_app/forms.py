"""Forms.py file."""

from django import forms
from .models import Action, UseCase, Project, Jobs, Document
import os
from django.conf import settings


DEFAULT_OPTION = [["", "Select an option"]]


ACTION_CHOICES = [
    ["Click", "Click"],
    ["EnterText", "Enter Text"],
    ["SelectFromDropDown", "Select From Drop Down"],
    ["SelectFromLookUp", "Select From Look Up"],
    ["URL", "URL"],
    ["PAUSE", "PAUSE"],
    ["LOOP", "Loop"],
    ["PRESENCEOFELEMENT", "Presence Of Element"],
    ["GETPAGETITLE", "Get Page Title"],
    ["GETPAGEURL", "Get Page URL"],
    ["NAVIGATEBACK", "Navigate Back"],
    ["HOVERON", "Hoveron"],
    ["ENTERDYNAMICTEXT", "Enter Dynamic Text"],
<<<<<<< Updated upstream
    ["CLEARTEXT","Clear Text"],
    ["GETTEXT","Get Text"],
    ["CLICKONENTER","Click on Enter"],
    ["CLICKONTAB","Click on TAB"],
    ["STOREDATAINVARIABLE","Store Data In Variable"],
    ["GETDATAFROMVARIABLE","Get Data From Variable"],
    ["GETVALUE","Get Element Value"],
    ["DRAGANDDROP","Drag and Drop"],
    ["VERIFYALL","Verify All"],
    ["VERIFYCHECKBOX","Verify Checkbox"],
    ["ISEMPTY", "Is Empty"],
    ["UPLOADFILES", "Upload the files"]
]

LOCATORS_CHOICES = [
    ["ID", "ID"],
    ["NAME", "Name"],
    ["XPATH", "X Path"],
    ["CSSSELECTOR", "CSS Selector"],
    ["LINKTEXT", "Link Text"],
    ["CLASSNAME", "Class Name"],
    ["TAGNAME", "Tag Name"],
    ["PARTIALLINKTEXT", "Partial Link Text"]
]


class ActionsFormset(forms.ModelForm):
    """Actions form."""

    hidden_id = forms.CharField(required=False, widget=forms.HiddenInput())
    seq = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    action = forms.ChoiceField(choices=DEFAULT_OPTION + ACTION_CHOICES, required=False, widget=forms.Select(attrs={'class': 'action_class'}))
    locators = forms.ChoiceField(choices=DEFAULT_OPTION + LOCATORS_CHOICES, required=False)
    upload_files = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'upload-files-class'}))

    class Meta:
        """Meta Data."""

        model = Action
        fields = ['seq', 'description', 'action', 'locators', 'element_identifier', 'element_value', 'upload_files']

    def __init__(self, files_choices=None, *args, **kwargs):
        super(ActionsFormset, self).__init__(*args, **kwargs)
        self.fields['upload_files'] = forms.ChoiceField(choices=files_choices, required=False, widget=forms.Select(attrs={'class': 'upload-files-class'}))


class UsecaseForm(forms.ModelForm):
    """Usecase form."""

    class Meta:
        """Meta Data."""

        model = UseCase
        fields = ['use_case_name', 'use_case_description']


class ProjectForm(forms.ModelForm):
    """ProjectForm."""

    class Meta:
        """Meta class."""

        model = Project
        fields = ['name']


class JobsForm(forms.ModelForm):
    """Jobs form."""

    class Meta:
        """Meta Data."""

        model = Jobs
        fields = ['name']


class DocumentForm(forms.ModelForm):
    """Upload form."""

    class Meta:
        """Meta Data."""

        model = Document
        fields = ['document']
