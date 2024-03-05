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

import requests
from requests.exceptions import ConnectTimeout
import logging
from .http_config import http_retries, http_backoff


class ApiResponse:
    session = requests.Session()

    def __init__(self, url: str, *args, **kwargs):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.url = url
        self.retry = 'retries' in kwargs
        self.retries = kwargs.get('retries', http_retries)
        self.timeout = kwargs.get('timeout', None)
        self.backoff = kwargs.get('backoff', http_backoff)
        self.headers = kwargs.get('headers', {})
        self.response: requests.Response = None  # type: ignore
        self.get()

    def get(self):
        '''
        Get the response from the PromQL API
        Executes the HTTP GET request to the PromQL API

        Parameters:
            None
        Returns:
            None
        Exceptions:
            requests.exceptions.RequestException: If the HTTP GET request fails
        '''
        if self.response:
            return

        retries = self.retries
        timeout = self.timeout
        while retries > 0:
            try:
                self.logger.debug(f'HTTP GET url: {self.url}; headers: {self.headers}, timeout: {timeout}')
                self.response = ApiResponse.session.get(self.url, headers=self.headers, timeout=timeout)
                break
            except ConnectTimeout:
                self.logger.warning(f"HTTP connection timeout, {retries} retries remaining")
                retries -= 1
                timeout *= self.backoff
            except Exception as e:
                raise e
        if retries == 0:
            raise ConnectTimeout(f"HTTP GET request failed. URL: {self.url}; headers: {self.headers}")

    def http_response_ok(self):
        '''
        Is HTTP response OK?

        Parameters:
            None
        Returns:
            bool: True if HTTP response is OK, False otherwise
        '''
        if self.response is None:
            return False
        return self.response.status_code == 200

    def status(self):
        '''
        Get PromQL API response status

        Parameters:
            None
        Returns:
            status (str): The status of the PromQL API response
        '''
        if not self.http_response_ok():
            return None
        return self.response.json()['status']

    def data(self):
        '''
        Get PromQL API response data

        Parameters:
            None
        Returns:
            data (dict): The data of the PromQL API response
        '''
        if self.status() != 'success':
            return None
        return self.response.json()['data']

    def error_type(self):
        '''
        Get PromQL API response error type

        Parameters:
            None
        Returns:
            error_type (str): The error type of the PromQL API response
        '''
        if self.status() != 'error':
            return None
        return self.response.json()['errorType']

    def error(self):
        '''
        Get PromQL API response error string

        Parameters:
            None
        Returns:
            error (str): The error string of the PromQL API response
        '''
        if self.status() != 'error':
            return None
        return self.response.json()['error']

    def __str__(self):
        '''
        Convert response to string (json)

        Parameters:
            None
        Returns:
            str: The string representation of the response
        '''
        ret = ""
        ret += f"status_code: {self.response.status_code}, "
        ret += f"status: {self.status()}, "
        ret += f"data: {self.data()}"
        return ret
