from rest_framework import generics, status


from bugs.models import Bug, Comment
from bugs.serializers import BugsModelSerializer, \
    CommentModelSerializer


class BugCreateView(generics.CreateAPIView):
    serializer_class = BugsModelSerializer
    queryset = Bug


class BugsListView(generics.ListAPIView):
    serializer_class = BugsModelSerializer
    queryset = Bug

    def get_queryset(self):
        return self.queryset.objects.all()


class BugDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BugsModelSerializer
    lookup_url_kwarg = 'id'
    queryset = Bug


class ResolvedBugsListView(generics.ListAPIView):
    serializer_class = BugsModelSerializer
    queryset = Bug

    def get_queryset(self):
        return self.queryset.objects.filter(status="resolved")


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentModelSerializer
    queryset = Comment


class CommentsListView(generics.ListAPIView):
    serializer_class = CommentModelSerializer
    queryset = Comment


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentModelSerializer
    lookup_url_kwarg = 'id'
    queryset = Comment
