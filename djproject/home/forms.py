from django.db.models import fields, query
from django.forms import ModelForm
from django.forms.models import ModelChoiceField
from .models import (
    CasesRecord,
    ComplainReg,
    CriminalRecord,
    Designations,
    PrisonerRecord,
    SuspectRecord,
    Work_force,
)
from django.core import validators
from django import forms


class complainform(ModelForm):
    class Meta:
        model = ComplainReg
        fields = "__all__"


class caseform(ModelForm):
    def __init__(self, *args, **kwargs):
        super(caseform, self).__init__(*args, **kwargs)
        self.fields["complain_id"] = ModelChoiceField(
            queryset=ComplainReg.objects.filter(FIR_status=1),
            widget=forms.Select(attrs={"class": "complain_id-select"}),
        )

    class Meta:
        model = CasesRecord
        fields = [
            "complain_id",
            "case_id",
            "officer",
            "CrimeScene",
            "Evidence",
            "CaseStatus",
        ]


class criminalform(ModelForm):
    class Meta:
        model = CriminalRecord
        fields = "__all__"


class workforceform(ModelForm):
    class Meta:
        model = Work_force
        fields = "__all__"


class suspectform(ModelForm):
    class Meta:
        model = SuspectRecord
        fields = "__all__"


class prisonerform(ModelForm):
    class Meta:
        model = PrisonerRecord
        fields = "__all__"


class desigform(ModelForm):
    class Meta:
        model = Designations
        fields = "__all__"
