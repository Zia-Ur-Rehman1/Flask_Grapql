# Guild's Backend Take-Home Challenge

Thanks so much for taking the time to show off some of your skills! Take-home projects/coding challenges come in all shapes and sizes. Some are great and some are terrible. We've worked really hard to create a challenge that not only gives us some insight into your abilities as an engineer, but one that is also fun to work on.

There are not supposed to be any "gotchas" in this challenge. If you find yourself wondering if we're trying to trick you in regards to one of the requirements, we aren't.

This challenge is designed to be completed in 2-4 hours. We are not evaluating how much time someone can put in beyond that limit. If you can't complete everything within this timeframe, we prefer to see one part done well rather than multiple parts done partially. For example, there are two report queries we ask for in the [Software Engineer I/II Requirements](SE_REQUIREMENTS.md). If you are not going to be able to complete everything for both in the 2-4 hours, completing everything for one will tell us a lot more about your abilities as an engineer. If you run out of time, feel free to include a brief paragraph in your submission describing what you would do next if you had more time - this helps us understand your thought process and priorities.

You may use either Python or Typescript (choose one only, boilerplate found in the corresponding directories). Please use the boilerplate provided as opposed to rolling your own.

## The challenge

You will find several CSVs in the Data section below. You will use these to populate your data table(s). How you structure the data is entirely up to you. We have provided an example of how to write a GraphQL resolver if you are unfamiliar. The ultimate goal is for you to write the business logic to satisfy the GraphQL queries already provided in the `~/graphql/schema.graphql` file (do not modify this file).

### Background

- To graduate, every student must complete 120 credits
  - In order for a credit to apply toward a student's accrued credit count, they must receive a passing (C- or better) grade
  - Courses are uniquely named, and always contain the major in the name (e.g. Mathematics 1000), and a student may take any course including outside their major
- A student can only receive credit for a course one time
- All grades are letter grades (+/- impacts GPA calculation)
- In-progress enrollments (enrollments that have start dates in the past and end dates in the future relative to now) do not count toward GPA/accrued credit counts

#### Grade conversion

| Grade | Value |
| ----- | ----- |
| A+    | 4.0   |
| A     | 4.0   |
| A-    | 3.7   |
| B+    | 3.3   |
| B     | 3.0   |
| B-    | 2.7   |
| C+    | 2.3   |
| C     | 2.0   |
| C-    | 1.7   |
| D+    | 1.3   |
| D     | 1.0   |
| D-    | 0.7   |
| F     | 0.0   |

## The code

### Requirements

- Python - [pip](https://pypi.org/project/pip/)
- Typescript (Node) - [Yarn](https://yarnpkg.com/)
- Database - [Docker](https://www.docker.com/)

### Project Structure

The `database` directory contains everything related to the DB, the `graphql` directory contains the graphql schema, and the `python` and `typescript` directories contain the backends in each respective language.

The env file `.env` contains custom environmental values like what port to run the webserver on.

Everything can be setup and run through make commands defined in the Makefile.

## Data

The data is located in CSV format here:

- [Majors (<1kB)](https://guild-challenges.s3.us-west-2.amazonaws.com/backend-take-home-csv/majors.csv)
- [Students (8MB)](https://guild-challenges.s3.us-west-2.amazonaws.com/backend-take-home-csv/students.csv)
- [Enrollments (80MB)](https://guild-challenges.s3.us-west-2.amazonaws.com/backend-take-home-csv/enrollments.csv)

### Database

Commands to start/stop/migrate/seed the database. Make commands use docker but you can also DIY using the .sql files.

- `make db-start` - starts the database
- `make db-stop` - stops the database (and erases all data)
- `make db-migrate` - runs the contents of `database/schema.sql` to create the database structure
- `make db-seed` - runs the contents of `database/seeder.sql` to seed sample/test data

### Typescript

- `make typescript-setup` - installs node packages and builds typescript files
- `make typescript-test` - run unit tests
- `make typescript-dev` - run the GraphQL server locally (with hot reloading on file change)
- `make typescript-lint` - lint all files in `src` and `test

### Python

1. Start a virtual environment with `python -m venv python/python-env`
2. Activate the environment with `source python/python-env/bin/activate`
3. Install dependencies with `pip install -r python/src/requirements.txt`

To start the server: `make python-start-server`
To run tests: `make python-run-tests`

After starting the server, the GraphQL interactive UI can be accessed at `http://127.0.0.1:5000/graphql`.

## Delivering your code

Please create a branch for your work off of `main` in this repository. When you are ready to submit the project, open a PR into `main` from your feature branch, assign the repository creator (most likely the hiring manager you spoke with on the phone) as a reviewer and let your Guild recruiting coordinator know that you're done.

## Reviewers

Please submit your feedback via Greenhouse.
