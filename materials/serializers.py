from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson
from users.models import User


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("id", "course", "title", "description", "owner")


class CourseSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons_list = LessonSerializer(source="lessons", many=True, read_only=True)

    @staticmethod
    def get_lessons_count(obj):
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "description",
            "lessons_count",
            "owner",
            "lessons_list",
        )