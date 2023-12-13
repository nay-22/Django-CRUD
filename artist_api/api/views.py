import os
import boto3
from openai import OpenAI
from decouple import config
from rest_framework import generics, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Artist, Work, User
from rest_framework.parsers import MultiPartParser
from .serializers import ArtistSerializer, WorkSerializer, UserSerializer, WorkSerializerNew


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArtistListView(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class WorkCreateView(generics.CreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Work.objects.all()
    serializer_class = WorkSerializerNew
    def perform_create(self, serializer):
        artist_id = self.request.data.get('artist')
        try:
            artist = Artist.objects.get(pk=artist_id)
        except Artist.DoesNotExist:
            raise serializer.ValidationError(f"Artist with id {artist_id} does not exist.")
        serializer.save()
        artist.works.add(serializer.instance)
        

class WorkListView(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WorkSerializer
    def get_queryset(self):
        work_type = self.request.query_params.get('work_type', None)
        artist = self.request.query_params.get('artist', None)
        if work_type:
            return Work.objects.filter(work_type=work_type)
        if artist:
            return Work.objects.all().filter(artist__name=artist)
        return Work.objects.all()
    
def generate_product_details(product_title):
    openai_api_key = config('OPENAI_API_KEY')
    os.environ["OPENAI_API_KEY"] = openai_api_key
    client = OpenAI()
    description_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user", 
                "content": f"Create a detailed product description of '{product_title}' in 50 words."
            }
        ]
    )
    product_description = description_completion.choices[0].message.content.strip()
    keyword_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user", 
                "content": f"Extract the important keywords from the following description, '{product_description}'."
            }
        ]
    )
    keywords = keyword_completion.choices[0].message.content.strip()
    return product_description, [keyword.strip() for keyword in keywords.split(',')]

class ProductDescriptionView(APIView):
    def post(self, request, *args, **kwargs):
        product_title = request.data.get('product_title', '')
        if not product_title:
            return Response({'error': 'Product title is required.'}, status=status.HTTP_400_BAD_REQUEST)
        product_description, keywords = generate_product_details(product_title)
        response_data = {
            'product_description': product_description,
            'product_keywords': keywords,
        }
        return Response(response_data, status=status.HTTP_200_OK)

def extract_text(img_path):
    region_name = 'ap-south-1'
    rekognition = boto3.client('rekognition', region_name=region_name)
    with open(img_path, 'rb') as image_file:
        image_data = image_file.read()
    response = rekognition.detect_text(Image={'Bytes': image_data})
    detected_texts = [text['DetectedText'] for text in response.get('TextDetections', [])]
    return detected_texts    

class ImageTextExtractionView(APIView):
    parser_classes = [MultiPartParser]
    def post(self, request, *args, **kwargs):
        if 'image' not in request.FILES:
            return Response({'error': 'Image file is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        img = request.FILES['image']
        img_path = os.path.join('images', img.name)
        with open(img_path, 'wb') as f:
            for chunk in img.chunks():
                f.write(chunk)
        
        texts = extract_text(img_path)
        response_data = {
            "texts": texts
        }
        return Response(response_data, status=status.HTTP_200_OK)



