from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_link


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для урока
    """

    video_link = serializers.CharField(validators=[validate_link])

    class Meta:
        model = Lesson
        fields = ("id", "course", "title", "description", "video_link", "owner")


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для курса
    """

    lessons_count = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()
    lessons_list = LessonSerializer(source="lessons", many=True, read_only=True)

    def get_is_subscribed(self, obj):
        return Subscription.objects.filter(
            user=self.context["request"].user, course=obj
        ).exists()

    @staticmethod
    def get_lessons_count(obj):
        return Lesson.objects.filter(course=obj).count()  # Получение количества уроков

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "description",
            "lessons_count",
            "owner",
            "lessons_list",
            "is_subscribed",
        )


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"