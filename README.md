Course Enrollment System Documentation

Project Overview

This is a university course enrollment system developed using Python and Tkinter for the graphical interface, with MySQL as the backend database. The project includes two versions:

1. Version 1 – Course enrollment is handled by the system manager.


2. Version 2 – Students can log in and enroll in courses themselves.




---

Technologies Used

Programming Language: Python

GUI Framework: Tkinter

Database: MySQL

Development Environment: Any (e.g., PyCharm, VS Code)



---

Version 1 – Admin-Based Enrollment

Main Sections:

About Me
Displays the developer's photo, biography, and personal interests.

Lesson
Allows the system manager to define and manage courses.

Student
Used to register and manage students by the manager.

Enrollment
This section is protected by a login screen. Only if the username is **_root_** and the password is ***root*123**, the manager can access and perform enrollment operations for students.



---



---

Features

User-friendly GUI using Tkinter

MySQL database integration for persistent storage

Authentication for both manager and student logins

Full course and student management

Self-service course enrollment by students (in Version 2)



---

Developer Notes

All data (students, courses, enrollment) are stored and retrieved via MySQL.

Basic login security is implemented using username/password validation.

Code is modular and organized for easier maintenance and future expansion.