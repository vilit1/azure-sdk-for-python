# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MonitoringOperations:
    """MonitoringOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.monitoring.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get_spark_job_list(
        self,
        x_ms_client_request_id: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.SparkJobListViewResponse":
        """Get list of spark applications for the workspace.

        :param x_ms_client_request_id: Can provide a guid, which is helpful for debugging and to
         provide better customer support.
        :type x_ms_client_request_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkJobListViewResponse, or the result of cls(response)
        :rtype: ~azure.synapse.monitoring.models.SparkJobListViewResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SparkJobListViewResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-12-01"
        accept = "application/json"

        # Construct URL
        url = self.get_spark_job_list.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", x_ms_client_request_id, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('SparkJobListViewResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_spark_job_list.metadata = {'url': '/monitoring/workloadTypes/spark/Applications'}  # type: ignore

    async def get_sql_job_query_string(
        self,
        x_ms_client_request_id: Optional[str] = None,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        skip: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.SqlQueryStringDataModel":
        """Get SQL OD/DW Query for the workspace.

        :param x_ms_client_request_id: Can provide a guid, which is helpful for debugging and to
         provide better customer support.
        :type x_ms_client_request_id: str
        :param filter:
        :type filter: str
        :param orderby:
        :type orderby: str
        :param skip:
        :type skip: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SqlQueryStringDataModel, or the result of cls(response)
        :rtype: ~azure.synapse.monitoring.models.SqlQueryStringDataModel
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SqlQueryStringDataModel"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-12-01"
        accept = "application/json"

        # Construct URL
        url = self.get_sql_job_query_string.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')
        if orderby is not None:
            query_parameters['$orderby'] = self._serialize.query("orderby", orderby, 'str')
        if skip is not None:
            query_parameters['skip'] = self._serialize.query("skip", skip, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", x_ms_client_request_id, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('SqlQueryStringDataModel', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_sql_job_query_string.metadata = {'url': '/monitoring/workloadTypes/sql/querystring'}  # type: ignore
