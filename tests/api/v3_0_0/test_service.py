# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI service API fixtures and tests.

Copyright (c) 2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import pytest
from fastjsonschema.exceptions import JsonSchemaException
from ciscoisesdk.exceptions import MalformedRequest
from tests.environment import IDENTITY_SERVICES_ENGINE_VERSION

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.0.0', reason='version does not match')


def is_valid_get_all_service(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_a14b837d975e5666860b664edde58837_v3_0_0').validate(obj.response)
    return True


def get_all_service(api):
    endpoint_result = api.service.get_all_service(

    )
    return endpoint_result


@pytest.mark.service
def test_get_all_service(api, validator):
    try:
        assert is_valid_get_all_service(
            validator,
            get_all_service(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_service_default(api):
    endpoint_result = api.service.get_all_service(

    )
    return endpoint_result


@pytest.mark.service
def test_get_all_service_default(api, validator):
    try:
        assert is_valid_get_all_service(
            validator,
            get_all_service_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_service_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_64cd4f6723b55471b856d3cc743f7b33_v3_0_0').validate(obj.response)
    return True


def get_service_by_name(api):
    endpoint_result = api.service.get_service_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.service
def test_get_service_by_name(api, validator):
    try:
        assert is_valid_get_service_by_name(
            validator,
            get_service_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_service_by_name_default(api):
    endpoint_result = api.service.get_service_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.service
def test_get_service_by_name_default(api, validator):
    try:
        assert is_valid_get_service_by_name(
            validator,
            get_service_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e