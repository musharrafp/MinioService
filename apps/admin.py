from django.contrib import admin
from apps.models import Document


@admin.register(Document)
class DocumentModelAdmin(admin.ModelAdmin):
    change_form_template = 'apps/view.html'
    list_display = ('name',)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context['image_url'] = Document.objects.get(pk=object_id).picture.url.replace('minio', 'localhost', 1)
        extra_context['file_url'] = Document.objects.get(pk=object_id).pdf.url.replace('minio', 'localhost', 1)
        return super().change_view(request, object_id, form_url, extra_context)
