from django_filters import rest_framework as filters

from .models import Question, QuestionTag


class QuestionFilter(filters.FilterSet):
    tag = filters.ModelMultipleChoiceFilter(
        field_name="tags__slug",
        queryset=QuestionTag.objects.all(),
        to_field_name="slug",
    )

    class Meta:
        model = Question
        fields = ["tags"]
