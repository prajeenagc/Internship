from ariadne import (
    QueryType,
    MutationType,
    ObjectType,
    make_executable_schema
)

from app.graphql.resolvers import (
    resolve_create_task,
    resolve_update_task,
    resolve_delete_task
)


type_defs = """

    type Task {
        id: Int!
        title: String!
        state: String!
        ownerId: Int!
    }


    type MutationResult {
        success: Boolean!
        message: String!
        task: Task
        taskId: Int
    }


    type Query {
        hello: String!
    }


    type Mutation {

        createTask(
            title: String!,
            state: String = "pending"
        ): MutationResult!


        updateTask(
            taskId: Int!,
            title: String,
            state: String
        ): MutationResult!


        deleteTask(
            taskId: Int!
        ): MutationResult!

    }

"""


query = QueryType()

mutation = MutationType()

task_type = ObjectType("Task")


@query.field("hello")
def resolve_hello(*_):

    return "Day 23 Shared Services API"


@task_type.field("ownerId")
def resolve_owner_id(obj, *_):

    return obj.owner_id


mutation.set_field(
    "createTask",
    resolve_create_task
)

mutation.set_field(
    "updateTask",
    resolve_update_task
)

mutation.set_field(
    "deleteTask",
    resolve_delete_task
)


schema = make_executable_schema(
    type_defs,
    query,
    mutation,
    task_type
)