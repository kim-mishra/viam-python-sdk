from grpclib.server import Stream

from viam.errors import ResourceNotFoundError
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.component.board import (
    BoardServiceBase,
    GetDigitalInterruptValueRequest,
    GetDigitalInterruptValueResponse,
    GetGPIORequest,
    GetGPIOResponse,
    PWMFrequencyRequest,
    PWMFrequencyResponse,
    PWMRequest,
    PWMResponse,
    ReadAnalogReaderRequest,
    ReadAnalogReaderResponse,
    SetGPIORequest,
    SetGPIOResponse,
    SetPWMFrequencyRequest,
    SetPWMFrequencyResponse,
    SetPWMRequest,
    SetPWMResponse,
    StatusRequest,
    StatusResponse,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .board import Board


class BoardService(BoardServiceBase, ResourceRPCServiceBase[Board]):
    """
    gRPC Service for a Board
    """

    RESOURCE_TYPE = Board

    async def Status(self, stream: Stream[StatusRequest, StatusResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        status = await board.status(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = StatusResponse(status=status)
        await stream.send_message(response)

    async def SetGPIO(self, stream: Stream[SetGPIORequest, SetGPIOResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_resource(name)
            pin = await board.gpio_pin_by_name(request.pin)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await pin.set(request.high, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = SetGPIOResponse()
        await stream.send_message(response)

    async def GetGPIO(self, stream: Stream[GetGPIORequest, GetGPIOResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_resource(name)
            pin = await board.gpio_pin_by_name(request.pin)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        high = await pin.get(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetGPIOResponse(high=high)
        await stream.send_message(response)

    async def PWM(self, stream: Stream[PWMRequest, PWMResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_resource(name)
            pin = await board.gpio_pin_by_name(request.pin)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        pwm = await pin.get_pwm(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = PWMResponse(duty_cycle_pct=pwm)
        await stream.send_message(response)

    async def SetPWM(self, stream: Stream[SetPWMRequest, SetPWMResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_resource(name)
            pin = await board.gpio_pin_by_name(request.pin)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await pin.set_pwm(request.duty_cycle_pct, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = SetPWMResponse()
        await stream.send_message(response)

    async def PWMFrequency(self, stream: Stream[PWMFrequencyRequest, PWMFrequencyResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_resource(name)
            pin = await board.gpio_pin_by_name(request.pin)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        frequency = await pin.get_pwm_frequency(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = PWMFrequencyResponse(frequency_hz=frequency)
        await stream.send_message(response)

    async def SetPWMFrequency(self, stream: Stream[SetPWMFrequencyRequest, SetPWMFrequencyResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_resource(name)
            pin = await board.gpio_pin_by_name(request.pin)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await pin.set_pwm_frequency(request.frequency_hz, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = SetPWMFrequencyResponse()
        await stream.send_message(response)

    async def ReadAnalogReader(self, stream: Stream[ReadAnalogReaderRequest, ReadAnalogReaderResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.board_name
        try:
            board = self.get_resource(name)
            analog_reader = await board.analog_reader_by_name(request.analog_reader_name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        value = await analog_reader.read(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = ReadAnalogReaderResponse(value=value)
        await stream.send_message(response)

    async def GetDigitalInterruptValue(self, stream: Stream[GetDigitalInterruptValueRequest, GetDigitalInterruptValueResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.board_name
        try:
            board = self.get_resource(name)
            interrupt = await board.digital_interrupt_by_name(request.digital_interrupt_name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        value = await interrupt.value(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetDigitalInterruptValueResponse(value=value)
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        try:
            board = self.get_resource(request.name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await board.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
