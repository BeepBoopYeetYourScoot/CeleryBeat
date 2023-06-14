from django.contrib import admin

from counter.models import ComparisonResult, M2ComparisonResult, \
    RMComparisonResult

admin.site.register(ComparisonResult)
admin.site.register(M2ComparisonResult)
admin.site.register(RMComparisonResult)
