from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


def index(request):
    return render(request, "index.html", {})


class BloggerAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = [
            {"id": 1, "name": "John"},
            {"id": 2, "name": "John2"}
        ]

        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"test": "hello"})

    def put(self, request, *args, **kwargs):
        return Response({"testPut": "ok"})
