CREATE EXTENSION IF NOT EXISTS pg_cron;

CREATE OR REPLACE FUNCTION data_arxiv()
RETURNS VOID AS
$$
BEGIN
  EXECUTE 'CREATE TABLE IF NOT EXISTS data (LIKE notifications_notification INCLUDING CONSTRAINTS)';

  EXECUTE '
    INSERT INTO data
    SELECT *
    FROM notifications_notification
    WHERE created_date < current_date - interval ''6 months''
  ';

  DELETE FROM notifications_notification WHERE created_date < current_date - interval '6 months';
END;
$$
LANGUAGE plpgsql;

SELECT cron.schedule('0 0 * * *', $$SELECT data_arxiv()$$);
