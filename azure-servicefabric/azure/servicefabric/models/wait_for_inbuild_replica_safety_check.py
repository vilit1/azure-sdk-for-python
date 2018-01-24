# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .partition_safety_check import PartitionSafetyCheck


class WaitForInbuildReplicaSafetyCheck(PartitionSafetyCheck):
    """Safety check that waits for the replica build operation to finish. This
    indicates that there is a replica that is going through the copy or is
    providing data for building another replica. Bring the node down will abort
    this copy operation which are typically expensive involving data movements.

    :param kind: Constant filled by server.
    :type kind: str
    :param partition_id: Id of the partition which is undergoing the safety
     check.
    :type partition_id: str
    """

    _validation = {
        'kind': {'required': True},
    }

    def __init__(self, partition_id=None):
        super(WaitForInbuildReplicaSafetyCheck, self).__init__(partition_id=partition_id)
        self.kind = 'WaitForInbuildReplica'
