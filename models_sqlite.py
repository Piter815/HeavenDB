import sqlite3
connection = sqlite3.connect("HeavenDB2.db")

cursor = connection.cursor()

sql_command1 = """

create table employees (
empl_id smallint unsigned not null,
empl_name varchar(40) not null,
empl_surname varchar(40) not null,
empl_start_date DATE not null,
empl_PESEL smallint(11) not null,
empl_phone varchar(40),
empl_address varchar(40),
primary key (empl_id));
"""

sql_command2 = """

create table departments (
department_id smallint unsigned not null,
department_name varchar(40) not null,
department_budget decimal (7,2) not null,
department_address varchar(40) not null,
dpt_supervisor_id smallint unsigned not null,
PRIMARY KEY (department_id),
FOREIGN KEY (dpt_supervisor_id) REFERENCES employees (empl_id)
);
"""
sql_command3 = """

create table courses (
course_id smallint unsigned not null,
course_price decimal (7,2) not null,
course_name varchar(40) not null,
course_points smallint (5) not null,
start_date DATE not null,
end_date DATE not null,
course_type varchar(40) not null,
course_teacher smallint unsigned not null,
PRIMARY KEY (COURSE_ID),
FOREIGN KEY (course_teacher) REFERENCES employees (empl_id)
);
"""
sql_command4 = """
create table scores (
record_id smallint unsigned not null,
course_id smallint unsigned not null,
score_date date not null,
score_value smallint not null,
primary KEY(record_id),
foreign key (course_id) references courses (course_id)
);
"""

sql_command5 = """

create table students (
student_id smallint unsigned not null,
student_name varchar(40) not null,
student_surname varchar(40) not null,
student_PESEL smallint(11) not null,
student_phone varchar(40),
student_address varchar(40),
primary key (student_id)
);
"""
sql_command6 = """

create table students_courses (
student_id smallint unsigned not null,
course_id smallint unsigned not null,
PRIMARY KEY (student_id, course_id),
foreign key (course_id) references courses (course_id),
foreign key (student_id) references students (student_id)
);
"""

cursor.execute(sql_command1)
cursor.execute(sql_command2)
cursor.execute(sql_command3)
cursor.execute(sql_command4)
cursor.execute(sql_command5)
cursor.execute(sql_command6)