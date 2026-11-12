SELECT 
    id,
    title,
    status,
    owner_id

FROM tasks
WHERE owner_id=1
ORDER BY created_at DESC, id DESC

SELECT
    tasks.id AS task_id,
    tasks.title AS task_title,
    projects.name AS project_name
FROM tasks
INNER JOIN projects
    ON tasks.project_id = projects.id
ORDER BY tasks.id ASC;


SELECT
    tasks.id,
    tasks.title,
    users.username AS owner,
    projects.name AS project
FROM tasks
INNER JOIN users
    ON tasks.owner_id = users.id
INNER JOIN projects
    ON tasks.project_id = projects.id
ORDER BY tasks.id ASC;


SELECT
    projects.id,
    projects.name,
    tasks.title
FROM projects
LEFT JOIN tasks
    ON projects.id = tasks.project_id
ORDER BY projects.id ASC, tasks.id ASC;


SELECT *
FROM tasks
ORDER BY created_at DESC, id DESC;