from typing import Any, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandResponse, DoCommandRequest
from viam.proto.component.sensor import (
    GetReadingsRequest,
    GetReadingsResponse,
    SensorServiceStub,
)
from viam.utils import dict_to_struct, struct_to_dict, sensor_readings_value_to_native, ValueTypes

from .sensor import Sensor


class SensorClient(Sensor):
    """
    gRPC client for the Sensor component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = SensorServiceStub(channel)
        super().__init__(name)

    async def get_readings(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None) -> Mapping[str, Any]:
        if extra is None:
            extra = {}
        request = GetReadingsRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetReadingsResponse = await self.client.GetReadings(request, timeout=timeout)
        return sensor_readings_value_to_native(response.readings)

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
