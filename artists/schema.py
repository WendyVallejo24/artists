import graphene

import artistas.schema


class Query(artistas.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)