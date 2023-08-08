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

    def __init__(self, url: str):
        self.url = url

    def query(self, *args, **kwargs) -> Query:
        '''
        Get a Query object
        '''
        return Query(self.url, *args, **kwargs)

    def query_range(self, *args, **kwargs) -> QueryRange:
        '''
        Get a QueryRange object
        '''
        return QueryRange(self.url, *args, **kwargs)

    def format_query(self, *args, **kwargs) -> FormatQuery:
        '''
        Get a FormatQuery object
        '''
        return FormatQuery(self.url, *args, **kwargs)

    def series(self, *args, **kwargs) -> Series:
        '''
        Get a Series object
        '''
        return Series(self.url, *args, **kwargs)

    def labels(self, *args, **kwargs) -> Labels:
        '''
        Get a Labels object
        '''
        return Labels(self.url, *args, **kwargs)

    def label_values(self, *args, **kwargs) -> LabelValues:
        '''
        Get a LabelValues object
        '''
        return LabelValues(self.url, *args, **kwargs)

    def targets(self, *args, **kwargs) -> Targets:
        '''
        Get a Targets object
        '''
        return Targets(self.url, *args, **kwargs)

    def rules(self, *args, **kwargs) -> Rules:
        '''
        Get a Rules object
        '''
        return Rules(self.url, *args, **kwargs)

    def alerts(self, *args, **kwargs) -> Alerts:
        '''
        Get an Alerts object
        '''
        return Alerts(self.url, *args, **kwargs)

    def alertmanagers(self, *args, **kwargs) -> AlertManagers:
        '''
        Get an AlertManagers object
        '''
        return AlertManagers(self.url, *args, **kwargs)

    def config(self, *args, **kwargs) -> Config:
        '''
        Get a Config object
        '''
        return Config(self.url, *args, **kwargs)

    def flags(self, *args, **kwargs) -> Flags:
        '''
        Get a Flags object
        '''
        return Flags(self.url, *args, **kwargs)

    def runtimeinfo(self, *args, **kwargs) -> RuntimeInfo:
        '''
        Get a RuntimeInfo object
        '''
        return RuntimeInfo(self.url, *args, **kwargs)

    def buildinfo(self, *args, **kwargs) -> BuildInfo:
        '''
        Get a BuildInfo object
        '''
        return BuildInfo(self.url, *args, **kwargs)
