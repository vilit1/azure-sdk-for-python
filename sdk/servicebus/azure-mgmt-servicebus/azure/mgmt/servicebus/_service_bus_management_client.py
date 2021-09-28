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

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from msrest import Deserializer, Serializer

from ._configuration import ServiceBusManagementClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class ServiceBusManagementClient(MultiApiClientMixin, _SDKClient):
    """Azure Service Bus client.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2017-04-01'
    _PROFILE_TAG = "azure.mgmt.servicebus.ServiceBusManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        api_version=None, # type: Optional[str]
        base_url=None,  # type: Optional[str]
        profile=KnownProfiles.default, # type: KnownProfiles
        **kwargs  # type: Any
    ):
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ServiceBusManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(ServiceBusManagementClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-08-01: :mod:`v2015_08_01.models<azure.mgmt.servicebus.v2015_08_01.models>`
           * 2017-04-01: :mod:`v2017_04_01.models<azure.mgmt.servicebus.v2017_04_01.models>`
           * 2018-01-01-preview: :mod:`v2018_01_01_preview.models<azure.mgmt.servicebus.v2018_01_01_preview.models>`
           * 2021-01-01-preview: :mod:`v2021_01_01_preview.models<azure.mgmt.servicebus.v2021_01_01_preview.models>`
           * 2021-06-01-preview: :mod:`v2021_06_01_preview.models<azure.mgmt.servicebus.v2021_06_01_preview.models>`
        """
        if api_version == '2015-08-01':
            from .v2015_08_01 import models
            return models
        elif api_version == '2017-04-01':
            from .v2017_04_01 import models
            return models
        elif api_version == '2018-01-01-preview':
            from .v2018_01_01_preview import models
            return models
        elif api_version == '2021-01-01-preview':
            from .v2021_01_01_preview import models
            return models
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def disaster_recovery_configs(self):
        """Instance depends on the API version:

           * 2017-04-01: :class:`DisasterRecoveryConfigsOperations<azure.mgmt.servicebus.v2017_04_01.operations.DisasterRecoveryConfigsOperations>`
           * 2018-01-01-preview: :class:`DisasterRecoveryConfigsOperations<azure.mgmt.servicebus.v2018_01_01_preview.operations.DisasterRecoveryConfigsOperations>`
           * 2021-01-01-preview: :class:`DisasterRecoveryConfigsOperations<azure.mgmt.servicebus.v2021_01_01_preview.operations.DisasterRecoveryConfigsOperations>`
           * 2021-06-01-preview: :class:`DisasterRecoveryConfigsOperations<azure.mgmt.servicebus.v2021_06_01_preview.operations.DisasterRecoveryConfigsOperations>`
        """
        api_version = self._get_api_version('disaster_recovery_configs')
        if api_version == '2017-04-01':
            from .v2017_04_01.operations import DisasterRecoveryConfigsOperations as OperationClass
        elif api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import DisasterRecoveryConfigsOperations as OperationClass
        elif api_version == '2021-01-01-preview':
            from .v2021_01_01_preview.operations import DisasterRecoveryConfigsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import DisasterRecoveryConfigsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'disaster_recovery_configs'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def event_hubs(self):
        """Instance depends on the API version:

           * 2017-04-01: :class:`EventHubsOperations<azure.mgmt.servicebus.v2017_04_01.operations.EventHubsOperations>`
           * 2018-01-01-preview: :class:`EventHubsOperations<azure.mgmt.servicebus.v2018_01_01_preview.operations.EventHubsOperations>`
        """
        api_version = self._get_api_version('event_hubs')
        if api_version == '2017-04-01':
            from .v2017_04_01.operations import EventHubsOperations as OperationClass
        elif api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import EventHubsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'event_hubs'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def migration_configs(self):
        """Instance depends on the API version:

           * 2017-04-01: :class:`MigrationConfigsOperations<azure.mgmt.servicebus.v2017_04_01.operations.MigrationConfigsOperations>`
           * 2018-01-01-preview: :class:`MigrationConfigsOperations<azure.mgmt.servicebus.v2018_01_01_preview.operations.MigrationConfigsOperations>`
           * 2021-01-01-preview: :class:`MigrationConfigsOperations<azure.mgmt.servicebus.v2021_01_01_preview.operations.MigrationConfigsOperations>`
           * 2021-06-01-preview: :class:`MigrationConfigsOperations<azure.mgmt.servicebus.v2021_06_01_preview.operations.MigrationConfigsOperations>`
        """
        api_version = self._get_api_version('migration_configs')
        if api_version == '2017-04-01':
            from .v2017_04_01.operations import MigrationConfigsOperations as OperationClass
        elif api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import MigrationConfigsOperations as OperationClass
        elif api_version == '2021-01-01-preview':
            from .v2021_01_01_preview.operations import MigrationConfigsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import MigrationConfigsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'migration_configs'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def namespaces(self):
        """Instance depends on the API version:

           * 2015-08-01: :class:`NamespacesOperations<azure.mgmt.servicebus.v2015_08_01.operations.NamespacesOperations>`
           * 2017-04-01: :class:`NamespacesOperations<azure.mgmt.servicebus.v2017_04_01.operations.NamespacesOperations>`
           * 2018-01-01-preview: :class:`NamespacesOperations<azure.mgmt.servicebus.v2018_01_01_preview.operations.NamespacesOperations>`
           * 2021-01-01-preview: :class:`NamespacesOperations<azure.mgmt.servicebus.v2021_01_01_preview.operations.NamespacesOperations>`
           * 2021-06-01-preview: :class:`NamespacesOperations<azure.mgmt.servicebus.v2021_06_01_preview.operations.NamespacesOperations>`
        """
        api_version = self._get_api_version('namespaces')
        if api_version == '2015-08-01':
            from .v2015_08_01.operations import NamespacesOperations as OperationClass
        elif api_version == '2017-04-01':
            from .v2017_04_01.operations import NamespacesOperations as OperationClass
        elif api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import NamespacesOperations as OperationClass
        elif api_version == '2021-01-01-preview':
            from .v2021_01_01_preview.operations import NamespacesOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import NamespacesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'namespaces'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2015-08-01: :class:`Operations<azure.mgmt.servicebus.v2015_08_01.operations.Operations>`
           * 2017-04-01: :class:`Operations<azure.mgmt.servicebus.v2017_04_01.operations.Operations>`
           * 2018-01-01-preview: :class:`Operations<azure.mgmt.servicebus.v2018_01_01_preview.operations.Operations>`
           * 2021-01-01-preview: :class:`Operations<azure.mgmt.servicebus.v2021_01_01_preview.operations.Operations>`
           * 2021-06-01-preview: :class:`Operations<azure.mgmt.servicebus.v2021_06_01_preview.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2015-08-01':
            from .v2015_08_01.operations import Operations as OperationClass
        elif api_version == '2017-04-01':
            from .v2017_04_01.operations import Operations as OperationClass
        elif api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import Operations as OperationClass
        elif api_version == '2021-01-01-preview':
            from .v2021_01_01_preview.operations import Operations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def premium_messaging_regions(self):
        """Instance depends on the API version:

           * 2017-04-01: :class:`PremiumMessagingRegionsOperations<azure.mgmt.servicebus.v2017_04_01.operations.PremiumMessagingRegionsOperations>`
           * 2018-01-01-preview: :class:`PremiumMessagingRegionsOperations<azure.mgmt.servicebus.v2018_01_01_preview.operations.PremiumMessagingRegionsOperations>`
        """
        api_version = self._get_api_version('premium_messaging_regions')
        if api_version == '2017-04-01':
            from .v2017_04_01.operations import PremiumMessagingRegionsOperations as OperationClass
        elif api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import PremiumMessagingRegionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'premium_messaging_regions'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_endpoint_connections(self):
        """Instance depends on the API version:

           * 2018-01-01-preview: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.servicebus.v2018_01_01_preview.operations.PrivateEndpointConnectionsOperations>`
           * 2021-01-01-preview: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.servicebus.v2021_01_01_preview.operations.PrivateEndpointConnectionsOperations>`
           * 2021-06-01-preview: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.servicebus.v2021_06_01_preview.operations.PrivateEndpointConnectionsOperations>`
        """
        api_version = self._get_api_version('private_endpoint_connections')
        if api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2021-01-01-preview':
            from .v2021_01_01_preview.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import PrivateEndpointConnectionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_endpoint_connections'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_link_resources(self):
        """Instance depends on the API version:

           * 2018-01-01-preview: :class:`PrivateLinkResourcesOperations<azure.mgmt.servicebus.v2018_01_01_preview.operations.PrivateLinkResourcesOperations>`
           * 2021-01-01-preview: :class:`PrivateLinkResourcesOperations<azure.mgmt.servicebus.v2021_01_01_preview.operations.PrivateLinkResourcesOperations>`
           * 2021-06-01-preview: :class:`PrivateLinkResourcesOperations<azure.mgmt.servicebus.v2021_06_01_preview.operations.PrivateLinkResourcesOperations>`
        """
        api_version = self._get_api_version('private_link_resources')
        if api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2021-01-01-preview':
            from .v2021_01_01_preview.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import PrivateLinkResourcesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_link_resources'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def queues(self):
        """Instance depends on the API version:

           * 2015-08-01: :class:`QueuesOperations<azure.mgmt.servicebus.v2015_08_01.operations.QueuesOperations>`
           * 2017-04-01: :class:`QueuesOperations<azure.mgmt.servicebus.v2017_04_01.operations.QueuesOperations>`
           * 2018-01-01-preview: :class:`QueuesOperations<azure.mgmt.servicebus.v2018_01_01_preview.operations.QueuesOperations>`
           * 2021-01-01-preview: :class:`QueuesOperations<azure.mgmt.servicebus.v2021_01_01_preview.operations.QueuesOperations>`
           * 2021-06-01-preview: :class:`QueuesOperations<azure.mgmt.servicebus.v2021_06_01_preview.operations.QueuesOperations>`
        """
        api_version = self._get_api_version('queues')
        if api_version == '2015-08-01':
            from .v2015_08_01.operations import QueuesOperations as OperationClass
        elif api_version == '2017-04-01':
            from .v2017_04_01.operations import QueuesOperations as OperationClass
        elif api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import QueuesOperations as OperationClass
        elif api_version == '2021-01-01-preview':
            from .v2021_01_01_preview.operations import QueuesOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import QueuesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'queues'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def regions(self):
        """Instance depends on the API version:

           * 2017-04-01: :class:`RegionsOperations<azure.mgmt.servicebus.v2017_04_01.operations.RegionsOperations>`
           * 2018-01-01-preview: :class:`RegionsOperations<azure.mgmt.servicebus.v2018_01_01_preview.operations.RegionsOperations>`
        """
        api_version = self._get_api_version('regions')
        if api_version == '2017-04-01':
            from .v2017_04_01.operations import RegionsOperations as OperationClass
        elif api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import RegionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'regions'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def rules(self):
        """Instance depends on the API version:

           * 2017-04-01: :class:`RulesOperations<azure.mgmt.servicebus.v2017_04_01.operations.RulesOperations>`
           * 2018-01-01-preview: :class:`RulesOperations<azure.mgmt.servicebus.v2018_01_01_preview.operations.RulesOperations>`
           * 2021-01-01-preview: :class:`RulesOperations<azure.mgmt.servicebus.v2021_01_01_preview.operations.RulesOperations>`
           * 2021-06-01-preview: :class:`RulesOperations<azure.mgmt.servicebus.v2021_06_01_preview.operations.RulesOperations>`
        """
        api_version = self._get_api_version('rules')
        if api_version == '2017-04-01':
            from .v2017_04_01.operations import RulesOperations as OperationClass
        elif api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import RulesOperations as OperationClass
        elif api_version == '2021-01-01-preview':
            from .v2021_01_01_preview.operations import RulesOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import RulesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'rules'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def subscriptions(self):
        """Instance depends on the API version:

           * 2015-08-01: :class:`SubscriptionsOperations<azure.mgmt.servicebus.v2015_08_01.operations.SubscriptionsOperations>`
           * 2017-04-01: :class:`SubscriptionsOperations<azure.mgmt.servicebus.v2017_04_01.operations.SubscriptionsOperations>`
           * 2018-01-01-preview: :class:`SubscriptionsOperations<azure.mgmt.servicebus.v2018_01_01_preview.operations.SubscriptionsOperations>`
           * 2021-01-01-preview: :class:`SubscriptionsOperations<azure.mgmt.servicebus.v2021_01_01_preview.operations.SubscriptionsOperations>`
           * 2021-06-01-preview: :class:`SubscriptionsOperations<azure.mgmt.servicebus.v2021_06_01_preview.operations.SubscriptionsOperations>`
        """
        api_version = self._get_api_version('subscriptions')
        if api_version == '2015-08-01':
            from .v2015_08_01.operations import SubscriptionsOperations as OperationClass
        elif api_version == '2017-04-01':
            from .v2017_04_01.operations import SubscriptionsOperations as OperationClass
        elif api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import SubscriptionsOperations as OperationClass
        elif api_version == '2021-01-01-preview':
            from .v2021_01_01_preview.operations import SubscriptionsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import SubscriptionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'subscriptions'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def topics(self):
        """Instance depends on the API version:

           * 2015-08-01: :class:`TopicsOperations<azure.mgmt.servicebus.v2015_08_01.operations.TopicsOperations>`
           * 2017-04-01: :class:`TopicsOperations<azure.mgmt.servicebus.v2017_04_01.operations.TopicsOperations>`
           * 2018-01-01-preview: :class:`TopicsOperations<azure.mgmt.servicebus.v2018_01_01_preview.operations.TopicsOperations>`
           * 2021-01-01-preview: :class:`TopicsOperations<azure.mgmt.servicebus.v2021_01_01_preview.operations.TopicsOperations>`
           * 2021-06-01-preview: :class:`TopicsOperations<azure.mgmt.servicebus.v2021_06_01_preview.operations.TopicsOperations>`
        """
        api_version = self._get_api_version('topics')
        if api_version == '2015-08-01':
            from .v2015_08_01.operations import TopicsOperations as OperationClass
        elif api_version == '2017-04-01':
            from .v2017_04_01.operations import TopicsOperations as OperationClass
        elif api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import TopicsOperations as OperationClass
        elif api_version == '2021-01-01-preview':
            from .v2021_01_01_preview.operations import TopicsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import TopicsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'topics'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
