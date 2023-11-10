from django.db import models

class Reports(models.Model):
    id = models.AutoField(primary_key=True)
    marketplace = models.CharField(max_length=255)
    infringing_listing_id = models.CharField(max_length=255)
    scope = models.CharField(max_length=255)
    type_of_infringement = models.CharField(max_length=255)
    complaint_reason = models.CharField(max_length=255)
    ip_owner = models.CharField(max_length=255)
    registration_number = models.IntegerField()
    additional_information = models.TextField()

    class Meta:
        db_table = 'reports'

    def __str__(self):
        return {self.id}, {self.marketplace}, {self.infringing_listing_id}, {self.scope}, {self.type_of_infringement}, {self.complaint_reason}, {self.ip_owner}, {self.registration_number}, {self.additional_information}
