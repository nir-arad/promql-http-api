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

import json
import logging
from .api_response import ApiResponse


class ApiEndpoint:
    '''
    Base class for API endpoints
    '''

    def __init__(self, url: str):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.base_url = url
        self.response: ApiResponse = None  # type: ignore

    def pretty(self, msg: str):
        return json.dumps(msg, indent=4)

    def __call__(self, *args, **kwargs):
        url = self.base_url + self.make_url()
        if self.response is not None:
            return
        self.response = ApiResponse(url, *args, **kwargs)
        self.logger.debug('response = ' + self.pretty(str(self.response)))
        data = self.response.data()
        return data

    def make_url(self):
        '''
        Make the URL for the API endpoint.
        This method must be overridden by the subclass.

        Parameters:
            None
        Returns:
            url (str): The URL for the API endpoint
        '''
        raise NotImplementedError
