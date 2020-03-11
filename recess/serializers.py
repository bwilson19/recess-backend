from rest_framework import serializers
from .models import Game, League, UserProfile, Post, Comment
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User


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


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')
