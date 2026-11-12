
-- ==========================================
-- DAY 14: ACTIVITY TABLE MIGRATION
-- ==========================================

BEGIN;

CREATE TABLE task_activities (
    id SERIAL PRIMARY KEY,

    task_id INTEGER NOT NULL,

    actor_id INTEGER NOT NULL,

    action VARCHAR(50) NOT NULL,

    old_value VARCHAR(100),

    new_value VARCHAR(100),

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_activity_task
        FOREIGN KEY (task_id)
        REFERENCES tasks(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_activity_actor
        FOREIGN KEY (actor_id)
        REFERENCES users(id)
);

COMMIT;
