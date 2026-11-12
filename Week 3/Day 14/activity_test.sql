
-- ==========================================
-- DAY 14: RECORD TASK STATE CHANGE
-- ==========================================

-- Check the task before updating

SELECT *
FROM tasks
WHERE id = 1;

-- Update the task and record its activity
-- in the same SQL statement.

WITH changed_task AS (

    UPDATE tasks
    SET status = 'completed'
    WHERE id = 1
      AND status = 'pending'

    RETURNING id, status

)

INSERT INTO task_activities (
    task_id,
    actor_id,
    action,
    old_value,
    new_value
)

SELECT
    changed_task.id,
    1,
    'status_changed',
    'pending',
    changed_task.status

FROM changed_task;

-- Verify updated task

SELECT *
FROM tasks
WHERE id = 1;

-- Verify activity record

SELECT
    task_activities.id,
    task_activities.task_id,
    users.username AS changed_by,
    task_activities.action,
    task_activities.old_value,
    task_activities.new_value,
    task_activities.created_at

FROM task_activities

INNER JOIN users
    ON task_activities.actor_id = users.id

WHERE task_activities.task_id = 1;
