"""
    sender.py
    ~~~~~~~~~~~~~~

    This example demonstrates how to integrate a surgical device with dopl connect.

    :copyright: 2022 Ryan James
"""
from os import path

from dopltech.sdk import Sdk
from dopltech.protos.common_pb2 import DataType, Frame, RobotControllerData, CatheterData, ElectricalSignalData, CatheterCoordinates, Coordinates, Quaternion


def on_session_joined(session_id):
    print("Joined session:", session_id)

def on_session_ended(session_id):
    print("Session ended:", session_id)

def get_frame_callback():
    print("sending data")
    frame = Frame()

    # robotControllerData = frame.robotControllerData()
    frame.robotControllerData.movementVelocity = 1

    frame.catheterData.append(
        CatheterData(
            sensorId=0,
            coordinates= CatheterCoordinates(
                position=Coordinates(
                    x=0,
                    y=1,
                    z=2,
                ),
                rotation=Quaternion(
                    x=0,
                    y=1,
                    z=2,
                    w=1,
                ),
            ),
        )
    )

    return frame

def on_frame_callback(frame):
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
