# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/app/playeronline/v1/playeronline.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/bilibili/app/playeronline/v1/playeronline.proto\x12\x1c\x62ilibili.app.playeronline.v1\">\n\x0fPlayerOnlineReq\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0b\n\x03\x63id\x18\x02 \x01(\x03\x12\x11\n\tplay_open\x18\x03 \x01(\x08\"r\n\x11PlayerOnlineReply\x12\x12\n\ntotal_text\x18\x01 \x01(\t\x12\x10\n\x08sec_next\x18\x02 \x01(\x03\x12\x13\n\x0b\x62ottom_show\x18\x03 \x01(\x08\x12\x10\n\x08sdm_show\x18\x04 \x01(\x08\x12\x10\n\x08sdm_text\x18\x05 \x01(\t2~\n\x0cPlayerOnline\x12n\n\x0cPlayerOnline\x12-.bilibili.app.playeronline.v1.PlayerOnlineReq\x1a/.bilibili.app.playeronline.v1.PlayerOnlineReplyb\x06proto3')



_PLAYERONLINEREQ = DESCRIPTOR.message_types_by_name['PlayerOnlineReq']
_PLAYERONLINEREPLY = DESCRIPTOR.message_types_by_name['PlayerOnlineReply']
PlayerOnlineReq = _reflection.GeneratedProtocolMessageType('PlayerOnlineReq', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERONLINEREQ,
  '__module__' : 'bilibili.app.playeronline.v1.playeronline_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.playeronline.v1.PlayerOnlineReq)
  })
_sym_db.RegisterMessage(PlayerOnlineReq)

PlayerOnlineReply = _reflection.GeneratedProtocolMessageType('PlayerOnlineReply', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERONLINEREPLY,
  '__module__' : 'bilibili.app.playeronline.v1.playeronline_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.playeronline.v1.PlayerOnlineReply)
  })
_sym_db.RegisterMessage(PlayerOnlineReply)

_PLAYERONLINE = DESCRIPTOR.services_by_name['PlayerOnline']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYERONLINEREQ._serialized_start=81
  _PLAYERONLINEREQ._serialized_end=143
  _PLAYERONLINEREPLY._serialized_start=145
  _PLAYERONLINEREPLY._serialized_end=259
  _PLAYERONLINE._serialized_start=261
  _PLAYERONLINE._serialized_end=387
# @@protoc_insertion_point(module_scope)