import pytest
from promql_http_api.api_endpoint import ApiEndpoint


@pytest.fixture
def dut():
    return ApiEndpoint('http://localhost:9090')


def test_constructor(dut):
    assert isinstance(dut, ApiEndpoint)


def test_logger(dut, caplog):
    dut.logger.info('test')
    for record in caplog.records:
        assert record.levelname != "INFO"
    assert "test" not in caplog.text


def test_pretty(dut):
    assert dut.pretty({'a': 1}) == '{\n    "a": 1\n}'


def test_call(dut):
    '''
    This test will raise an exception because make_url() is not implemented.
    '''
    with pytest.raises(NotImplementedError):
        dut()


def test_make_url(dut):
    with pytest.raises(NotImplementedError):
        dut.make_url()
