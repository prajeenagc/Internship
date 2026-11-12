
-- GENERATE ADDITIONAL SYNTHETIC DATA

-- Add more users

INSERT INTO users (username)
SELECT 'User_' || generate_series
FROM generate_series(4, 1000);

-- Add 100,000 additional tasks

INSERT INTO tasks (
    title,
    status,
    owner_id,
    project_id
)

SELECT
    'Synthetic task ' || n,

    CASE
        WHEN n % 2 = 0 THEN 'completed'
        ELSE 'pending'
    END,

    (n % 1000) + 1,

    (n % 2) + 1

FROM generate_series(1, 100000) AS n;

-- Update statistics

ANALYZE tasks;

-- TEST 1: WITHOUT INDEX

EXPLAIN ANALYZE
SELECT *
FROM tasks
WHERE owner_id = 10;

-- TEST 2: CREATE INDEX

CREATE INDEX idx_tasks_owner_id
ON tasks(owner_id);

ANALYZE tasks;


-- TEST 3: WITH INDEX


EXPLAIN ANALYZE
SELECT *
FROM tasks
WHERE owner_id = 10;


-- INSPECT INDEX


SELECT
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'tasks';

