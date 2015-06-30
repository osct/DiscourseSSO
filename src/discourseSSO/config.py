# Copyright 2015 INFN
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
SSO FLASK Application for Discourse main configuration file
"""

# Discourse URL to send the user back
DISCOURSE_URL = 'http://discuss.example.com'

# Secret key shared with the Discourse server
DISCOURSE_SECRET_KEY = 'd836444a9e4084d5b224a60c208dce14'

# Attribute to read from the environment after user validation
DISCOURSE_USER_MAP = {
    'name': ['givenName', 'sn'],
    'username': 'username',
    'external_id': 'eppn',
    'email': 'mail'
}
