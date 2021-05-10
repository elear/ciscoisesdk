# -*- coding: utf-8 -*-
"""Identity Services Engine getGuestUserById data model.

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


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
import json
from ciscoisesdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidatorC3C7D5A3A83D9F7441972D399(object):
    """getGuestUserById request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC3C7D5A3A83D9F7441972D399, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "GuestUser": {
                "properties": {
                "customFields": {
                "type": "object"
                },
                "guestAccessInfo": {
                "properties": {
                "fromDate": {
                "type": "string"
                },
                "location": {
                "type": "string"
                },
                "toDate": {
                "type": "string"
                },
                "validDays": {
                "type": "integer"
                }
                },
                "required": [
                "validDays",
                "fromDate",
                "toDate",
                "location"
                ],
                "type": "object"
                },
                "guestInfo": {
                "properties": {
                "creationTime": {
                "type": "string"
                },
                "enabled": {
                "type": "boolean"
                },
                "notificationLanguage": {
                "type": "string"
                },
                "password": {
                "type": "string"
                },
                "userName": {
                "type": "string"
                }
                },
                "required": [
                "userName",
                "password",
                "creationTime",
                "enabled",
                "notificationLanguage"
                ],
                "type": "object"
                },
                "guestType": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "link": {
                "properties": {
                "href": {
                "type": "string"
                },
                "rel": {
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "required": [
                "rel",
                "href",
                "type"
                ],
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "sponsorUserId": {
                "type": "string"
                },
                "sponsorUserName": {
                "type": "string"
                },
                "status": {
                "type": "string"
                }
                },
                "required": [
                "id",
                "name",
                "guestType",
                "status",
                "sponsorUserName",
                "sponsorUserId",
                "guestInfo",
                "guestAccessInfo",
                "customFields",
                "link"
                ],
                "type": "object"
                }
                },
                "required": [
                "GuestUser"
                ],
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )