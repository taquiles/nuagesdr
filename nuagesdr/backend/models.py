from django.db import models

class RiskTypesModel(models.Model):
    risk_type_name = models.CharField(max_length=255, blank=False, unique=True, null=True)

class FieldTypesModel(models.Model):
    
    risktype   = models.ForeignKey(RiskTypesModel, related_name='field_info', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255, blank=False, null=True)
    field_type = models.CharField(max_length=10, null=True)    

    class Meta:
        unique_together = ('risktype', 'field_name', 'field_type')
        ordering = ['field_name']

    def __unicode__(self):
        return '%s' % (self.field_name) 
        # , self.field_type)


class EnumFieldTypesModel(models.Model):
    fieldtypes = models.ForeignKey(FieldTypesModel, related_name='enum_value', on_delete=models.CASCADE)
    enum_value = models.CharField(max_length=255, unique=False, null=True)
    
    unique_together = ('fieldtypes', 'enum_value')
    ordering = ['enum_value']
