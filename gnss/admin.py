from django.contrib import admin
from gnss.models import *

# Register your models here.
admin.site.register(GPS_data)
admin.site.register(Biedou_data)
admin.site.register(GALILEO_data)
admin.site.register(GLONASS_data)
admin.site.register(IRNSS_data)