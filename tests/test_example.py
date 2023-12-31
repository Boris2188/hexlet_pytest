import pytest
from hexlet_pytest.example import reverse,to_strip,summa_n


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'
    assert reverse('Boris') == 'siroB'
    assert reverse('') == ''

def test_to_strip():
    assert to_strip('www.yandex.ru') == 'yandex'

def test_summa_n():
    t = 3
    assert summa_n(t) == 6


if __name__ == '__main__':
    pytest.main()
