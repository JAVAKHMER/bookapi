from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import Http404
from bookapi.models import Books
from bookapi.serializers import BookSerializer
class BooksAPI(APIView):
    def get(self, request, format=None):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        lret_dic = dict(books=serializer.data)
        return Response(lret_dic, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data.get('book'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookAPI(APIView):
    def get_object(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
