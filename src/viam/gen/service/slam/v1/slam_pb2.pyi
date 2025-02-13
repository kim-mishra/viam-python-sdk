"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
from .... import common
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetPositionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of slam service'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetPositionRequest = GetPositionRequest

@typing_extensions.final
class GetPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int

    @property
    def pose(self) -> common.v1.common_pb2.PoseInFrame:
        """Current position of the robot within the World frame."""

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, pose: common.v1.common_pb2.PoseInFrame | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra', 'pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'pose', b'pose']) -> None:
        ...
global___GetPositionResponse = GetPositionResponse

@typing_extensions.final
class GetMapRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    CAMERA_POSITION_FIELD_NUMBER: builtins.int
    INCLUDE_ROBOT_MARKER_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of slam service'
    mime_type: builtins.str
    'Requested MIME type of response (image/jpeg or image/pcd)'

    @property
    def camera_position(self) -> common.v1.common_pb2.Pose:
        """Optional parameter for image/jpeg mime_type, used to project point
        cloud into a 2D image.
        """
    include_robot_marker: builtins.bool
    'Optional parameter for image/jpeg mime_type, defaults to false.\n    Tells us whether to include the robot position on the 2D image.\n    '

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., mime_type: builtins.str=..., camera_position: common.v1.common_pb2.Pose | None=..., include_robot_marker: builtins.bool=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_camera_position', b'_camera_position', 'camera_position', b'camera_position', 'extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_camera_position', b'_camera_position', 'camera_position', b'camera_position', 'extra', b'extra', 'include_robot_marker', b'include_robot_marker', 'mime_type', b'mime_type', 'name', b'name']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_camera_position', b'_camera_position']) -> typing_extensions.Literal['camera_position'] | None:
        ...
global___GetMapRequest = GetMapRequest

@typing_extensions.final
class GetMapResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POINT_CLOUD_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int

    @property
    def point_cloud(self) -> common.v1.common_pb2.PointCloudObject:
        ...
    image: builtins.bytes
    mime_type: builtins.str
    'Actual MIME type of response (image/jpeg or image/pcd)'

    def __init__(self, *, point_cloud: common.v1.common_pb2.PointCloudObject | None=..., image: builtins.bytes=..., mime_type: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['image', b'image', 'map', b'map', 'point_cloud', b'point_cloud']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['image', b'image', 'map', b'map', 'mime_type', b'mime_type', 'point_cloud', b'point_cloud']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['map', b'map']) -> typing_extensions.Literal['point_cloud', 'image'] | None:
        ...
global___GetMapResponse = GetMapResponse

@typing_extensions.final
class GetPositionNewRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of slam service'

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetPositionNewRequest = GetPositionNewRequest

@typing_extensions.final
class GetPositionNewResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSE_FIELD_NUMBER: builtins.int
    COMPONENT_REFERENCE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int

    @property
    def pose(self) -> common.v1.common_pb2.Pose:
        """Current position of the specified component in the SLAM Map"""
    component_reference: builtins.str
    'This is usually the name of the camera that is in the SLAM config'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional information in the response"""

    def __init__(self, *, pose: common.v1.common_pb2.Pose | None=..., component_reference: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra', 'pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['component_reference', b'component_reference', 'extra', b'extra', 'pose', b'pose']) -> None:
        ...
global___GetPositionNewResponse = GetPositionNewResponse

@typing_extensions.final
class GetPointCloudMapRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of slam service'

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetPointCloudMapRequest = GetPointCloudMapRequest

@typing_extensions.final
class GetPointCloudMapResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POINT_CLOUD_PCD_FIELD_NUMBER: builtins.int
    point_cloud_pcd: builtins.bytes
    'pointclouds are returned as a set of bytes in the standard PCD format\n    https://pointclouds.org/documentation/tutorials/pcd_file_format.html\n    '

    def __init__(self, *, point_cloud_pcd: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['point_cloud_pcd', b'point_cloud_pcd']) -> None:
        ...
global___GetPointCloudMapResponse = GetPointCloudMapResponse

@typing_extensions.final
class GetInternalStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of slam service'

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetInternalStateRequest = GetInternalStateRequest

@typing_extensions.final
class GetInternalStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INTERNAL_STATE_FIELD_NUMBER: builtins.int
    internal_state: builtins.bytes
    'A chunk of the internal state of the SLAM algorithm required to continue\n    mapping/localization\n    '

    def __init__(self, *, internal_state: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['internal_state', b'internal_state']) -> None:
        ...
global___GetInternalStateResponse = GetInternalStateResponse

@typing_extensions.final
class GetPointCloudMapStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of slam service'

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetPointCloudMapStreamRequest = GetPointCloudMapStreamRequest

@typing_extensions.final
class GetPointCloudMapStreamResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POINT_CLOUD_PCD_CHUNK_FIELD_NUMBER: builtins.int
    point_cloud_pcd_chunk: builtins.bytes
    'One chunk of the PointCloud.\n    For a given GetPointCloudMapStream request,\n    concatinating all\n    GetPointCloudMapStreamResponse.point_cloud_pcd_chunk\n    values in the order received result in\n    the complete pointcloud in standard PCD format.\n    https://pointclouds.org/documentation/tutorials/pcd_file_format.html\n    '

    def __init__(self, *, point_cloud_pcd_chunk: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['point_cloud_pcd_chunk', b'point_cloud_pcd_chunk']) -> None:
        ...
global___GetPointCloudMapStreamResponse = GetPointCloudMapStreamResponse

@typing_extensions.final
class GetInternalStateStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of slam service'

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetInternalStateStreamRequest = GetInternalStateStreamRequest

@typing_extensions.final
class GetInternalStateStreamResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INTERNAL_STATE_CHUNK_FIELD_NUMBER: builtins.int
    internal_state_chunk: builtins.bytes
    'Chunk of the internal state of the SLAM algorithm required to continue\n    mapping/localization\n    '

    def __init__(self, *, internal_state_chunk: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['internal_state_chunk', b'internal_state_chunk']) -> None:
        ...
global___GetInternalStateStreamResponse = GetInternalStateStreamResponse