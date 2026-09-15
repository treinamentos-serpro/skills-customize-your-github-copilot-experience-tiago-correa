import sqlite3


def create_database():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    # TODO: Create a table named tasks with columns such as id, title, and completed.

    connection.commit()
    connection.close()


def insert_sample_tasks():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    # TODO: Insert at least three tasks into the database.

    connection.commit()
    connection.close()


def list_tasks():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    # TODO: Select all tasks and print them in a readable format.

    connection.close()


def update_task(task_id, new_title):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    # TODO: Update the task with the given id.

    connection.commit()
    connection.close()


def delete_task(task_id):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    # TODO: Delete the task with the given id.

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
    insert_sample_tasks()
    list_tasks()
    update_task(1, "Learn SQLite")
    delete_task(2)
    list_tasks()
