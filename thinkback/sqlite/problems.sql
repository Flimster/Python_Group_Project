create table problems
(
	p_id text
		constraint problem_pk
			primary key,
	a_id text not null
		constraint problem_assigment_a_id_fk
			references assigment,
	p_name text,
	p_desc text,
	p_solution_name text
);
