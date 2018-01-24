# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PropertyDescription(Model):
    """Description of a Service Fabric property.

    :param property_name: The name of the Service Fabric property.
    :type property_name: str
    :param custom_type_id: The property's custom type id. Using this property,
     the user is able to tag the type of the value of the property.
    :type custom_type_id: str
    :param value: Describes a Service Fabric property value.
    :type value: ~servicefabric.models.PropertyValue
    """

    _validation = {
        'property_name': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'property_name': {'key': 'PropertyName', 'type': 'str'},
        'custom_type_id': {'key': 'CustomTypeId', 'type': 'str'},
        'value': {'key': 'Value', 'type': 'PropertyValue'},
    }

    def __init__(self, property_name, value, custom_type_id=None):
        super(PropertyDescription, self).__init__()
        self.property_name = property_name
        self.custom_type_id = custom_type_id
        self.value = value
