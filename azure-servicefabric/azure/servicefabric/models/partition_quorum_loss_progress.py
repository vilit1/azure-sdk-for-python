# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PartitionQuorumLossProgress(Model):
    """Information about a partition quorum loss user-induced operation.

    :param state: The state of the operation. Possible values include:
     'Invalid', 'Running', 'RollingBack', 'Completed', 'Faulted', 'Cancelled',
     'ForceCancelled'
    :type state: str or ~servicefabric.models.OperationState
    :param invoke_quorum_loss_result: Represents information about an
     operation in a terminal state (Completed or Faulted).
    :type invoke_quorum_loss_result:
     ~servicefabric.models.InvokeQuorumLossResult
    """

    _attribute_map = {
        'state': {'key': 'State', 'type': 'str'},
        'invoke_quorum_loss_result': {'key': 'InvokeQuorumLossResult', 'type': 'InvokeQuorumLossResult'},
    }

    def __init__(self, state=None, invoke_quorum_loss_result=None):
        super(PartitionQuorumLossProgress, self).__init__()
        self.state = state
        self.invoke_quorum_loss_result = invoke_quorum_loss_result
