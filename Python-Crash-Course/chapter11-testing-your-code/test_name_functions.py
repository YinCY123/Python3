import unittest
import name_function


class NameTestCase(unittest.TestCase):
    """Test for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""

        formatted_name = name_function.get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, "Janis Joplin")


unittest.main()
