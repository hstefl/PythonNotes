"""
https://edube.org/learn/pcpp1-5/lab-sqlite3-lab-1
"""
import sqlite3


class Todo:
    def __init__(self):
        self.db = sqlite3.connect('todo.db')
        self.cursor = self.db.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS `todo` (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                priority INTEGER NOT NULL
            )""")

    def create_task(self, task_name, task_priority):
        if Todo.validate(task_name and task_priority > 0, ValueError('Name can not be empty and priority must be > 0')):
            if not self.find_task(task_name):
                self.cursor.execute("INSERT INTO `todo` (`name`, `priority`) VALUES (?, ?)", (task_name, task_priority))
                self.db.commit()
            else:
                print(f'Record with the name {task_name} exists already, skipping')

    def find_task(self, task_name):
        """
        The method returns the record found or None otherwise.
        """
        self.cursor.execute("SELECT * FROM todo WHERE `name`=?", (task_name,))
        result = self.cursor.fetchone()

        return result if result is not None else None

    def show_tasks(self):
        for record in self.cursor.execute('SELECT * FROM `todo`'):
            print(record)

    def change_priority(self, id_, task_priority):
        """
        The method should get the id of the task from the user and its new priority (greater than or equal to 1).
        """
        if Todo.validate(task_priority > 0 and id_ > 0, ValueError('Priority and task_id has to be > 0')):
            self.cursor.execute('UPDATE `todo` SET `priority`=? WHERE id=?', (task_priority, id_))

        self.db.commit()

    def delete_task(self, id_):
        """
        Responsible for deleting single tasks. The method should get the task id from the user.
        """
        if Todo.validate(id_ > 0, ValueError('Priority and task_id has to be > 0')):
            self.cursor.execute('DELETE FROM `todo` WHERE id=?', (id_,))

    @staticmethod
    def validate(expression, exc):
        if not expression:
            raise exc

        return True


    def __del__(self):
        print('Closing db connection ...')
        self.db.close()


def print_menu():
    print()
    print('1. Show tasks')
    print('2. Add task')
    print('3. Change priority')
    print('4. Delete task')
    print('5. Exit')


if __name__ == '__main__':
    todo = Todo()

    while True:
        print_menu()
        selected_op = int(input('Your choice: '))

        match selected_op:
            case 1:
                todo.show_tasks()

            case 2:
                name = input('Name: ')
                priority = int(input('Priority: '))
                todo.create_task(name, priority)

            case 3:
                task_id = int(input('Task ID: '))
                priority = int(input('Priority: '))
                todo.change_priority(task_id, priority)

            case 4:
                task_id = int(input('Task ID: '))
                todo.delete_task(task_id)

            case 5:
                del todo
                exit(0)
