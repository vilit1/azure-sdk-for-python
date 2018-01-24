# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .repair_impact_description_base import RepairImpactDescriptionBase


class NodeRepairImpactDescription(RepairImpactDescriptionBase):
    """Describes the expected impact of a repair on a set of nodes.
    This type supports the Service Fabric platform; it is not meant to be used
    directly from your code.
    .

    :param kind: Constant filled by server.
    :type kind: str
    :param node_impact_list: The list of nodes impacted by a repair action and
     their respective expected impact.
    :type node_impact_list: list[~servicefabric.models.NodeImpact]
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'Kind', 'type': 'str'},
        'node_impact_list': {'key': 'NodeImpactList', 'type': '[NodeImpact]'},
    }

    def __init__(self, node_impact_list=None):
        super(NodeRepairImpactDescription, self).__init__()
        self.node_impact_list = node_impact_list
        self.kind = 'Node'
