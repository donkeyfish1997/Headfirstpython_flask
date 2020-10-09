import sqlite3


def get_names_from_store():
    connection = sqlite3.connect('static/coachdata.sqlite')
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM athletes")
    response = [row[0] for row in cursor.fetchall()]
    connection.close()
    return response


def get_ID_from_name(athlete_name):
    connection = sqlite3.connect('static/coachdata.sqlite')
    cursor = connection.cursor()

    cursor.execute("SELECT id FROM athletes WHERE name = ?", (athlete_name,))
    response = cursor.fetchone()[0]
    connection.close()
    return response


def add_time_from_id(the_current_id, each_time):
    connection = sqlite3.connect('static/coachdata.sqlite')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO timing (athlete_id,value) VALUES (?,?)", (the_current_id, each_time))
    connection.commit()
    connection.close()


def add_athlete(athlete_name,athlete_dob):
    connection = sqlite3.connect('static/coachdata.sqlite')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO athletes (name,dob) VALUES (?,?)", (athlete_name,athlete_dob))
    connection.commit()
    connection.close()


def get_athlete_from_id(athlete_id):
    connection = sqlite3.connect('static/coachdata.sqlite')
    cursor = connection.cursor()

    cursor.execute("SELECT name,dob FROM athletes WHERE id = ?", (athlete_id,))
    (name, dob) = cursor.fetchone()

    cursor.execute("SELECT value FROM timing WHERE athlete_id = ?", (athlete_id,))
    data = [row[0] for row in cursor.fetchall()]

    response = {
        'Name': name,
        'DOB': dob,
        'data': data,
        'top3': sorted(data)[:3],
    }
    connection.close()
    return response


if __name__ == '__main__':
    print(get_names_from_store())
