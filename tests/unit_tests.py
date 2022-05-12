import copy
import unittest
from parameterized import parameterized
from main import search_name, add_doc, move_doc, del_doc
from main import documents, directories


class TestFunctionsUnitTest(unittest.TestCase):

    def setUp(self):
        self.docs = copy.deepcopy(documents)
        self.dirs = copy.deepcopy(directories)


    def test_search_name(self):
        self.assertEqual(search_name('11-2', self.docs), 'Геннадий Покемонов')

    def test_add_doc(self):
        result = add_doc('passport', '12345', 'owner', '1', self.docs, self.dirs)
        self.assertTrue(result)
        self.assertIn({'type': 'passport', 'number': '12345', 'name': 'owner'}, self.docs)
        self.assertIn('12345', self.dirs['1'])

    def test_del_doc(self):
        result = del_doc('11-2', self.docs, self.dirs)
        self.assertTrue(result)
        for self.doc in self.docs:
            self.assertNotEqual('11-2', self.doc['number'])
        for dir_ in self.dirs:
            self.assertNotIn('11-2', self.dirs[dir_])



    @parameterized.expand([
        ('11-2', '2'),
        ('2207 876234', '3')
    ])
    def test_move_doc(self, a, b):
        self.assertEqual(move_doc(a, b, self.docs, self.dirs), b)
        self.assertIn(a, self.dirs[b])


if __name__ == '__main__':
    unittest.main()
