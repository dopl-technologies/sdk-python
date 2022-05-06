"""
    receiver.py
    ~~~~~~~~~~~~~~

    This example demonstrates how to integrate a surgical device with dopl connect.

    :copyright: 2020 Ryan James
"""
from os import path

from google.protobuf.json_format import MessageToJson

from dopltech.sdk import Sdk
from dopltech.protos.common_pb2 import DataType, Frame, RobotControllerData, CatheterData, ElectricalSignalData, CatheterCoordinates, Coordinates, Quaternion


def on_session_joined(session_id):
    print("Joined session:", session_id)

def on_session_ended(session_id):
    print("Session ended:", session_id)

def get_frame_callback():
    return None

def on_frame_callback(frame):
    print("Data received")
    json = MessageToJson(frame)
    print(json)
    return True

dopltechPath = path.join(path.dirname(__file__), ".dopltech.yml")

sdk = Sdk(
    dopltechPath,
    on_session_joined,
    on_session_ended,
    get_frame_callback,
    on_frame_callback,
)
sdk.connect_async()
