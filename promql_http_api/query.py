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

from datetime import datetime
from datetime import timezone
import logging
import pandas as pd
from .api_endpoint import ApiEndpoint


class Base(ApiEndpoint):
    '''
    Base class for Query and QueryRange endpoints
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timezone = timezone.utc
        self.time_format = "%Y-%m-%dT%H:%M:%S"
        self.schema: dict = None  # type: ignore
        self.prom_results: list = None  # type: ignore

    def to_dataframe(self):
        '''
        Convert the PromQL query results to a Pandas DataFrame
        Implicitly executes the query if it has not already been executed

        Parameters:
            None
        Returns:
            df (DataFrame): The query results as a Pandas DataFrame
        '''
        data = self.response.data()
        if data is None:
            return None

        self.prom_results = data['result']
        if len(self.prom_results) == 0:
            return None
        logging.debug(f'prom_results: {self.prom_results}')

        prom_result_type = data['resultType']
        if prom_result_type == 'vector':
            return self.to_dataframe_vector()
        elif prom_result_type == 'matrix':
            return self.to_dataframe_matrix()
        else:
            return None

    def to_dataframe_vector(self):
        '''
        Helper function to convert a vector result to a Pandas DataFrame
        '''
        records = []
        columns = self.get_columns()
        for result in self.prom_results:
            prom_metric = result['metric']
            columns: list[str] = \
                columns if columns else list(prom_metric.keys())
            record = [prom_metric[column] for column in columns]
            value = result['value']
            timestamp = value[0]
            timestr = self.timestamp_to_str(timestamp)
            result = self.cast(value[1])
            full_record = [timestr] + record + [result]
            logging.debug(f'record = {full_record}')
            records.append(full_record)
        columns = ['timestamp'] + columns + ['value']
        df = pd.DataFrame(records, columns=columns)
        return df

    def to_dataframe_matrix(self):
        records = []
        columns = self.get_columns()
        for result in self.prom_results:
            prom_metric = result['metric']
            values = result['values']
            columns = columns if columns else list(prom_metric.keys())
            record = [prom_metric[column] for column in columns]
            for value in values:
                timestamp = value[0]
                timestr = self.timestamp_to_str(timestamp)
                result = self.cast(value[1])
                full_record = [timestr] + record + [result]
                logging.debug(f'record = {full_record}')
                records.append(full_record)
        columns = ['timestamp'] + columns + ['value']
        df = pd.DataFrame(records, columns=columns)
        return df

    def get_columns(self) -> list:
        if self.schema:
            return self.schema['columns']
        else:
            return None  # type: ignore

    def timestamp_to_str(self, timestamp):
        date_time = datetime.fromtimestamp(timestamp)
        return date_time.astimezone(self.timezone).strftime(self.time_format)

    def cast(self, result):
        if self.schema:
            dtype: type = self.schema.get('dtype', str)
            result = dtype(result)
        return result


class Query(Base):
    '''
    Query API endpoint class
    '''

    def __init__(self,
                 url: str = None,    # type: ignore
                 query: str = None,  # type: ignore
                 time: str = None):  # type: ignore
        super().__init__(url)
        self.query: str = query
        self.time = time

    def __str__(self):
        return self.query

    def __repr__(self):
        return self.query

    def make_url(self):
        '''
        Make the URL for the API endpoint

        Parameters:
            None
        Returns:
            url (str): The URL for the API endpoint
        '''
        url = '/api/v1/query?query=' + self.query
        url += '&time=' + self.time if self.time else ''
        return url

    def to_dataframe(self, schema: dict = None):  # type: ignore
        if self.query is None:
            return None
        self.schema = schema
        self.__call__()
        return super().to_dataframe()


class QueryRange(Base):
    '''
    QueryRange API endpoint class
    '''

    def __init__(self,
                 url: str = None,    # type: ignore
                 query: str = None,  # type: ignore
                 start: str = None,  # type: ignore
                 end: str = None,    # type: ignore
                 step: str = None):  # type: ignore
        super().__init__(url)
        self.query = query
        self.start = start
        self.end = end
        self.step = step

    def __str__(self):
        return self.query

    def __repr__(self):
        return self.query

    def make_url(self):
        '''
        Make the URL for the API endpoint

        Parameters:
            None
        Returns:
            url (str): The URL for the API endpoint
        '''
        url = '/api/v1/query_range?query=' + self.query
        url += '&start=' + self.start
        url += '&end=' + self.end
        url += '&step=' + self.step
        return url

    def to_dataframe(self, schema: dict = None):  # type: ignore
        if self.query is None:
            return None
        self.schema = schema
        self.__call__()
        return super().to_dataframe()
