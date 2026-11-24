from ariadne import QueryType, make_executable_schema

from app.resolvers import resolve_current_user, resolve_my_tasks


type_defs = """
    type User {
        id: Int!
        username: String!
    }

    type Task {
        id: Int!
        title: String!
    }

    type Query {
        currentUser: User!
        myTasks: [Task!]!
    }
"""

# QueryType connects GraphQL queries to Python functions.
query = QueryType()

query.set_field("currentUser", resolve_current_user)
query.set_field("myTasks", resolve_my_tasks)

schema = make_executable_schema(type_defs, query)