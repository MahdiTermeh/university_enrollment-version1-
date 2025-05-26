create database university;

--

create table university.students
(
    s_id int  primary key auto_increment,
    name varchar(30),
    family varchar(30),
    birth_date date,
    username varchar(30),
    password varchar(20)

);

--

create table university.lessons
(
    l_id int auto_increment primary key ,
    title varchar(30),
    start_date date,
    end_date date,
    professor varchar(30),
    room_number int,
    credit int,
    capacity int
);

--

create table university.enrollment
(
    id int auto_increment primary key ,
    lesson_id int,
    foreign key (lesson_id) references university.lessons(l_id) on delete cascade ,
    student_id int,
    foreign key (student_id) references university.students(s_id) on delete cascade ,
    enrollment_date date
);



--

create view enrollment_report as
select * from university.enrollment
join university.students on students.s_id=enrollment.student_id
join university.lessons on lessons.l_id = enrollment.lesson_id;


