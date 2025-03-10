"""
Provide GraphQL interface over data on local DB.
Create test that can .
"""
import sqlite3

import strawberry
import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()


@strawberry.type
class User:
    id: int
    name: str
    email: str


@strawberry.type
class Query:
    @strawberry.field
    def get_users(self) -> list[User]:
        cursor.execute("SELECT * FROM `user`")
        res = []
        for user in cursor.fetchall():
            res.append(User(id=user[0], name=user[1], email=user[2]))

        return res


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, id: int, name: str, email: str) -> User:
        cursor.execute("INSERT INTO `user` (id, name, email) VALUES (?, ?, ?) ", (id, name, email))
        connection.commit()
        return User(id=id, name=name, email=email)


def init_db():
    cursor.execute("CREATE TABLE `user` (id INTEGER PRIMARY KEY, name STRING, email STRING)")
    cursor.executemany("INSERT INTO `user` (name, email) VALUES (?, ?)", [
        ("John Doe", "jon@doe.com"),
        ("Jane Doe", "jane@doe.com"),
        ("Jan Doe", "jan@doe.com"),
    ])

    connection.commit()


init_db()
schema = strawberry.Schema(query=Query, mutation=Mutation)
app = FastAPI()

graphql_router = GraphQLRouter(schema)
app.include_router(graphql_router, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run("training:app", host="127.0.0.1", port=8000, reload=True)

"""
Visit: http://127.0.0.1:8000/graphql
Try
```
    query {
      getUsers {
        id
        name
        email
      }
    }
```
"""
