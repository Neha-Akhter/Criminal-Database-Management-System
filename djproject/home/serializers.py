import serializers
from home.models import ComplainReg


class complainserializer(serializers.ModelSerializer):
    class meta:
        models = ComplainReg
        fields = ('complain_id', 'complainee_fname',
                  'complainee_lname', 'complainee_DOB', 'dateofcomplain', 'timeofcomplain', 'complainee_cnic', 'complainee_contactno', 'FIR_status', 'crime_description', 'victim_description', 'email_address')
