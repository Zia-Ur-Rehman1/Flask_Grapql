drop table if exists students;
create table students (
    id uuid primary key default gen_random_uuid(),
    name varchar not null
);
