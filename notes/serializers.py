from rest_framework import serializers
from .models import Note, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class NoteSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'tags', 'temperature')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        note = Note.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
            note.tags.add(tag)
        return note
