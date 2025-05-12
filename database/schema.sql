-- Drop tables in reverse order of dependencies
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS majors;

-- Create the `majors` table first (no dependencies)
CREATE TABLE majors (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR NOT NULL,
    credit_required INT NOT NULL,
    minimum_gpa FLOAT NOT NULL
);

-- Create the `students` table (depends on `majors`)
CREATE TABLE students (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR NOT NULL,
    major_id UUID,
    CONSTRAINT fk_major FOREIGN KEY (major_id) REFERENCES majors(id) ON DELETE CASCADE
);

-- Create the `courses` table (keep id and add unique constraint on course_name)
CREATE TABLE courses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    course_name VARCHAR NOT NULL UNIQUE, -- Add unique constraint on course_name
    major_id UUID ,
    credit_hours INT NOT NULL,
    tuition_cost FLOAT NOT NULL,
    CONSTRAINT fk_major FOREIGN KEY (major_id) REFERENCES majors(id) ON DELETE CASCADE
);

-- Create the `enrollments` table (use course_name for association)
CREATE TABLE enrollments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID,
    course_id UUID NOT NULL,  -- Change to UUID to match courses.id
    credit_hours FLOAT NOT NULL, 
    letter_grade VARCHAR NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    cost FLOAT NOT NULL,
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE  -- Reference courses.id
);