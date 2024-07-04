DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
	user_email varchar(100) NOT NULL,
	user_first_name VARCHAR(64) NOT NULL,
	user_last_name VARCHAR(64) NOT NULL,
	user_password VARCHAR(250) NOT NULL
);

DROP TABLE IF EXISTS splits CASCADE;
CREATE TABLE splits(
	split_id SERIAL PRIMARY KEY,
	split_name VARCHAR(64) NOT NULL,
	split_desc VARCHAR(200),
	_user_id INT NOT NULL,
	FOREIGN KEY (_user_id) REFERENCES users(user_id)
);

DROP TABLE IF EXISTS exercises CASCADE;
CREATE TABLE exercises(
	exercise_id SERIAL PRIMARY KEY,
	exercise_name VARCHAR(64) NOT NULL,
	exercise_desc VARCHAR(200),
	_split_id INT NOT NULL,
	FOREIGN KEY (_split_id) REFERENCES splits(_split_id)
);

DROP TABLE IF EXISTS sessions CASCADE;
CREATE TABLE sessions(
	session_id SERIAL PRIMARY KEY,
	session_date DATE NOT NULL DEFAULT CURRENT_DATE,
	_split_id INT NOT NULL,
	FOREIGN KEY (_split_id) REFERENCES splits(_split_id)
);

DROP TABLE IF EXISTS sets CASCADE:
CREATE TABLE sets(
	set_id SERIAL PRIMARY KEY,
	set_number INT NOT NULL,
	weight decimal NOT NULL,
	reps smallint NOT NULL,
	_exercise_id INT NOT NULL,
	_session_id INT NOT NULL,
	FOREIGN KEY (_exercise_id) REFERENCES exercises(exercise_id),
	FOREIGN KEY (_session_id) REFERENCES exercises(_session_id)
);
