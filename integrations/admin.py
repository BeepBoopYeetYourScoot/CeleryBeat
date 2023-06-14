from django.contrib import admin

from integrations.models import Offer, ProductOffer, ProductOfferPrice, \
    ProductOfferAvailabilities, ProductOfferQuantities


class MultiDBModelAdmin(admin.ModelAdmin):
    using = None

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(
            db_field, request, using=self.using, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(
            db_field, request, using=self.using, **kwargs
        )


class M2ModelAdmin(MultiDBModelAdmin):
    using = 'm2'


class RMModelAdmin(MultiDBModelAdmin):
    using = 'rm'


admin.site.register(Offer, M2ModelAdmin)
admin.site.register(ProductOffer, RMModelAdmin)
admin.site.register(ProductOfferAvailabilities, RMModelAdmin)
admin.site.register(ProductOfferPrice, RMModelAdmin)
admin.site.register(ProductOfferQuantities, RMModelAdmin)
