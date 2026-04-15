from abc import ABC, abstractmethod
from db_configuration import get_connection

class BaseManager(ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def view(self):
        pass


class User(BaseManager):

    def __init__(self, name):
        self.__name = name

    def add(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users(name) VALUES (%s)", (self.__name,))
        conn.commit()
        print("User added")

    def view(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            print(row)


class Expense(User):

    def __init__(self, user_id, amount, category, description, date):
        super().__init__("temp")
        self.__user_id = user_id
        self.__amount = amount
        self.__category = category
        self.__description = description
        self.__date = date

    def add(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO expenses(user_id, amount, category, description, date)
        VALUES (%s, %s, %s, %s, %s)
        """, (self.__user_id, self.__amount,
              self.__category, self.__description, self.__date))

        conn.commit()
        print("Expense added")

    def view(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT users.name, expenses.amount, expenses.category,
               expenses.description, expenses.date
        FROM expenses
        JOIN users ON users.user_id = expenses.user_id
        WHERE users.user_id = %s
        """, (self.__user_id,))

        data = cursor.fetchall()

        for row in data:
            print(row)

        return data