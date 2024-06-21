from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import ImageText
from .serializers import ImageTextSerializer
from django.core.files.storage import default_storage
from .utils import extract_text_from_image




class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request, *args, **kwargs):
        file_obj = request.data['file']
        file_name = default_storage.save(file_obj.name, file_obj)
        text, bold_words, img_base64 = extract_text_from_image(file_name)
        
        image_text = ImageText.objects.create(
            image=file_obj,
            extracted_text=text,
            bold_words=", ".join(bold_words),
            image_base64=img_base64
        )
        
        serializer = ImageTextSerializer(image_text)
        return Response(serializer.data)

class ImageTextListView(APIView):
    def get(self, request, *args, **kwargs):
        images = ImageText.objects.all()
        serializer = ImageTextSerializer(images, many=True)
        return Response(serializer.data)