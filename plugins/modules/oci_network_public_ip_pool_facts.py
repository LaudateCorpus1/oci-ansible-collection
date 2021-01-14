#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_network_public_ip_pool_facts
short_description: Fetches details about one or multiple PublicIpPool resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PublicIpPool resources in Oracle Cloud Infrastructure
    - Lists the PublicIpPool objects in the specified compartment.
      You can filter the list by using query parameters.
    - If I(public_ip_pool_id) is specified, the details of a single PublicIpPool will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    public_ip_pool_id:
        description:
            - The OCID of the Public Ip Pool object.
            - Required to get a specific public_ip_pool.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple public_ip_pools.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    byoip_range_id:
        description:
            - A filter to return only resources that match the given Byoip Range
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List public_ip_pools
  oci_network_public_ip_pool_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific public_ip_pool
  oci_network_public_ip_pool_facts:
    public_ip_pool_id: ocid1.publicippool.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
public_ip_pools:
    description:
        - List of PublicIpPool resources
    returned: on success
    type: complex
    contains:
        cidr_blocks:
            description:
                - The CIDRs that make up this pool
            returned: on success
            type: list
            sample: []
        compartment_id:
            description:
                - The OCID of the compartment containing the Public IP Pool
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The Oracle ID (OCID) of the Public Ip Pool.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The Public IP Pool's current state.
            returned: on success
            type: string
            sample: INACTIVE
        time_created:
            description:
                - The date and time the public IP Pool was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        items:
            description:
                - list of Public Ip pool object summaries
            returned: on success
            type: complex
            contains:
                compartment_id:
                    description:
                        - The OCID of the compartment containing the Public IP Pool
                    returned: on success
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                defined_tags:
                    description:
                        - Defined tags for this resource. Each key is predefined and scoped to a
                          namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                    returned: on success
                    type: dict
                    sample: {'Operations': {'CostCenter': 'US'}}
                display_name:
                    description:
                        - A user-friendly name. Does not have to be unique, and it's changeable.
                          Avoid entering confidential information.
                    returned: on success
                    type: string
                    sample: display_name_example
                freeform_tags:
                    description:
                        - Free-form tags for this resource. Each tag is a simple key-value pair with no
                          predefined name, type, or namespace. For more information, see L(Resource
                          Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                id:
                    description:
                        - The Oracle ID (OCID) of the Public Ip Pool.
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                lifecycle_state:
                    description:
                        - The Public IP Pool's current state.
                    returned: on success
                    type: string
                    sample: lifecycle_state_example
                time_created:
                    description:
                        - The date and time the public IP Pool was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
    sample: [{
        "cidr_blocks": [],
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "INACTIVE",
        "time_created": "2016-08-25T21:10:29.600Z",
        "items": [{
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "defined_tags": {'Operations': {'CostCenter': 'US'}},
            "display_name": "display_name_example",
            "freeform_tags": {'Department': 'Finance'},
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "lifecycle_state": "lifecycle_state_example",
            "time_created": "2016-08-25T21:10:29.600Z"
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PublicIpPoolFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "public_ip_pool_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_public_ip_pool,
            public_ip_pool_id=self.module.params.get("public_ip_pool_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "byoip_range_id",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_public_ip_pools,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


PublicIpPoolFactsHelperCustom = get_custom_class("PublicIpPoolFactsHelperCustom")


class ResourceFactsHelper(PublicIpPoolFactsHelperCustom, PublicIpPoolFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            public_ip_pool_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            byoip_range_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="public_ip_pool",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(public_ip_pools=result)


if __name__ == "__main__":
    main()
