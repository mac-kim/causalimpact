# Copyright 2014 Google Inc. All rights reserved.
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

# We used setup.py from the requests library as reference:
# https://github.com/requests/requests/blob/master/setup.py

"""
General fixtures for tests.
"""
import os

import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def fix_path():
    p = os.path.dirname(os.path.abspath(__file__))
    p = os.path.join(p, 'fixtures')
    return p


@pytest.fixture
def rand_data():
    return pd.DataFrame(np.random.randn(200, 3), columns=["y", "x1", "x2"])


@pytest.fixture
def date_rand_data(rand_data):
    date_rand_data = rand_data.set_index(pd.date_range(
        start='20180101',
        periods=len(rand_data))
    )
    return date_rand_data


@pytest.fixture
def pre_int_period():
    return [0, 99]


@pytest.fixture
def post_int_period():
    return [100, 199]


@pytest.fixture
def pre_str_period():
    return ['20180101', '20180410']


@pytest.fixture
def post_str_period():
    return ['20180411', '20180719']
