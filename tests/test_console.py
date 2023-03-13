#!/usr/bin/python3
"""Module for TestHBNBCommand class."""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os


class TestHBNBCommand(unittest.TestCase):
    """
        Tests HBNBCommand console

    """

    def setUp(self):
        print("Testing Console methods")

    def test_help_quit(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        s = 'Quit command to exit the program\n'
        self.assertEqual(s, f.getvalue())

    def test_help_create(self):
        """Tests the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        s = 'Creates a new instance of BaseModel\n'
        self.assertEqual(s, f.getvalue())

    def test_help_clear(self):
        """Tests default"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help clear")
            s = 'Clear the screen\n'
            self.assertEqual(s, f.getvalue())

    def test_help_show(self):
        """Tests show"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            s = 'Prints the string representation of an instance\n'
            self.assertEqual(s, f.getvalue())

    def test_help_destroy(self):
        """Tests destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            s = 'Deletes an instance based on the class name and id\n'
            self.assertEqual(s, f.getvalue())

    def test_help_all(self):
        """Tests All"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            s = 'Prints all string representation of all instances\n'
            self.assertEqual(s, f.getvalue())

    def test_help_update(self):
        """Tests Update"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            s = 'Updates the class object\n'
            self.assertEqual(s, f.getvalue())


if __name__ == "__main__":
    unittest.main()
