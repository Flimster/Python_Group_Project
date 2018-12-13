PRAGMA foreign_keys = ON;

create table assigments
(
	a_id integer
		constraint assigment_pk
			primary key autoincrement,
	a_nafn text,
	a_active integer
);

create table problems
(
	p_id integer
		constraint problems_pk
			primary key autoincrement,
	a_id integer
		constraint problems_assigments_a_id_fk
			references assigments,
	p_name text,
	p_desc text,
	p_solution_name text
);
