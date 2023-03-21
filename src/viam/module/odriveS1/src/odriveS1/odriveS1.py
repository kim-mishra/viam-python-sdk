from typing import ClassVar, Mapping, Any, Dict, Optional, Tuple

from typing_extensions import Self

from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from viam.components.motor import Motor

# import asyncio
import odrive

# import gc

# import odrive.enums

# from viam.module.odriveS1.src.odriveS1.utils import rsetattr


class OdriveS1(Motor, Reconfigurable):
    MODEL: ClassVar[Model] = Model(ModelFamily("viam-user", "motor"), "odrive")
    serial_number: str
    max_rpm: float
    odrv: Any

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        odriveS1 = cls(config.name)
        cls.serial_number = config.attributes.fields["serial_number"].string_value
        cls.max_rpm = config.attributes.fields["max_rpm"].number_value

        # odrive_configs = config.attributes.fields["odrive_configs"].struct_value

        # with asyncio.Runner() as runner:
        #     odrv = runner.run(odrive.find_any_async())

        # for cfg, val in odrive_configs.fields.items():
        #     attrs = ".".join(attr for attr in cfg.split(":")[1:])
        #     rsetattr(odrv, attrs, val.number_value)
        cls.odrv = odrive.find_any()
        return odriveS1

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        self.serial_number = config.attributes.fields["serial_number"].string_value
        self.max_rpm = config.attributes.fields["max_rpm"].number_value

    async def set_power(self, power: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        pass

    async def go_for(self, rpm: float, revolutions: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        pass

    async def go_to(self, rpm: float, revolutions: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        pass

    async def reset_zero_position(self, offset: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
        pass

    async def get_position(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        pass

    async def get_properties(self, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Motor.Properties:
        return Motor.Properties(position_reporting=False)

    async def stop(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        # self.odrv.stop()
        # del OdriveS1.odrv
        pass

    async def is_powered(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Tuple[bool, float]:
        return False, 0.0

    async def is_moving(self):
        return False
