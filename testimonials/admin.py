from django.contrib import admin


from testimonials.models import Testimonial
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'testimonial')
    list_display_links = ('id', 'name')
admin.site.register(Testimonial, TestimonialAdmin)