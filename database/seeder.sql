\copy majors(id, name, credit_required, minimum_gpa) FROM 'majors.csv' CSV HEADER NULL 'null';

CREATE TEMP TABLE temp_students AS TABLE students WITH NO DATA;

\copy temp_students(id, name, major_id) FROM 'students.csv' CSV HEADER NULL 'null';
INSERT INTO students (id, name, major_id)
SELECT id, name, major_id
FROM temp_students
WHERE major_id IS NOT NULL;
DROP TABLE temp_students;

CREATE TEMP TABLE temp_enrollments (
    student_id UUID,
    course_name VARCHAR NOT NULL,
    credit_hours FLOAT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    cost FLOAT NOT NULL,
    letter_grade VARCHAR NOT NULL
);
\copy temp_enrollments(student_id, course_name, credit_hours, start_date, end_date, cost, letter_grade) FROM 'enrollments.csv' CSV HEADER NULL 'null';
INSERT INTO courses (id, course_name, major_id, credit_hours, tuition_cost)
SELECT 
    md5(course_name)::uuid AS id,  
    course_name,
    (
        SELECT s.major_id
        FROM students s
        WHERE s.id = ANY (
            SELECT DISTINCT te.student_id
            FROM temp_enrollments te
            WHERE te.course_name = e.course_name
            AND major_id IS NOT NULL
        )
        LIMIT 1
    ) AS major_id,  
    MODE() WITHIN GROUP (ORDER BY credit_hours) AS credit_hours,
    AVG(cost) AS tuition_cost  
FROM temp_enrollments e
GROUP BY course_name;


INSERT INTO enrollments (student_id, course_id, credit_hours, start_date, end_date, cost, letter_grade)
SELECT 
    te.student_id,
    c.id AS course_id,  
    te.credit_hours,
    te.start_date,
    te.end_date,
    te.cost,
    te.letter_grade
FROM temp_enrollments te
JOIN courses c ON te.course_name = c.course_name
Where te.student_id IN (SELECT id FROM students);
DROP TABLE temp_enrollments;