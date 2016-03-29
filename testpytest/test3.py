"""Experiment for using pytest to mark tests for different environment.
"""
import pytest

@pytest.fixture(scope='function', params=None, autouse=False):
    def only_on_controller(request):
        if not request.on_controller:
            raise Exception('Not working for none controller environment')


@pytest.fixture(scope='function', params=None, autouse=False):
    def only_on_server(request):
        pass

@pytest.fixture(scope='function', params=None, autouse=False):
    def both_controller_server(request):
        pass


from mfgtest.lib.mfg_query import query_pdb, query_ctl
from mfgtest.lib.utest import only_on_server


def test_query_pdb(only_on_server):
    assert query_pdb('a6') == []
