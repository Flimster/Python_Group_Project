CREATE TABLE Assignment (
    a_name TEXT,
    a_active INT
);

CREATE TABLE Problem (
    p_id TEXT PRIMARY KEY,
    p_name TEXT,
    p_desc TEXT,
    p_assignment_name TEXT,
    p_function_name TEXT);