import pytest
from hexlet_pytest.function import to_upper


test_case=[('loud nises', 'LOUD NISES'),
('helo world', 'HELO WORLD')

]
@pytest.mark.parametrize('text, result',test_case)
def test_to_upper(text,result):
    assert to_upper(text) == result
