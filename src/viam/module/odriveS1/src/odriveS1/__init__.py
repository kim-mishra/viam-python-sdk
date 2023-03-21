"""
This file odriveS1 model  with the Viam Registry.
"""

from viam.resource.registry import Registry
from viam.components.motor import Motor
from viam.module.odriveS1.src.odriveS1.odriveS1 import OdriveS1

Registry.register_resource_creator(Motor.SUBTYPE, OdriveS1.MODEL, OdriveS1.new)
