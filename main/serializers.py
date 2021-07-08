from rest_framework import serializers

from entertainment.models import Article
from entertainment.serializers import MovieSerializer, VideoSerializer
from main.models import Main
from places.serializers import PlaceSerializer
from questions.serializers import QuestionSerializer
from story.models import Story


class ArticleMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "color"]


class StoryMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ["title", "image"]


class MainSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    questions = QuestionSerializer(many=True)
    articles = ArticleMainSerializer(many=True)
    movies = MovieSerializer(many=True)
    history = StoryMainSerializer()
    video = VideoSerializer()

    class Meta:
        model = Main
        fields = [
            "place",
            "questions",
            "articles",
            "movies",
            "history",
            "video",
        ]
