# Copyright 2011 Denali Systems, Inc.
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
OSDs interface (1.1 extension).
"""

import urllib
from vsmclient import base


class Osd(base.Resource):
    """A osd is an extra block level storage to the OpenStack instances."""
    def __repr__(self):
        try:
            return "<OSD: %s>" % self.id
        except AttributeError:
            return "<OSD: summary>"

    def delete(self):
        """Delete this osd."""
        self.manager.delete(self)

    def update(self, **kwargs):
        """Update the display_name or display_description for this osd."""
        self.manager.update(self, **kwargs)

    def force_delete(self):
        """Delete the specified osd ignoring its current state.

        :param osd: The UUID of the osd to force-delete.
        """
        self.manager.force_delete(self)


class OsdManager(base.ManagerWithFind):
    """
    Manage :class:`OSD` resources.
    """
    resource_class = Osd

    def get(self, osd_id):
        """
        Get a osd.

        :param osd_id: The ID of the osd.
        :rtype: :class:`OSD`
        """
        return self._get("/osds/%s" % osd_id, "osd")

    def list(self, detailed=False, search_opts=None, paginate_opts=None):
        """
        Get a list of all osds.

        :rtype: list of :class:`OSD`
        """
        if search_opts is None:
            search_opts = {}

        if paginate_opts is None:
            paginate_opts = {}

        qparams = {}

        for opt, val in search_opts.iteritems():
            if val:
                qparams[opt] = val

        for opt, val in paginate_opts.iteritems():
            if val:
                qparams[opt] = val


        query_string = "?%s" % urllib.urlencode(qparams) if qparams else ""

        detail = ""
        if detailed:
            detail = "/detail"

        ret = self._list("/osds%s%s" % (detail, query_string),
                          "osds")
        return ret

    def restart(self, osd):
        self._action('restart', osd)

    def remove(self, osd):
        self._action('remove', osd)

    def delete(self, osd):
        self._delete("/osds/%s" % base.getid(osd))

    def restore(self, osd):
        self._action('restore', osd)

    def summary(self):
        """
        summary
        """
        url = "/osds/summary"
        return self._get(url, 'osd-summary')

    def _action(self, action, osd, info=None, **kwargs):
        """
        Perform a osd "action."
        """
        body = {action: info}
        self.run_hooks('modify_body_for_action', body, **kwargs)
        url = '/osds/%s/action' % base.getid(osd)
        return self.api.client.post(url, body=body)

