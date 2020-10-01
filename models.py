from sqlalchemy import create_engine, Column, Integer, Sequence, Float, String, Date, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Department(Base):
    __tablename__ = "departments"
    department_id = Column(Integer, Sequence("departments_id_seq"), primary_key=True)
    department_name = Column(String(40))
    department_budget = Column(Numeric(7,2))
    department_address = Column(String(40))
    dpt_supervisor_id = Column(Integer, ForeignKey('employees.empl_id'))


class Score(Base):
    __tablename__ = "scores"
    record_id = Column(Integer, Sequence("departments_id_seq"), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    score_date = Column(Date)
    score_value = Column(Integer)


class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, Sequence("courses_id_seq"), primary_key=True)
    course_price = Column(Numeric(7,2))
    course_name = Column(String(40))
    course_points = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    course_type = Column(String(40))

    scores = relationship('Score', back_populates='courses')


class Employee(Base):
    __tablename__ = "employees"
    empl_id = Column(Integer, Sequence("employees_id_seq"), primary_key=True)
    empl_name = Column(String(40))
    empl_surname = Column(String(40))
    empl_start_date = Column(Date)
    empl_PESEL = Column(Integer)
    empl_phone = Column(String(40))
    empl_address = Column(String(40))

    departments = relationship('Department', back_populates='employees')


class Student(Base):
    __tablename__ = "students"
    student_id = Column(Integer, Sequence("students_id_seq"), primary_key=True)
    student_name = Column(String(40))
    student_surname = Column(String(40))
    student_PESEL = Column(Integer)
    student_phone = Column(String(40))
    student_address = Column(String(40))


Department.employees = relationship(
    'Employee',
    order_by=Employee.empl_id,
    back_populates='departments'
)

Score.courses = relationship(
    'Course',
    order_by=Course.course_id,
    back_populates='scores'
)

if __name__ == '__main__':
    engine = create_engine("sqlite:///HeavenDB.sqlite")
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()