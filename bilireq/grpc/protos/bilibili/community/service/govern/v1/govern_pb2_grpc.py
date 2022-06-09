# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilibili.community.service.govern.v1 import govern_pb2 as bilibili_dot_community_dot_service_dot_govern_dot_v1_dot_govern__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class QoeStub(object):
    """
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QoeReport = channel.unary_unary(
                '/bilibili.community.service.govern.v1.Qoe/QoeReport',
                request_serializer=bilibili_dot_community_dot_service_dot_govern_dot_v1_dot_govern__pb2.QoeReportReq.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class QoeServicer(object):
    """
    """

    def QoeReport(self, request, context):
        """
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QoeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'QoeReport': grpc.unary_unary_rpc_method_handler(
                    servicer.QoeReport,
                    request_deserializer=bilibili_dot_community_dot_service_dot_govern_dot_v1_dot_govern__pb2.QoeReportReq.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bilibili.community.service.govern.v1.Qoe', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Qoe(object):
    """
    """

    @staticmethod
    def QoeReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.community.service.govern.v1.Qoe/QoeReport',
            bilibili_dot_community_dot_service_dot_govern_dot_v1_dot_govern__pb2.QoeReportReq.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)