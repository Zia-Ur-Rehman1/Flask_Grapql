from db_utils import create_connection, execute_read_query

from ariadne import (
    ObjectType,
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)

query = ObjectType("Query")


@query.field("student")
def resolve_get_student(*_, id):
    conn = create_connection()

    query = "SELECT * FROM students WHERE id = %s::uuid;"
    result = execute_read_query(conn, query, (id,))

    return result[0] if result else None


@query.field("students")
def resolve_get_all_students(*_):
    conn = create_connection()

    query = "SELECT * FROM students;"
    result = execute_read_query(conn, query)

    return result


@query.field("getMostPopularCourse")
def resolve_get_most_popular_course():
  raise NotImplementedError()


type_defs = load_schema_from_path("graphql/schema.graphql")
schema = make_executable_schema(type_defs, query, snake_case_fallback_resolvers)
