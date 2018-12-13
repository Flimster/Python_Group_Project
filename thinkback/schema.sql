PRAGMA foreign_keys = ON;

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
insert into assignments(a_name, a_active) values ('Advanced Mathematics', 1);
insert into assignments(a_name, a_active) values ('Discrete Mathematics', 0);
insert into assignments(a_name, a_active) values ('Quantum Calulations', 0);
insert into assignments(a_name, a_active) values ('Tic Tac Toe', 1);
insert into assignments(a_name, a_active) values ('Hangman', 0);
insert into assignments(a_name, a_active) values ('Texas hold em', 1);
insert into assignments(a_name, a_active) values ('String lists', 1);
insert into assignments(a_name, a_active) values ('Dictionaries', 0);

insert into problems(a_id, p_name, p_desc, p_solution_name) values (1, 'Create Hello World', 'Create and app that prints out hello world', 'hello_world');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (1, 'Sum of two numbers', 'Create an app that calculates the sum of two numbers', 'two_sum');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (2, 'Matrix calculation', 'Calculate any sort of incoming matrix', 'matrix');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (3, 'Calculate distance', 'Calculate the distance of two objects', 'calculate_distance');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (4, 'Something very mathy', 'Do some swesome equation calculation', 'quantum_calc');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (5, 'Tic Tac Toe game', 'Make the tic tac toe game', 'tic_tac_toe');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (6, 'Hangman game', 'Make the hangman game', 'hangman');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (7, 'Texas hold em poker game', 'Make the poker game', 'poker');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (8, 'Name list', 'Take in a list of names and print out only the ones with more than 7 characters and no middle name', 'name_list');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (9, 'Country list', 'List all countries that took part in WWII','country_list');
insert into problems(a_id, p_name, p_desc, p_solution_name) values (9, 'Persons info', 'List the infromation of people stored in a dict. their ssn is the dict key', 'person_info');


