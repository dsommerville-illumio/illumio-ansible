# -*- coding: utf-8 -*-

# Copyright 2022 Illumio, Inc. All Rights Reserved.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):

    DOCUMENTATION = r'''
options:
  pce_hostname:
    description:
      - URL or FQDN of Illumio Policy Compute Engine.
        C(pce_url) is an alias for C(pce_hostname).
      - Can be set with the environment variable C(ILLUMIO_PCE_HOST).
    type: str
    aliases: [ pce_url ]
    required: true
  pce_port:
    description:
      - HTTP(S) port used by the PCE.
      - Can be set with the environment variable C(ILLUMIO_PCE_PORT).
    type: int
    default: 443
  pce_org_id:
    description:
      - PCE Organization ID.
      - Can be set with the environment variable C(ILLUMIO_PCE_ORG_ID).
    type: int
    default: 1
  api_key_username:
    description:
      - Illumio PCE API key username.
      - Can be set with the environment variable C(ILLUMIO_API_KEY_USERNAME).
    type: str
    required: true
  api_key_secret:
    description:
      - Illumio PCE API key secret.
      - Can be set with the environment variable C(ILLUMIO_API_KEY_SECRET).
    type: str
    required: true
'''
