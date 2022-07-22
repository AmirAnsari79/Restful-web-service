from rest_framework import serializers


# serializer manual


class StoreSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)


# serializer using model
from api.models import Store, Book


class StoreSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('title', 'city',)  # you can use "__all__"
        # exclude=('address',)
        # read_only_fields=('') no editable


# serialized book fully
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100, allow_null=False, read_only=..., required=..., default=...,
                                  validators=..., error_messages=..., )
    category = serializers.CharField(max_length=50, allow_null=True)
    publisher = serializers.CharField(max_length=100, allow_null=True)
    isbn = serializers.CharField(max_length=15, allow_null=True)
    creator = serializers.CharField(source='creator.username', allow_null=True)

    # this function for validate attrs when post or put
    def validate(self, data):
        if data['title'] not in 'abcdefgi':
            raise serializers.ValidationError('!!!')

    # def save(self, **kwargs):
    #     super(BookSerializer, self).save(**kwargs)
    # we dont need now
    def create(self, validated_data):
        """
        create and return  a new book
        """
        request = self.context.get('request')
        validated_data['creator'] = request.user
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        update and return an existing book

        """
        instance.title = validated_data.get('title', instance.title)
        instance.category = validated_data.get('category', instance.category)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        request = self.context.get('request')
        instance.creator = request.user
        instance.save()
        return instance

        # #         hyperlinkmodelserial with BOOk
# class BookSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name="ketab", lookup_field="id")
#
#     class Meta:
#         model = Book
#         fields = '__all__'
