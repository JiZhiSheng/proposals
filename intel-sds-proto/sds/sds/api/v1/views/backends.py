# Copyright (c) 2014 Intel Corporation
# Copyright (c) 2014 OpenStack Foundation
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

from sds.api import common
from sds.openstack.common import log as logging
LOG = logging.getLogger(__name__)


class ViewBuilder(common.ViewBuilder):

    def trim(self, storage_backend):
        trimmed = dict(id=storage_backend.get('id'),
                       name=storage_backend.get('name'),
                       capability_specs_id=storage_backend.get('capability_specs_id'),
                       config_specs_id=storage_backend.get('config_specs_id'))
        return trimmed

    def show(self, request, storage_backend, brief=False):
        """Trim away extraneous storage backend attributes."""
        return self.trim(storage_backend) if brief else dict(storage_backend=storage_backend)

    def list(self, request, storage_backend, brief=False):
        """Trim away extraneous storage backend attributes."""
        return self.trim(storage_backend) if brief else storage_backend

    def summary_list(self, request, storage_backends):
        """Index over trimmed volume types."""
        storage_backends_list = [self.list(request, storage_backend, True)
                                 for storage_backend in storage_backends]
        return dict(storage_backends=storage_backends_list)

    def detail_list(self, request, storage_backends):
        """Index over trimmed volume types."""
        storage_backends_list = [self.list(request, storage_backend, False)
                                 for storage_backend in storage_backends]
        return dict(storage_backends=storage_backends_list)
