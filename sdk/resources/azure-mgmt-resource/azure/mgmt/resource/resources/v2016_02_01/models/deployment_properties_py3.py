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


class DeploymentProperties(Model):
    """Deployment properties.

    All required parameters must be populated in order to send to Azure.

    :param template: The template content. It can be a JObject or a well
     formed JSON string. Use only one of Template or TemplateLink.
    :type template: object
    :param template_link: The template URI. Use only one of Template or
     TemplateLink.
    :type template_link:
     ~azure.mgmt.resource.resources.v2016_02_01.models.TemplateLink
    :param parameters: Deployment parameters. It can be a JObject or a well
     formed JSON string. Use only one of Parameters or ParametersLink.
    :type parameters: object
    :param parameters_link: The parameters URI. Use only one of Parameters or
     ParametersLink.
    :type parameters_link:
     ~azure.mgmt.resource.resources.v2016_02_01.models.ParametersLink
    :param mode: Required. The deployment mode. Possible values include:
     'Incremental', 'Complete'
    :type mode: str or
     ~azure.mgmt.resource.resources.v2016_02_01.models.DeploymentMode
    :param debug_setting: The debug setting of the deployment.
    :type debug_setting:
     ~azure.mgmt.resource.resources.v2016_02_01.models.DebugSetting
    """

    _validation = {
        'mode': {'required': True},
    }

    _attribute_map = {
        'template': {'key': 'template', 'type': 'object'},
        'template_link': {'key': 'templateLink', 'type': 'TemplateLink'},
        'parameters': {'key': 'parameters', 'type': 'object'},
        'parameters_link': {'key': 'parametersLink', 'type': 'ParametersLink'},
        'mode': {'key': 'mode', 'type': 'DeploymentMode'},
        'debug_setting': {'key': 'debugSetting', 'type': 'DebugSetting'},
    }

    def __init__(self, *, mode, template=None, template_link=None, parameters=None, parameters_link=None, debug_setting=None, **kwargs) -> None:
        super(DeploymentProperties, self).__init__(**kwargs)
        self.template = template
        self.template_link = template_link
        self.parameters = parameters
        self.parameters_link = parameters_link
        self.mode = mode
        self.debug_setting = debug_setting