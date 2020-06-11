__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '11/06/20'

from django.contrib.gis.db import models
from mapserver.models.base import base_model


class HazardEventQueue(base_model):
    """ Model for hazard event queue """
    id = models.BigIntegerField(primary_key=True)
    flood_map_id = models.IntegerField()
    acquisition_date = models.DateTimeField()
    forecast_date = models.DateTimeField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    trigger_status = models.IntegerField(blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    hazard_type_id = models.IntegerField(blank=True, null=True)
    queue_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hazard_event_queue'
