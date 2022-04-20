import unittest
import math
from hypothesis import given
import hypothesis.strategies as st

from DicHashMap import Dic


class TestDicHashMap(unittest.TestCase):

    @given(st.integers(), st.integers())
    def test1_add(self, a, b):
        dic = Dic()
        dic.add(a, b)
        self.assertEqual(dic.to_list(), [(a, b)])

    @given(st.binary(), st.binary())
    def test2_add(self, a, b):
        dic = Dic()
        dic.add(a, b)
        self.assertEqual(dic.to_list(), [(a, b)])

    @given(st.text(), st.text())
    def test3_add(self, a, b):
        dic = Dic()
        dic.add(a, b)
        self.assertEqual(dic.to_list(), [(a, b)])

    @given(st.none(), st.none())
    def test4_add(self, a, b):
        dic = Dic()
        dic.add(a, b)
        self.assertEqual(dic.to_list(), [])

    @given(st.floats(), st.floats())
    def test5_add(self, a, b):
        dic = Dic()
        dic.add(a, b)
        self.assertEqual(dic.to_list(), [(a, b)])

    def test6_add(self):
        dic = Dic()
        a = None
        b = 1.2
        dic.add(a, b)
        self.assertEqual(dic.to_list(), [(a, b)])

    @given(st.integers(), st.integers())
    def test_set(self, a, b):
        dic = Dic()
        self.assertEqual(dic.to_list(), [])
        dic.add(a, b)
        self.assertEqual(dic.to_list(), [(a, b)])

    @given(st.floats(), st.floats())
    def test1_get(self, a, b):
        dic = Dic()
        dic.set(a, b)
        if math.isnan(b):
            self.assertEqual(math.isnan(dic.get(a)), True)
        else:
            self.assertEqual(dic.get(a), b)

    @given(st.integers(), st.integers())
    def test2_get(self, a, b):
        dic = Dic()
        dic.set(a, b)
        if math.isnan(b):
            self.assertEqual(math.isnan(dic.get(a)), True)
        else:
            self.assertEqual(dic.get(a), b)

    def test_get(self):
        dic = Dic()
        a = None
        b = 1.3
        dic.set(a, b)
        self.assertEqual(dic.get(a), b)
        c = float("nan")
        d = 1.2
        dic.set(c, d)
        self.assertEqual(dic.get(c), d)
        e = float("nan")
        f = float("nan")
        dic.set(e, f)
        self.assertEqual(math.isnan(dic.get(e)), True)
        g = "zpeng"
        h = "cpo"
        dic.set(g, h)
        self.assertEqual(dic.get(g), h)

    @given(st.floats(), st.floats(), st.floats())
    def test1_change(self, a, b, c):
        dic = Dic()
        dic.set(a, b)
        dic.change(a, c)
        if math.isnan(c):
            self.assertEqual(math.isnan(dic.get(a)), True)
        else:
            self.assertEqual(dic.get(a), c)

    @given(st.integers(), st.integers(), st.integers())
    def test2_change(self, a, b, c):
        dic = Dic()
        dic.set(a, b)
        dic.change(a, c)
        if math.isnan(c):
            self.assertEqual(math.isnan(dic.get(a)), True)
        else:
            self.assertEqual(dic.get(a), c)

    def test3_change(self):
        dic = Dic()
        dic.set(1, 2)
        dic.change(1, 3)
        self.assertEqual(dic.get(1), 3)

    @given(st.integers(), st.integers())
    def test_remove(self, a, b):
        dic = Dic()
        self.assertEqual(dic.remove(a), False)
        dic.set(a, b)
        self.assertEqual(dic.remove(a), True)

    def test1_size(self):
        self.assertEqual(Dic().size(), 0)
        dic = Dic()
        dic.set(1, 2)
        self.assertEqual(dic.size(), 1)
        dic.set(1, 2)
        self.assertEqual(dic.size(), 1)
        dic.set(2, 3)
        dic.set(3, 4)
        self.assertEqual(dic.size(), 3)

    @given(st.dictionaries(st.integers(), st.integers()))
    def test2_size(self, a):
        c = list(a.items())
        dic = Dic()
        dic.from_list(c)
        self.assertEqual(dic.size(), len(a))

    @given(st.dictionaries(st.floats(), st.floats()))
    def test3_size(self, a):
        c = list(a.items())
        dic = Dic()
        dic.from_list(c)
        self.assertEqual(dic.size(), len(a))

    @given(st.dictionaries(st.text(), st.text()))
    def test4_size(self, a):
        c = list(a.items())
        dic = Dic()
        dic.from_list(c)
        self.assertEqual(dic.size(), len(a))

    @given(st.integers(), st.integers())
    def test1_is_member_for_key(self, a, b):
        dic = Dic()
        dic.set(a, b)
        self.assertEqual(dic.is_member_for_key(a), True)

    def test2_is_member_for_key(self):
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
        self.assertEqual(dic.concat(None, (3, 4)).to_list(), [(3, 4)])
        self.assertEqual(dic.concat((1, 2), None).to_list(), [(1, 2)])
        self.assertEqual(dic.concat(None, None).to_list(), [])
        self.assertEqual(dic.concat(tem_dic, None).to_list(), x)
