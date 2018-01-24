# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PartitionDataLossProgress(Model):
    """Information about a partition data loss user-induced operation.

    :param state: The state of the operation. Possible values include:
     'Invalid', 'Running', 'RollingBack', 'Completed', 'Faulted', 'Cancelled',
     'ForceCancelled'
    :type state: str or ~servicefabric.models.OperationState
    :param invoke_data_loss_result: Represents information about an operation
     in a terminal state (Completed or Faulted).
    :type invoke_data_loss_result: ~servicefabric.models.InvokeDataLossResult
    """

    _attribute_map = {
        'state': {'key': 'State', 'type': 'str'},
        'invoke_data_loss_result': {'key': 'InvokeDataLossResult', 'type': 'InvokeDataLossResult'},
    }

    def __init__(self, state=None, invoke_data_loss_result=None):
        super(PartitionDataLossProgress, self).__init__()
        self.state = state
        self.invoke_data_loss_result = invoke_data_loss_result
