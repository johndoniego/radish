from database import insert_schedule, create_connection, insert_teacher, insert_rooms, get_schedule

def all_schedules():
    # Initialize the database and tables
    insert_rooms()

    # Add sample teacher
    insert_teacher("21-24870", "John Doniego")

    # Insert sample schedules
    insert_schedule('CL-A', '11/4/24', 'Math', '2', '00', 'AM', '7', '00', 'PM', '1', '21-24870')
    insert_schedule('CL-B', '11/5/24', 'Science', '3', '00', 'PM', '5', '00', 'PM', '2', '21-24870')

    # Fetch and print all schedules
    schedules = get_schedule()
    for schedule in schedules:
        print(schedule)

# Debugging: Print all schedules to verify insertion
def print_all_schedules():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM schedule')
    rows = cursor.fetchall()
    for row in rows:
        print(dict(row))
    conn.close()

# Call this function to verify data insertion
all_schedules()
print_all_schedules()