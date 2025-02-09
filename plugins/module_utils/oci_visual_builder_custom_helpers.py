# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class VbInstanceActionsHelperCustom:
    def get_action_idempotent_states(self, action):
        action_idempotent_states = super(
            VbInstanceActionsHelperCustom, self
        ).get_action_idempotent_states(action)

        if action.lower() == "stop":
            return action_idempotent_states + [
                "INACTIVE",
            ]
        return action_idempotent_states
