PRAGMA foreign_keys = ON;
UPDATE sqlite_sequence SET seq = 0;

create table assignments
(
	a_id integer
		constraint assigment_pk
			primary key autoincrement,
	a_name text,
	a_active integer
);

create table problems
(
	p_id integer
		constraint problems_pk
			primary key autoincrement,
	a_id integer
		constraint problems_assignments_a_id_fk
			references assignments,
	p_name text,
	p_desc text,
	p_solution_name text
);

insert into assignments(a_name, a_active) values ('Basics in Pyton', 1);
insert into assignments(a_name, a_active) values ('Advanced Python pt. 1', 1);
insert into assignments(a_name, a_active) values ('Advanced Python pt. 2', 0);

insert into problems(a_id, p_name, p_desc, p_solution_name) values (1, 'Hello World', 'Create and app that prints out hello world', 'hello_world');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (1, 'Sum of two numbers', 'Create an app that calculates the sum of two numbers', 'two_sum');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (1, 'Pring out an input', 'Create a function print_input that prints out the input as a string', 'print_input');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (1, 'If statement', 'Create an if statement that will return True if a number is positive, False if its not', 'if_statement');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (2, 'For loop', 'Create a function that takes in a positive number. Create a loop that prints out, starting from 0, to the input number', 'for_loop');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (2, 'Lists', 'Create a for loop that takes in a number and adds them to a list. 1,2,3 would then be [1, 2, 3]', 'numbers_tolist');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (3, 'Country list', 'List all countries that took part in WWII','country_list');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (3, 'Persons info', 'List the infromation of people stored in a dict. their ssn is the dict key', 'person_info');


