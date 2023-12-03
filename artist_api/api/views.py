# artists/views.py
from rest_framework import generics, authentication, permissions
from .models import Artist, Work, User
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





















# class WorkListCreateView(generics.ListCreateAPIView):
#     queryset = Work.objects.all()
#     serializer_class = WorkSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [authentication.TokenAuthentication]

#     def perform_create(self, serializer):
#         serializer.save()

# class ArtistListView(generics.ListAPIView):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [authentication.TokenAuthentication]

# class ArtistCreateView(generics.CreateAPIView):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [authentication.TokenAuthentication]

#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user=user)

# class ArtistDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [authentication.TokenAuthentication]

#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)
