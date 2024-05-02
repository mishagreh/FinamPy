# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from FinamPy.proto import candles_pb2 as FinamPy_dot_proto_dot_candles__pb2

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
        + f' but the generated code in FinamPy/grpc/candles_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class CandlesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDayCandles = channel.unary_unary(
                '/grpc.tradeapi.v1.Candles/GetDayCandles',
                request_serializer=FinamPy_dot_proto_dot_candles__pb2.GetDayCandlesRequest.SerializeToString,
                response_deserializer=FinamPy_dot_proto_dot_candles__pb2.GetDayCandlesResult.FromString,
                _registered_method=True)
        self.GetIntradayCandles = channel.unary_unary(
                '/grpc.tradeapi.v1.Candles/GetIntradayCandles',
                request_serializer=FinamPy_dot_proto_dot_candles__pb2.GetIntradayCandlesRequest.SerializeToString,
                response_deserializer=FinamPy_dot_proto_dot_candles__pb2.GetIntradayCandlesResult.FromString,
                _registered_method=True)


class CandlesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetDayCandles(self, request, context):
        """Returns the list of day candles.
        Возвращает дневные свечи.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIntradayCandles(self, request, context):
        """Returns the list of intraday candles.
        Возвращает внутридневные свечи.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CandlesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDayCandles': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDayCandles,
                    request_deserializer=FinamPy_dot_proto_dot_candles__pb2.GetDayCandlesRequest.FromString,
                    response_serializer=FinamPy_dot_proto_dot_candles__pb2.GetDayCandlesResult.SerializeToString,
            ),
            'GetIntradayCandles': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIntradayCandles,
                    request_deserializer=FinamPy_dot_proto_dot_candles__pb2.GetIntradayCandlesRequest.FromString,
                    response_serializer=FinamPy_dot_proto_dot_candles__pb2.GetIntradayCandlesResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.tradeapi.v1.Candles', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Candles(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetDayCandles(request,
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
            '/grpc.tradeapi.v1.Candles/GetDayCandles',
            FinamPy_dot_proto_dot_candles__pb2.GetDayCandlesRequest.SerializeToString,
            FinamPy_dot_proto_dot_candles__pb2.GetDayCandlesResult.FromString,
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
    def GetIntradayCandles(request,
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
            '/grpc.tradeapi.v1.Candles/GetIntradayCandles',
            FinamPy_dot_proto_dot_candles__pb2.GetIntradayCandlesRequest.SerializeToString,
            FinamPy_dot_proto_dot_candles__pb2.GetIntradayCandlesResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)