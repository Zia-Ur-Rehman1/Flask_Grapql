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
def resolve_get_most_popular_course(_, info, input):
    conn = create_connection()

    start_date = input['startDate']
    end_date = input['endDate']
    
    query = """
    SELECT courses.id, courses.course_name AS name, courses.major_id, courses.credit_hours, courses.tuition_cost,
    COUNT(enrollments.id) AS enrollment_count
    FROM courses
    JOIN enrollments ON courses.id = enrollments.course_id
    WHERE enrollments.start_date >= %s AND enrollments.end_date <= %s
    GROUP BY courses.id
    ORDER BY enrollment_count DESC
    LIMIT 1;
    """
    result = execute_read_query(conn, query, (start_date, end_date))
    
    if result:
        return {
            "id": result[0]["id"],
            "name": result[0]["name"],
            "majorId": result[0]["major_id"],
            "creditHours": result[0]["credit_hours"],
            "tuitionCost": result[0]["tuition_cost"],
            "deviationFromMeanGPA": None,
            "rawDifferenceFromMeanGPA": None,
            }
    return None

@query.field("getGradesPerCourse")
def resolve_get_grades_per_course(_, info, input):
    conn = create_connection()
    course_id = input['courseId']
    
    query = """
    SELECT ARRAY_AGG(letter_grade) AS grades
    FROM enrollments
    WHERE course_id = %s;
    """
    
    try:
        result = execute_read_query(conn, query, (course_id,))
        return {
            "courseId": course_id,
            "grades": result[0]["grades"] if result and result[0]["grades"] else []
        }
    except Exception as e:
        print(f"Error fetching grades for course {course_id}: {e}")
        return {
            "courseId": course_id,
            "grades": []
        }        
type_defs = load_schema_from_path("graphql/schema.graphql")
schema = make_executable_schema(type_defs, query, snake_case_fallback_resolvers)
