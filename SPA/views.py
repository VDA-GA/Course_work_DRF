from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from SPA.models import Habit
from SPA.pagination import HabitPagination
from SPA.permissions import IsCreator, ReadOnly
from SPA.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitUserListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublishedListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated & ReadOnly]
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    queryset = Habit.objects.filter(is_published=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated & IsCreator]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated & IsCreator]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated & IsCreator]
    queryset = Habit.objects.all()
