from datetime import date, datetime
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import BloggerListSerializer, TourListSerializer
from .models import Blogger, Tour

"""
todo:
login
logout

create_blogger
update_blogger
delete_blogger

"""


class BloggerListAPI(APIView):

    def get(self, request, *args, **kwargs):
        bloggers = Blogger.objects.filter()

        serializer = BloggerListSerializer(bloggers, many=True)

        return Response(serializer.data)

        # data = {
        #     "bloggers": [
        #         {
        #             "blogger_id": 1,
        #             "user_data": {
        #                 'id': 12,
        #                 'username': '',
        #                 'first_name': '',
        #                 'last_name': ''
        #             },
        #             "username": "MisterIvanov67",
        #             "first_name": "Ivanov",
        #             "last_name": "Ivanov",
        #             "email": "some@email.com",
        #             "tel": "+78002223523",
        #             "avatar": "media/avatars/...",
        #             "gender": 'm'|'w',
        #             "is_archive": True, 
        #             "social_networks": {
        #                 "facebook": {
        #                 "link": "facebook.com/ivan",
        #                 "subscribers": 34
        #                 },
        #                 "instagram": {
        #                 "link": "instagram.com/ivan",
        #                 "subscribers": 378,
        #                 "posts": 343
        #                 },
        #             }                
        #         },
        #         ...
        #     ]
        # }


    # def post(self, request, *args, **kwargs):
    #     """
    #     Request for creating new bloggers (searching new bloggers and put that in the db)
    #     """

    #     return Response({"testCreate": "ok"})


    def put(self, request, *args, **kwargs):
        """
        Updating the blogger (for exmaple: ban)
        """

        return Response({"testUpdate": "ok"})


class BanBlogger(APIView):
    def patch(self, request, *args, **kwargs):
        return Response({"testUpdate": "ok"})


class SearchNewBloggers(APIView):
    def get(self, request, *args, **kwargs):
        ...


class BloggerDetailAPI(APIView):
    def get(self, request, *args, **kwargs):
        """
        get one of the bloggers
        """
        return Response()


    def put(self, request, *args, **kwargs):
        """
        update blogger data
        """
        return Response({"args": args, "kwargs": kwargs})


class TourListAPI(APIView):
    def get(self, request, *args, **kwargs):
        """
        kwargs = {
            'from': >=0,
            'to': >=0
        }
        """
        tours = Tour.objects.all()[kwargs['from']:kwargs['to']]
        serialiser = TourListSerializer(tours, many=True)        
        return Response(serialiser.data)
    

class TourDetailAPI(APIView):
    def get(self, request, *args, **kwargs):
        """get points and all data of the tour"""

        data = {}
        return Response(data)


    def post(self, request, *args, **kwargs):
        """
        create new Tour
        change all data of the tour
        * add points
        * delete points
        launch when we click 'save' bottom
        """
        data = {}
        return Response(data)


    def put(self, request, *args, **kwargs):
        """update tour data, including points"""
        data = {}
        return Response(data)
