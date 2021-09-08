from datetime import date, datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from .serializers import BloggerDetailSerializer, BloggerListSerializer, TourDetailSerializer, TourListSerializer
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
    DEFAULT_BLOGGER_LIMIT = 10

    available_filters = {
        'name_contains': lambda val: Q(
                Q(first_name__contains=val['name_contains']) | \
                Q(last_name__contains=val['name_contains'])
            ),
        'username_contains': lambda val: Q(username__contains=val['username_contains']),
        'regestered': lambda val: Q(user__isnull=val['regestered']),
        'gender': lambda val: Q(gender__iexact=val['gender']),
        'location': lambda val: Q(locations__icontains=val['location']),
        'is_archive': lambda val: Q(is_archive=val['is_archive']),        
        'job': lambda val: Q(job__title__iexact=val['job']),
        'tour_participant': lambda val: Q(tours__pk=val['tour_participant']),
        'age_gt': lambda val: Q(age__gt=val['age_gt']), 
        'age_lt': lambda val: Q(age__gt=val['age_lt']),
        'success_tours_gt': lambda val: Q(count_success_tours__gt=val['age_gt']),
        'success_tours_lt': lambda val: Q(count_success_tours__lt=val['age_lt']),
    }

    def get_blogger_filters(self, kwargs:dict):
        filters = Q()

        for filter_key in kwargs:
            if filter_key in self.available_filters:
                filters &= self.available_filters[filter_key](kwargs)

        return filters
        # filters = \
            # Q(
            #     Q(first_name__contains=kwargs['name_contains']) | \
            #     Q(last_name__contains=kwargs['name_contains'])
            # ) & \
            # Q(username__contains=kwargs['username_contains']) & \
            # Q(user__isnull=kwargs['regestered']) & \
            # Q(gender__iexact=kwargs['gender']) & \
            # Q(locations__icontains=kwargs['location']) & \
            # Q(age__range=(kwargs['age_gt'], kwargs['age_lt'])) & \
            # Q(is_archive=kwargs['is_archive']) & \
            # Q(count_success_tours__gt=kwargs['success_tours_gt']) & \
            # Q(count_success_tours__lt=kwargs['success_tours_lt']) & \
            # Q(job__title__iexact=kwargs['job'])
            

        return filters
    

    def get(self, request, *args, **kwargs):
        """
        kwargs = {
            'from': Int(>=0),
            'to': Int(>=0),
            'registered': bool,
            'username_contains': str,
            'name_contains': str,
            'gender': Str('m'|'f'),
            ''
        }
        """

        if 'from' not in kwargs:
            kwargs['from'] = 0

        if 'to' not in kwargs:
            kwargs['to'] = kwargs['from'] + self.DEFAULT_BLOGGER_LIMIT

        blogger_filters = self.get_blogger_filters(kwargs)

        if blogger_filters:
            bloggers = Blogger.objects.filter(blogger_filters)[kwargs['from']:kwargs['to']]
        else:
            bloggers = Blogger.objects.all()[kwargs['from']:kwargs['to']]
        
        serializer = BloggerListSerializer(bloggers, many=True) # todo: get user_data 
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
        #                     "link": "facebook.com/ivan",
        #                     "subscribers": 34
        #                 },
        #                 "instagram": {
        #                     "link": "instagram.com/ivan",
        #                     "subscribers": 378,
        #                     "posts": 343
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


class ToggleBanAPI(APIView):
    def patch(self, request, *args, **kwargs):
        return Response({"Banned": True})


class SearchNewBloggersAPI(APIView):
    def get(self, request, *args, **kwargs):
        """
        Request for creating new bloggers (searching new bloggers and put that in the db)
        """
        return Response({"testSearchBloggers": "ok"})


class BloggerDetailAPI(APIView):
    def get(self, request, blogger_id, *args, **kwargs):
        """
        get one of the bloggers
        """
        blogger = Blogger.objects.get(pk=blogger_id)
        serializer = BloggerDetailSerializer(blogger)
        return Response(serializer.data)


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
    def get(self, request, tour_id, *args, **kwargs):
        """get points and all data of the tour"""

        tour = Tour.objects.get(pk=tour_id)
        serializer = TourDetailSerializer(tour)
        return Response(serializer.data)


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
