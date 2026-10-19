import sqlite3
from icecream import ic as print
cursor
""" we use 
    with connection: because if any error occors it rolls back 
    else it execute perfectly
    like if we are addding two users 
    1 line executed and other failed then it rolls back that is it undos everthing it has done

""" 


# step-1 Setup database
def get_connection(db_name):
    try:
        return sqlite3.connect(db_name)
    except Exception as e:
        print(f"Error: {e}")
        raise


# step-2 Create a table in database
def create_table(connection):
    # u canuse any name for the table here I used users
    query = """
   CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
    """
    try:
        with connection:
            connection.execute(query)
        print("Table created succesfully")
    except Exception as e:
        print(e)


# step-3 Add User to a database
def insert_user(connection, name: str, age: int, email: str):
    # here ? are place holders .we use them to avoid injection(input) problems
    query = "INSERT INTO users (name,age,email) VALUES (?, ?, ?)"
    try:
        with connection:
            connection.execute(query, (name, age, email))
        print(f"Users: {name} is added")
    except Exception as e:
        print(e)


# step - 4 query all users in database
def fetch_users(connection, condition=None) -> list[tuple]:  # (raghava,17,email)
    # * means all
    query = "SELECT * FROM users"
    if condition:
        query += f"WHERE {condition}"
    try:
        with connection:
            rows = connection.execute(query).fetchall()
        return rows
    except Exception as e:
        print(e)


# step - 5 delete a user
def delete_user(connection, user_id: int):
    query = "DELETE FROM users WHERE id = ?"
    try:
        with connection:
            connection.execute(
                query, (user_id,)
            )  # we need to give a tuple so we put a ,
        print(f"USER ID: {user_id} was deleted")
    except Exception as e:
        print(e)


# step-6 updating a user
def update_user(connection, user_id: int, name, email, age):
    if email:
        query = "UPDATE users SET email = ? WHERE id = ?"
        try:
            with connection:
                connection.execute(query, (email, user_id))
        except Exception as e:
            print(e)
    if name:
        query = "UPDATE users SET name = ? WHERE id = ?"
        try:
            with connection:
                connection.execute(query, (name, user_id))
        except Exception as e:
            print(e)
    if age:
        query = "UPDATE users SET age = ? WHERE id = ?"
        try:
            with connection:
                connection.execute(query, (age, user_id))
        except Exception as e:
            print(e)


# add multiple users
def insert_users(connection, users: list[tuple[str, int, str]]):
    query = "INSERT INTO users (name, age, email) VALUES (?,?,?)"
    try:
        with connection:
            connection.executemany(query, users)
        print(f"{len(users)} are added")
    except Exception as e:
        print(e)


# main function
def main():
    connection = get_connection("Raghava.db")

    try:
        create_table(connection)  # Create  my table
        while True:
            start = input(
                "Options: (Add, Delete, Update, Search, Add, Add Many, End): "
            ).lower()
            if start == "add":
                name = input("Name: ")
                age = int(input("Age: "))
                email = input("Email: ")
                insert_user(connection, name, age, email)
            elif start == "search":
                print("All Users: ")
                for user in fetch_users(connection):
                    print(user)
            elif start == "delete":
                user_id = int(input("Id of the user: "))
                delete_user(connection, user_id)
                print("User has been succesfully deleted")
            elif start == "end":
                break
            elif start == "update":
                user_id = int(input("Id of the user: "))
                what = input("Name,Age,Email: ").lower()
                if what == "name":
                    name = input("name: ")
                    try:
                        update_user(connection, user_id, name, None, None)
                    except Exception as e:
                        print(e)
                elif what == "age":
                    age = int(input("age: "))
                    try:
                        update_user(connection, user_id, None, None, age)
                    except Exception as e:
                        print(e)
                elif what == "email":
                    email = input("email: ")
                    try:
                        update_user(connection, user_id, None, email, None)
                    except Exception as e:
                        print(e)
            elif start == "add many":
                users = [
                    ("gohan", 100, "gohan@dzb.com"),
                    ("goku", 300, "goku@dzb.com"),
                ]
                insert_users(connection, users)

            else:
                break
    finally:
        connection.close()


if __name__ == "__main__":
    main()
