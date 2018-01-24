# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeployedCodePackageInfo(Model):
    """Information about code package deployed on a Service Fabric node.

    :param name: The name of the code package.
    :type name: str
    :param version: The version of the code package specified in service
     manifest.
    :type version: str
    :param service_manifest_name: The name of service manifest that specified
     this code package.
    :type service_manifest_name: str
    :param service_package_activation_id: The ActivationId of a deployed
     service package. If ServicePackageActivationMode specified at the time of
     creating the service
     is 'SharedProcess' (or if it is not specified, in which case it defaults
     to 'SharedProcess'), then value of ServicePackageActivationId
     is always an empty string.
    :type service_package_activation_id: str
    :param host_type: Specifies the type of host for main entry point of a
     code package as specified in service manifest. Possible values include:
     'Invalid', 'ExeHost', 'ContainerHost'
    :type host_type: str or ~servicefabric.models.HostType
    :param host_isolation_mode: Specifies the isolation mode of main entry
     point of a code package when it's host type is ContainerHost. This is
     specified as part of container host policies in application manifest while
     importing service manifest. Possible values include: 'None', 'Process',
     'HyperV'
    :type host_isolation_mode: str or ~servicefabric.models.HostIsolationMode
    :param status: Specifies the status of a deployed application or service
     package on a Service Fabric node.
     . Possible values include: 'Invalid', 'Downloading', 'Activating',
     'Active', 'Upgrading', 'Deactivating'
    :type status: str or ~servicefabric.models.DeploymentStatus
    :param run_frequency_interval: The interval at which code package is run.
     This is used for periodic code package.
    :type run_frequency_interval: str
    :param setup_entry_point: Information about setup or main entry point of a
     code package deployed on a Service Fabric node.
    :type setup_entry_point: ~servicefabric.models.CodePackageEntryPoint
    :param main_entry_point: Information about setup or main entry point of a
     code package deployed on a Service Fabric node.
    :type main_entry_point: ~servicefabric.models.CodePackageEntryPoint
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'version': {'key': 'Version', 'type': 'str'},
        'service_manifest_name': {'key': 'ServiceManifestName', 'type': 'str'},
        'service_package_activation_id': {'key': 'ServicePackageActivationId', 'type': 'str'},
        'host_type': {'key': 'HostType', 'type': 'str'},
        'host_isolation_mode': {'key': 'HostIsolationMode', 'type': 'str'},
        'status': {'key': 'Status', 'type': 'str'},
        'run_frequency_interval': {'key': 'RunFrequencyInterval', 'type': 'str'},
        'setup_entry_point': {'key': 'SetupEntryPoint', 'type': 'CodePackageEntryPoint'},
        'main_entry_point': {'key': 'MainEntryPoint', 'type': 'CodePackageEntryPoint'},
    }

    def __init__(self, name=None, version=None, service_manifest_name=None, service_package_activation_id=None, host_type=None, host_isolation_mode=None, status=None, run_frequency_interval=None, setup_entry_point=None, main_entry_point=None):
        super(DeployedCodePackageInfo, self).__init__()
        self.name = name
        self.version = version
        self.service_manifest_name = service_manifest_name
        self.service_package_activation_id = service_package_activation_id
        self.host_type = host_type
        self.host_isolation_mode = host_isolation_mode
        self.status = status
        self.run_frequency_interval = run_frequency_interval
        self.setup_entry_point = setup_entry_point
        self.main_entry_point = main_entry_point
