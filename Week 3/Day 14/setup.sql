CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);

CREATE TABLE projects(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE tasks(
    id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'pending',
    owner_id INTEGER NOT NULL,
    project_id INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_task_owner
    FOREIGN KEY (owner_id)
    REFERENCES users(id),

    CONSTRAINT fk_task_project
    FOREIGN KEY (project_id)
    REFERENCES users(id)


);

INSERT INTO users (username)
VALUES
('Alex'),
('Sam'),
('John');

INSERT INTO projects (name)
VALUES
('Website Development'),
('Mobile Application');

INSERT INTO tasks (title, status, owner_id, project_id)
VALUES
('Create login API', 'pending', 1, 1),
('Design homepage', 'completed', 2, 1),
('Build authentication', 'pending', 1, 2),
('Create dashboard', 'pending', 3, 2),
('Write API documentation', 'completed', 1, 1),
('Fix navigation bug', 'pending', 2, 2);

-- Verify records

SELECT * FROM users;
SELECT * FROM projects;
SELECT * FROM tasks;