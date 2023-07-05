import psycopg2
from src.models.Activity import Activity

def connect():
    return psycopg2.connect(
        host="localhost",
        database="crm",
        user="postgres",
        password="password"
    )

def get_all_activities():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM activities")
    rows = cur.fetchall()
    activities = [Activity(*row) for row in rows]
    cur.close()
    conn.close()
    return activities

def get_activity_by_id(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM activities WHERE id = %s", (id,))
    row = cur.fetchone()
    activity = Activity(*row) if row else None
    cur.close()
    conn.close()
    return activity

def create_activity(activity):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO activities (user_id, type, description, date) VALUES (%s, %s, %s, %s) RETURNING id",
        (activity.user_id, activity.type, activity.description, activity.date)
    )
    id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return id

def update_activity(activity):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE activities SET user_id = %s, type = %s, description = %s, date = %s WHERE id = %s",
        (activity.user_id, activity.type, activity.description, activity.date, activity.id)
    )
    conn.commit()
    cur.close()
    conn.close()

def delete_activity(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM activities WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()