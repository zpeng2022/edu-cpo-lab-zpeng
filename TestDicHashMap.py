import unittest

from hypothesis import given
import hypothesis.strategies as st

from DicHashMap import Dic 


class TestDicHashMap(unittest.TestCase):
   
    @given(st.integers(), st.integers())
    def test_add(self, a, b):
        dic = Dic()
        dic.add(a, b)
        self.assertEqual(dic.to_list(), [(a, b)])

    def test_set(self):
        dic = Dic()
        self.assertEqual(dic.to_list(), [])
        dic.add(1, 2)
        self.assertEqual(dic.to_list(), [(1, 2)])

    def test_get(self):
        dic = Dic()
        self.assertEqual(dic.get(1), None)
        dic.set(1, 2)
        self.assertEqual(dic.get(1), 2)

    def test_change(self):
        dic = Dic()
        dic.set(1, 2)
        dic.change(1, 3)
        self.assertEqual(dic.get(1), 3)

    def test_remove(self):
        dic = Dic()
        self.assertEqual(dic.remove(1), False)
        dic.set(1, 3)
        self.assertEqual(dic.remove(1), True)

    def test_size(self):
        self.assertEqual(Dic().size(), 0)
        dic = Dic()
        dic.set(1, 2)
        self.assertEqual(dic.size(), 1)
        dic.set(1, 2)
        self.assertEqual(dic.size(), 1)
        dic.set(2, 3)
        dic.set(3, 4)
        self.assertEqual(dic.size(), 3)

    def test_is_member_for_key(self):
        dic = Dic()
        dic.set(1, 3)
        self.assertEqual(dic.is_member_for_key(1), True)
        self.assertEqual(dic.is_member_for_key(2), False)

    def test_reverse(self):
        # dic is no order
        dic = Dic()
        self.assertEqual(dic.reverse(), True)

    def test_from_list(self):
        dic = Dic()
        dic.from_list([(1, 2), (1, 2), (1, 2), (1, 3)])
        self.assertEqual(dic.to_list(), [(1, 3)])
        dic.from_list([(1, 2), (1, 2), (1, 3), (1, 2)])
        self.assertEqual(dic.to_list(), [(1, 2)])

    def test_to_list(self):
        dic = Dic()
        self.assertEqual(dic.to_list(), [])
        dic.set(1, 2)
        self.assertEqual(dic.to_list(), [(1, 2)])
        dic.set(2, 3)
        dic.set(3, 4)
        self.assertEqual(dic.to_list(), [(1, 2), (2, 3), (3, 4)])

    def test_filter_the_value(self):
        dic = Dic()
        dic.from_list([(1, 2), (3, 4), (5, 6), (7, 7)])
        dic.filter_the_value(lambda x: x % 2 == 0)
        self.assertEqual(dic.to_list(), [(1, 2), (3, 4), (5, 6)])

    def test_map(self):
        dic = Dic()
        dic.from_list([(1, 2), (3, 4), (5, 6), (7, 7)])
        dic.map(lambda x: x + 1)
        self.assertEqual(dic.to_list(), [(1, 3), (3, 5), (5, 7), (7, 8)])

    def test_reduce(self):
        dic = Dic()
        dic.from_list([(1, 2), (3, 4), (5, 6), (7, 7)])
        dic.reduce(lambda x, state: x + 1 + 2 * state, 0)
        self.assertEqual(dic.to_list(), [(1, 3), (3, 5), (5, 7), (7, 8)])

    def test_iterator(self):
        x = [(1, 2), (3, 4), (5, 6), (7, 7)]
        dic = Dic()
        dic.from_list(x)
        tem = []
        for e in dic:
            tem.append(e)
        self.assertEqual(x, tem)

    def test_concat(self):
        x = [(1, 2), (3, 4), (5, 6), (7, 7)]
        tem_dic = Dic()
        tem_dic.from_list(x)
        dic = Dic()
        self.assertEqual(dic.concat((1, 2), (3, 4)).to_list(), [(1, 2), (3, 4)])
        self.assertEqual(dic.concat((1, 2), None).to_list(), [(1, 2)])
        self.assertEqual(dic.concat(None, None).to_list(), [])
        self.assertEqual(dic.concat(tem_dic, None).to_list(), x)
