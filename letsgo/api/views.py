from datetime import date, datetime
from rest_framework.views import APIView
from rest_framework.response import Response


class BloggerListAPI(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "bloggers": [
                {
                    "id": 1,
                    "login": "MisterIvanov67",
                    "name": "Ivanov",
                    "lastname": "Ivanov",
                    "email": "some@email.com",
                    "tel": "+78002223523",
                    "avatar": "media/avatars/...",
                    "gender": 'm'|'w',
                    "is_archive": True, 
                    "social_networks": {
                        "facebook": {
                        "link": "facebook.com/ivan",
                        "subscribers": 34
                        },
                        "instagram": {
                        "link": "instagram.com/ivan",
                        "subscribers": 378,
                        "posts": 343
                        },
                    }                
                },
                {
                    "id": 2,
                    "login": "MisterIvanov2",
                    "name": "Ivanov",
                    "lastname": "Ivanov",
                    "email": "some@email.com",
                    "tel": "+78002223523",
                    "avatar": "media/avatars/...",
                    "gender": 'm'|'w',
                    "is_archive": True,
                    "social_networks": {
                        "facebook": {
                        "link": "facebook.com/ivan",
                        "subscribers": 34
                        },
                        "instagram": {
                        "link": "instagram.com/ivan",
                        "subscribers": 378,
                        "posts": 343
                        },
                    }
                },
            ]
        }

        data = [
            {"id": 1, "name": "John"},
            {"id": 2, "name": "John2"}
        ]

        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"test": "hello"})

    def put(self, request, *args, **kwargs):
        return Response({"testPut": "ok"})


class BloggerDetailAPI(APIView):
    def get(self, request, *args, **kwargs):


        data = {
            "id": 2,
            "login": "MisterIvanov2",
            "name": "Ivanov",
            "lastname": "Ivanov",
            "email": "some@email.com",
            "tel": "+78002223523",
            "avatar": "media/avatars/...",
            "gender": 'm', # m or w
            "is_archive": True,
            "social": "СМИ", # "instagram" or 
            "social_networks": {
                "facebook": {
                "link": "facebook.com/ivan",
                "subscribers": 34
                },
                "instagram": {
                "link": "instagram.com/ivan",
                "subscribers": 378,
                "posts": 343
                },
            }
        }
        return Response()

    def post(self, request, *args, **kwargs):
        return Response({"args": args, "kwargs": kwargs})


class TourListAPI(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "start": 1,
            "end": 10, 
            "tours": [
                {
                    "title": "Путешествие в прошлое",
                    "address": "Самарская область, деревня Власово",
                    "points": "Программа: 08:00 – отправление; " * 10,
                    "short_description": "гончарное мастерство и знакомство с крестьянским бытом" * 10,
                    "date": datetime.date(2021, 12, 14).strftime("Y%:%m:%d"),
                },
                {
                    "title": "Путешествие в прошлое",
                    "address": "Самарская область, деревня Власово",
                    "points": "Программа: 08:00 – отправление; " * 10,
                    "short_description": "гончарное мастерство и знакомство с крестьянским бытом" * 10,
                    "date": datetime.date(2022, 1, 17).strftime("Y%:%m:%d"),
                },
            ]
        }

        return Response(data)


    def post(self, request, *args, **kwargs):
        """create new tour"""


    def put(self, request, *args, **kwargs):
        """change put data"""



class TourPointAPI(APIView):
    def post(self, request, *args, **kwargs):
        """add new point into the tour"""


    def put(self, request, *args, **kwargs):
        """update point of the tour"""


class TourDetailAPI(APIView):
    def get(self, request, *args, **kwargs):
        """get points and all data of the tour"""


    def post(self, request, *args, **kwargs):
        """
        change all data of the tour
        * add points
        * delete points
        launch when we click 'save' bottom
        """

        return Response()
