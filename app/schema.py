import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation

from .models import Dummy
from .serializers import DummySerializer


class DummyType(DjangoObjectType):
    class Meta:
        model = Dummy
        fields = ("id", "foo")


class DummyMutation(SerializerMutation):
    class Meta:
        serializer_class = DummySerializer


class Query(graphene.ObjectType):
    all_dummies = graphene.List(DummyType)

    def resolve_all_dummies(root, info):
        return Dummy.objects.all()


class Mutation(graphene.ObjectType):
    dummy_mutation = DummyMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
