import unittest
from tkinter import Tk
from src.todo import todo  

class TestTodoApp(unittest.TestCase):
    def test_todo_class_initialization(self):
        root = Tk()
        app = todo(root)
        self.assertIsInstance(app, todo)

if __name__ == '__main__':
    unittest.main()