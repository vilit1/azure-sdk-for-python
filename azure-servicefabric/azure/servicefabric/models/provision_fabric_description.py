# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ProvisionFabricDescription(Model):
    """Describes the parameters for provisioning a cluster.

    :param code_file_path: The cluster code package file path.
    :type code_file_path: str
    :param cluster_manifest_file_path: The cluster manifest file path.
    :type cluster_manifest_file_path: str
    """

    _attribute_map = {
        'code_file_path': {'key': 'CodeFilePath', 'type': 'str'},
        'cluster_manifest_file_path': {'key': 'ClusterManifestFilePath', 'type': 'str'},
    }

    def __init__(self, code_file_path=None, cluster_manifest_file_path=None):
        super(ProvisionFabricDescription, self).__init__()
        self.code_file_path = code_file_path
        self.cluster_manifest_file_path = cluster_manifest_file_path
