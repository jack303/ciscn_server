from rest_framework import serializers
from tutorial import models


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=models.LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=models.STYLE_CHOICES, default='friendly')

    # the method create and update is acquiescently not implemented
    def create(self, validated_data):
        """
            Create and return a new `Snippet` instance, 
            given the validated data.
        """

        #### add ** to invoke the create function
        return models.Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance,
        given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

