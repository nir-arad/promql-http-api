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

import logging
from typing import Optional
from .api_endpoint import ApiEndpoint


class Series(ApiEndpoint):
    '''
    Series API endpoint class
    '''

    def __init__(
            self,
            url: str,
            match: Optional[str] = None,
            **kwargs):  # type: ignore
        super().__init__(url, **kwargs)
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.match = match

    def make_url(self):
        '''
        Make the URL for the API endpoint

        Parameters:
            None
        Returns:
            url (str): The URL for the API endpoint
        '''
        url = '/api/v1/series?'

        self.logger.debug(f'match = {self.match}')
        if isinstance(self.match, str):
            url += f'match[]={self.match}'
        elif isinstance(self.match, list):
            url += 'match[]='
            url += '&match[]='.join(self.match)
        else:
            raise Exception('match is required')
        return url
