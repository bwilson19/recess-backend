from rest_framework import serializers
from .models import Game, League, UserProfile, Post, Comment


class GameSerializer(serializers.HyperlinkedModelSerializer):
    league = serializers.HyperlinkedRelatedField(
        view_name='league_detail',
        read_only=True
    )
    posts = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        many=True,
        read_only=True
    )
    game_url = serializers.ModelSerializer.serializer_url_field(
        view_name='game_detail')

    class Meta:
        model = Game
        fields = ('id', 'game_url', 'name', 'address',
                  'city', 'state', 'zipcode', 'date', 'info', 'image', 'league', 'posts',)


class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(
        view_name='game_detail',
        many=True,
        read_only=True
    )
    league_url = serializers.ModelSerializer.serializer_url_field(
        view_name='league_detail')

    class Meta:
        model = League
        fields = ('id', 'league_url', 'name', 'manager',
                  'city', 'sport', 'rules', 'games')


class UserProfileSerializer(serializers.ModelSerializer):
    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail')

    class Meta:
        model = UserProfile
        fields = ('id', 'user_url', 'name',
                  'bio', 'city', 'image',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.HyperlinkedRelatedField(
        view_name='game_detail',
        read_only=True
    )
    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True
    )
    post_url = serializers.ModelSerializer.serializer_url_field(
        view_name='post_detail')

    class Meta:
        model = Post
        fields = ('id', 'post_url', 'author',
                  'body', 'timestamp', 'game', 'comments')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        read_only=True
    )
    comment_url = serializers.ModelSerializer.serializer_url_field(
        view_name='comment_detail')

    class Meta:
        model = Comment
        fields = ('id', 'comment_url', 'author',
                  'body', 'timestamp', 'post')
