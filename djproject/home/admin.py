from django.contrib import admin
from home.models import (
    CasesRecord,
    ComplainReg,
    CriminalRecord,
    Designations,
    PrisonerRecord,
    SuspectRecord,
    Work_force,
)

admin.site.register(ComplainReg)
admin.site.register(PrisonerRecord)
admin.site.register(SuspectRecord)
admin.site.register(Work_force)
admin.site.register(CriminalRecord)
admin.site.register(CasesRecord)
admin.site.register(Designations)
