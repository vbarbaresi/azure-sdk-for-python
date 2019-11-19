# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineScaleSetUpdatePublicIPAddressConfiguration(Model):
    """Describes a virtual machines scale set IP Configuration's PublicIPAddress
    configuration.

    :param name: The publicIP address configuration name.
    :type name: str
    :param idle_timeout_in_minutes: The idle timeout of the public IP address.
    :type idle_timeout_in_minutes: int
    :param dns_settings: The dns settings to be applied on the publicIP
     addresses .
    :type dns_settings:
     ~azure.mgmt.compute.v2018_04_01.models.VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'idle_timeout_in_minutes': {'key': 'properties.idleTimeoutInMinutes', 'type': 'int'},
        'dns_settings': {'key': 'properties.dnsSettings', 'type': 'VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings'},
    }

    def __init__(self, *, name: str=None, idle_timeout_in_minutes: int=None, dns_settings=None, **kwargs) -> None:
        super(VirtualMachineScaleSetUpdatePublicIPAddressConfiguration, self).__init__(**kwargs)
        self.name = name
        self.idle_timeout_in_minutes = idle_timeout_in_minutes
        self.dns_settings = dns_settings