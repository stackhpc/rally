# Copyright 2013: Mirantis Inc.
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

from pbr import version as pbr_version

from rally.common.db import schema

RALLY_VENDOR = "OpenStack Foundation"
RALLY_PRODUCT = "OpenStack Rally"
RALLY_PACKAGE = None  # OS distro package version suffix

loaded = False
version_info = pbr_version.VersionInfo("rally")


def version_string():
    return version_info.semantic_version().debian_string()


def database_revision():
    return schema.schema_revision(detailed=True)
