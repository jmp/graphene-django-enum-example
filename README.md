# Graphene-Django Enum Example

This is a minimal sample demonstrating the issue [#1280](https://github.com/graphql-python/graphene-django/issues/1280)
in the [Graphene-Django](https://github.com/graphql-python/graphene-django) project.

Installation:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Generating the GraphQL schema:

    python manage.py graphql_schema --out schema.graphql
