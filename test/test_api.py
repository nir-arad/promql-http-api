import pytest
import promql_http_api
import datetime
from promql_http_api import PromqlHttpApi


@pytest.fixture
def dut():
    return PromqlHttpApi('http://localhost:9090')


def test_constructor(dut):
    assert isinstance(dut, PromqlHttpApi)


def test_query(dut):
    time = datetime.datetime.now()
    result = dut.query('up', time)
    assert isinstance(result, promql_http_api.Query)


def test_query_range(dut):
    time = datetime.datetime.now()
    result = dut.query_range('up', time, time, "1m")
    assert isinstance(result, promql_http_api.QueryRange)


def test_format_query(dut):
    result = dut.format_query('up')
    assert isinstance(result, promql_http_api.FormatQuery)


def test_series(dut):
    result = dut.series()
    assert isinstance(result, promql_http_api.Series)


def test_labels(dut):
    result = dut.labels()
    assert isinstance(result, promql_http_api.Labels)


def test_label_values(dut):
    result = dut.label_values('label')
    assert isinstance(result, promql_http_api.LabelValues)


def test_targets(dut):
    result = dut.targets()
    assert isinstance(result, promql_http_api.Targets)


def test_rules(dut):
    result = dut.rules()
    assert isinstance(result, promql_http_api.Rules)


def test_alerts(dut):
    result = dut.alerts()
    assert isinstance(result, promql_http_api.Alerts)


def test_alertmanagers(dut):
    result = dut.alertmanagers()
    assert isinstance(result, promql_http_api.AlertManagers)


def test_config(dut):
    result = dut.config()
    assert isinstance(result, promql_http_api.Config)


def test_flags(dut):
    result = dut.flags()
    assert isinstance(result, promql_http_api.Flags)


def test_runtimeinfo(dut):
    result = dut.runtimeinfo()
    assert isinstance(result, promql_http_api.RuntimeInfo)


def test_buildinfo(dut):
    result = dut.buildinfo()
    assert isinstance(result, promql_http_api.BuildInfo)
