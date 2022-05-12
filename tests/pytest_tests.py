import pytest
from main import search_name, add_doc, move_doc, del_doc
from main import documents, directories

fixtures = [
    ('11-2', '2'),
    ('2207 876234', '3')

]


def test_search_name():
    assert search_name('11-2', documents) == 'Геннадий Покемонов'


def test_add_doc():
    result = add_doc('passport', '12345', 'owner', '1', documents, directories)
    assert result is True
    assert {'type': 'passport', 'number': '12345', 'name': 'owner'} in documents
    assert '12345' in directories['1']


def test_del_doc():
    result = del_doc('11-2', documents, directories)
    assert result is True
    for doc in documents:
        assert '11-2' not in doc['number']
    for dir_ in directories:
        assert '11-2' is not directories[dir_]


@pytest.mark.parametrize('a, b', fixtures)
def test_move_doc(a, b):
    assert move_doc(a, b, documents, directories) == b
    assert a in directories[b]
