# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import gripper_pb2 as gripper_dot_gripper__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in gripper/gripper_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class GripperServiceStub(object):
    """
    Allows users to send gripper actions.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Grab = channel.unary_unary(
                '/mavsdk.rpc.gripper.GripperService/Grab',
                request_serializer=gripper_dot_gripper__pb2.GrabRequest.SerializeToString,
                response_deserializer=gripper_dot_gripper__pb2.GrabResponse.FromString,
                _registered_method=True)
        self.Release = channel.unary_unary(
                '/mavsdk.rpc.gripper.GripperService/Release',
                request_serializer=gripper_dot_gripper__pb2.ReleaseRequest.SerializeToString,
                response_deserializer=gripper_dot_gripper__pb2.ReleaseResponse.FromString,
                _registered_method=True)


class GripperServiceServicer(object):
    """
    Allows users to send gripper actions.
    """

    def Grab(self, request, context):
        """
        Gripper grab cargo.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Release(self, request, context):
        """
        Gripper release cargo.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GripperServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Grab': grpc.unary_unary_rpc_method_handler(
                    servicer.Grab,
                    request_deserializer=gripper_dot_gripper__pb2.GrabRequest.FromString,
                    response_serializer=gripper_dot_gripper__pb2.GrabResponse.SerializeToString,
            ),
            'Release': grpc.unary_unary_rpc_method_handler(
                    servicer.Release,
                    request_deserializer=gripper_dot_gripper__pb2.ReleaseRequest.FromString,
                    response_serializer=gripper_dot_gripper__pb2.ReleaseResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.gripper.GripperService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GripperService(object):
    """
    Allows users to send gripper actions.
    """

    @staticmethod
    def Grab(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mavsdk.rpc.gripper.GripperService/Grab',
            gripper_dot_gripper__pb2.GrabRequest.SerializeToString,
            gripper_dot_gripper__pb2.GrabResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Release(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mavsdk.rpc.gripper.GripperService/Release',
            gripper_dot_gripper__pb2.ReleaseRequest.SerializeToString,
            gripper_dot_gripper__pb2.ReleaseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
