# 📘 Assignment: SQLite Databases with Python

## 🎯 Objective

Learn how to work with SQLite databases in Python by creating, reading, updating, and deleting records in a small database application. This assignment connects Python programming with real data persistence and basic database concepts.

## 📝 Tasks

### 🛠️ Set Up the SQLite Database

#### Description
Create a Python script that connects to an SQLite database file and sets up a simple table for storing information.

#### Requirements
The completed program must:

- Import the `sqlite3` module.
- Connect to a SQLite database file such as `school.db` or `tasks.db`.
- Create a table with at least two columns, such as `id` and `name`.
- Include a primary key and at least one text or integer field.
- Print a confirmation message after creating the table.
- Close the database connection cleanly when finished.

### 🛠️ Insert and Read Data

#### Description
Add sample records to the database and retrieve them using SQL queries.

#### Requirements
The completed program must:

- Insert at least three records into the table.
- Use SQL `INSERT` statements to save the data.
- Query the database with `SELECT` to display all saved records.
- Format the output so it is easy to read in the terminal.
- Show the records in the order they were inserted or sorted by a field.

### 🛠️ Update and Delete Records

#### Description
Practice modifying and removing data safely using SQL statements and Python logic.

#### Requirements
The completed program must:

- Update at least one record using `UPDATE`.
- Delete at least one record using `DELETE`.
- Verify the change by querying the table again.
- Handle invalid IDs or missing records gracefully.
- Explain in comments or documentation how the program changes the database state.
