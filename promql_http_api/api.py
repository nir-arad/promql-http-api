# SPDX-FileCopyrightText: Copyright (c) 2022 NVIDIA CORPORATION & AFFILIATES.
# SPDX-FileCopyrightText: All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .query import Query, QueryRange
from .format_query import FormatQuery
from .series import Series
from .labels import Labels
from .label_values import LabelValues
from .targets import Targets
from .rules import Rules
from .alerts import Alerts
from .alertsmanagers import AlertManagers
from .config import Config
from .flags import Flags
from .runtimeinfo import RuntimeInfo
from .buildinfo import BuildInfo


class PromqlHttpApi:
    '''
    The top level API class
    Provides a convenient function interface to instanciate
    API endpoint classes
    '''

    def __init__(self, url: str, headers: dict = {}):
        self.url = url
        self.headers = headers

    def _update_(self, args, kwargs) -> list:
        args = [self.url] + list(args)

        # Make a copy of the default headers
        headers = self.headers.copy()
        # API calls may override default headers
        k_headers = kwargs.get('headers', {})
        for key, value in k_headers.items():
            headers[key] = value
        kwargs['headers'] = headers

        return [args, kwargs]

    def query(self, *args, **kwargs) -> Query:
        '''
        Get a Query object
        '''
        args, kwargs = self._update_(args, kwargs)
        return Query(*args, **kwargs)

    def query_range(self, *args, **kwargs) -> QueryRange:
        '''
        Get a QueryRange object
        '''
        args, kwargs = self._update_(args, kwargs)
        return QueryRange(*args, **kwargs)

    def format_query(self, *args, **kwargs) -> FormatQuery:
        '''
        Get a FormatQuery object
        '''
        args, kwargs = self._update_(args, kwargs)
        return FormatQuery(*args, **kwargs)

    def series(self, *args, **kwargs) -> Series:
        '''
        Get a Series object
        '''
        args, kwargs = self._update_(args, kwargs)
        return Series(*args, **kwargs)

    def labels(self, *args, **kwargs) -> Labels:
        '''
        Get a Labels object
        '''
        args, kwargs = self._update_(args, kwargs)
        return Labels(*args, **kwargs)

    def label_values(self, *args, **kwargs) -> LabelValues:
        '''
        Get a LabelValues object
        '''
        args, kwargs = self._update_(args, kwargs)
        return LabelValues(*args, **kwargs)

    def targets(self, *args, **kwargs) -> Targets:
        '''
        Get a Targets object
        '''
        args, kwargs = self._update_(args, kwargs)
        return Targets(*args, **kwargs)

    def rules(self, *args, **kwargs) -> Rules:
        '''
        Get a Rules object
        '''
        args, kwargs = self._update_(args, kwargs)
        return Rules(*args, **kwargs)

    def alerts(self, *args, **kwargs) -> Alerts:
        '''
        Get an Alerts object
        '''
        args, kwargs = self._update_(args, kwargs)
        return Alerts(*args, **kwargs)

    def alertmanagers(self, *args, **kwargs) -> AlertManagers:
        '''
        Get an AlertManagers object
        '''
        args, kwargs = self._update_(args, kwargs)
        return AlertManagers(*args, **kwargs)

    def config(self, *args, **kwargs) -> Config:
        '''
        Get a Config object
        '''
        args, kwargs = self._update_(args, kwargs)
        return Config(*args, **kwargs)

    def flags(self, *args, **kwargs) -> Flags:
        '''
        Get a Flags object
        '''
        args, kwargs = self._update_(args, kwargs)
        return Flags(*args, **kwargs)

    def runtimeinfo(self, *args, **kwargs) -> RuntimeInfo:
        '''
        Get a RuntimeInfo object
        '''
        args, kwargs = self._update_(args, kwargs)
        return RuntimeInfo(*args, **kwargs)

    def buildinfo(self, *args, **kwargs) -> BuildInfo:
        '''
        Get a BuildInfo object
        '''
        args, kwargs = self._update_(args, kwargs)
        return BuildInfo(*args, **kwargs)
