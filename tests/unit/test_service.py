# -*- coding: utf-8 -*-
# Copyright 2016 Open Permissions Platform Coalition
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import unicode_literals

import pytest
import voluptuous

import perch


def test_external_service_schema():
    service = {
        'service_type': 'external',
        'name': 'test',
        'organisation_id': 'an organisation ID',
        'created_by': 'someone'
    }

    valid = perch.Service.schema(service)

    assert valid['state'] == perch.State.approved.name
    assert 'location' not in valid


def test_nonexternal_service_schema():
    service = {
        'service_type': 'repository',
        'name': 'test',
        'organisation_id': 'an organisation ID',
        'location': 'http://test.url',
        'created_by': 'someone'
    }

    valid = perch.Service.schema(service)

    assert valid['state'] == perch.State.pending.name


def test_nonexternal_service_schema_without_location():
    service = {
        'service_type': 'repository',
        'name': 'test',
        'organisation_id': 'an organisation ID',
        'created_by': 'someone'
    }

    with pytest.raises(voluptuous.Invalid) as exc:
        perch.Service.schema(service)

    assert exc.value.path == ['location']