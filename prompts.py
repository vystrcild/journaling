import sqlite3
import csv

def import_data():
    # Connect to or create a new database
    conn = sqlite3.connect('prompts.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # # Create a table
    # cursor.execute('''CREATE TABLE prompts (id INTEGER PRIMARY KEY, prompt TEXT)''')

    # Open the CSV file and read the data
    with open('prompts.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Insert the data into the table
            #print(row["Prompt"])
            cursor.execute("INSERT INTO prompts (prompt) VALUES (?)", ((row["Prompt"],)))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def get_random_prompt():
    # Connect to the database
    conn = sqlite3.connect('prompts.db')
    cursor = conn.cursor()

    # Execute a SELECT statement to get a random row
    cursor.execute("SELECT * FROM prompts ORDER BY RANDOM() LIMIT 1")

    # Fetch the result
    result = cursor.fetchone()

        # Close the connection
    conn.close()
    return result[1]
