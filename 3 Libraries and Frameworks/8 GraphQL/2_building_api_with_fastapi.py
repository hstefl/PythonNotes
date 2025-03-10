from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry

# Define a simple GraphQL type
@strawberry.type
class Book:
    title: str
    author: str

# Define a Query schema
@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> list[Book]:
        return [
            Book(title="1984", author="George Orwell"),
            Book(title="Brave New World", author="Aldous Huxley")
        ]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        return Book(title=title, author=author)


# Create a Strawberry schema
schema = strawberry.Schema(query=Query, mutation=Mutation)

# Set up FastAPI
app = FastAPI()

# Mount the GraphQL router
graphql_router = GraphQLRouter(schema)
app.include_router(graphql_router, prefix="/graphql")

