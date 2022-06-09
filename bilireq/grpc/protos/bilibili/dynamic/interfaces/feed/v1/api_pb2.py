# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/dynamic/interfaces/feed/v1/api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilibili.dynamic.common import dynamic_pb2 as bilibili_dot_dynamic_dot_common_dot_dynamic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-bilibili/dynamic/interfaces/feed/v1/api.proto\x12\x1d\x62ilibili.main.dynamic.feed.v1\x1a%bilibili/dynamic/common/dynamic.proto\"\xf0\x04\n\x0c\x43reateDynReq\x12.\n\x04meta\x18\x01 \x01(\x0b\x32 .bilibili.dynamic.UserCreateMeta\x12\x30\n\x07\x63ontent\x18\x02 \x01(\x0b\x32\x1f.bilibili.dynamic.CreateContent\x12,\n\x05scene\x18\x03 \x01(\x0e\x32\x1d.bilibili.dynamic.CreateScene\x12)\n\x04pics\x18\x04 \x03(\x0b\x32\x1b.bilibili.dynamic.CreatePic\x12\x31\n\nrepost_src\x18\x05 \x01(\x0b\x32\x1d.bilibili.dynamic.DynIdentity\x12/\n\x05video\x18\x06 \x01(\x0b\x32 .bilibili.dynamic.CreateDynVideo\x12\x13\n\x0bsketch_type\x18\x07 \x01(\x03\x12(\n\x06sketch\x18\x08 \x01(\x0b\x32\x18.bilibili.dynamic.Sketch\x12*\n\x07program\x18\t \x01(\x0b\x32\x19.bilibili.dynamic.Program\x12,\n\x07\x64yn_tag\x18\n \x01(\x0b\x32\x1b.bilibili.dynamic.CreateTag\x12\x37\n\x0b\x61ttach_card\x18\x0b \x01(\x0b\x32\".bilibili.dynamic.CreateAttachCard\x12.\n\x06option\x18\x0c \x01(\x0b\x32\x1e.bilibili.dynamic.CreateOption\x12,\n\x05topic\x18\r \x01(\x0b\x32\x1d.bilibili.dynamic.CreateTopic\x12\x11\n\tupload_id\x18\x0e \x01(\t\"\x84\x01\n\x12\x43reateInitCheckReq\x12\r\n\x05scene\x18\x01 \x01(\x05\x12,\n\x04meta\x18\x02 \x01(\x0b\x32\x1e.bilibili.dynamic.MetaDataCtrl\x12\x31\n\x06repost\x18\x03 \x01(\x0b\x32!.bilibili.dynamic.RepostInitCheck\"&\n\x12\x43reatePageInfosReq\x12\x10\n\x08topic_id\x18\x01 \x01(\x03\"W\n\x12\x43reatePageInfosRsp\x12\x41\n\x05topic\x18\x01 \x01(\x0b\x32\x32.bilibili.main.dynamic.feed.v1.CreatePageTopicInfo\";\n\x13\x43reatePageTopicInfo\x12\x10\n\x08topic_id\x18\x01 \x01(\x03\x12\x12\n\ntopic_name\x18\x02 \x01(\t\"h\n\x1e\x43reatePermissionButtonClickReq\x12\x46\n\x04type\x18\x01 \x01(\x0e\x32\x38.bilibili.main.dynamic.feed.v1.DynamicButtonClickBizType\" \n\x1e\x43reatePermissionButtonClickRsp\"\x1a\n\x18\x43reatePlusButtonClickReq\"\x1a\n\x18\x43reatePlusButtonClickRsp\"\x17\n\x15\x44ynamicButtonClickReq\"\x17\n\x15\x44ynamicButtonClickRsp\"\x0e\n\x0cHotSearchReq\"w\n\x0cHotSearchRsp\x12?\n\x05items\x18\x01 \x03(\x0b\x32\x30.bilibili.main.dynamic.feed.v1.HotSearchRsp.Item\x12\x0f\n\x07version\x18\x02 \x01(\t\x1a\x15\n\x04Item\x12\r\n\x05words\x18\x01 \x01(\t\"\x98\x01\n\x15ReserveButtonClickReq\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x12\n\nreserve_id\x18\x02 \x01(\x03\x12\x15\n\rreserve_total\x18\x03 \x01(\x03\x12\x16\n\x0e\x63ur_btn_status\x18\x04 \x01(\x05\x12\r\n\x05spmid\x18\x05 \x01(\t\x12\x0e\n\x06\x64yn_id\x18\x06 \x01(\x03\x12\x10\n\x08\x64yn_type\x18\x07 \x01(\x03\"\x92\x02\n\x16ReserveButtonClickResp\x12L\n\x10\x66inal_btn_status\x18\x01 \x01(\x0e\x32\x32.bilibili.main.dynamic.feed.v1.ReserveButtonStatus\x12\x42\n\x08\x62tn_mode\x18\x02 \x01(\x0e\x32\x30.bilibili.main.dynamic.feed.v1.ReserveButtonMode\x12\x16\n\x0ereserve_update\x18\x03 \x01(\x03\x12\x13\n\x0b\x64\x65sc_update\x18\x04 \x01(\t\x12\x14\n\x0chas_activity\x18\x05 \x01(\x08\x12\x14\n\x0c\x61\x63tivity_url\x18\x06 \x01(\t\x12\r\n\x05toast\x18\x07 \x01(\t\"m\n\x0eSubmitCheckReq\x12\x30\n\x07\x63ontent\x18\x01 \x01(\x0b\x32\x1f.bilibili.dynamic.CreateContent\x12)\n\x04pics\x18\x02 \x03(\x0b\x32\x1b.bilibili.dynamic.CreatePic\"\x10\n\x0eSubmitCheckRsp\"%\n\nSuggestReq\x12\t\n\x01s\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x05\"=\n\nSuggestRsp\x12\x0c\n\x04list\x18\x01 \x03(\t\x12\x10\n\x08track_id\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t*\x95\x01\n\x19\x44ynamicButtonClickBizType\x12&\n\"DYNAMIC_BUTTON_CLICK_BIZ_TYPE_NONE\x10\x00\x12&\n\"DYNAMIC_BUTTON_CLICK_BIZ_TYPE_LIVE\x10\x01\x12(\n$DYNAMIC_BUTTON_CLICK_BIZ_TYPE_DYN_UP\x10\x02*u\n\x11ReserveButtonMode\x12\x1c\n\x18RESERVE_BUTTON_MODE_NONE\x10\x00\x12\x1f\n\x1bRESERVE_BUTTON_MODE_RESERVE\x10\x01\x12!\n\x1dRESERVE_BUTTON_MODE_UP_CANCEL\x10\x02*y\n\x13ReserveButtonStatus\x12\x1e\n\x1aRESERVE_BUTTON_STATUS_NONE\x10\x00\x12!\n\x1dRESERVE_BUTTON_STATUS_UNCHECK\x10\x01\x12\x1f\n\x1bRESERVE_BUTTON_STATUS_CHECK\x10\x02\x32\x88\x0b\n\x04\x46\x65\x65\x64\x12g\n\x0f\x43reateInitCheck\x12\x31.bilibili.main.dynamic.feed.v1.CreateInitCheckReq\x1a!.bilibili.dynamic.CreateCheckResp\x12k\n\x0bSubmitCheck\x12-.bilibili.main.dynamic.feed.v1.SubmitCheckReq\x1a-.bilibili.main.dynamic.feed.v1.SubmitCheckRsp\x12V\n\tCreateDyn\x12+.bilibili.main.dynamic.feed.v1.CreateDynReq\x1a\x1c.bilibili.dynamic.CreateResp\x12T\n\x0cGetUidByName\x12!.bilibili.dynamic.GetUidByNameReq\x1a!.bilibili.dynamic.GetUidByNameRsp\x12\x42\n\x06\x41tList\x12\x1b.bilibili.dynamic.AtListReq\x1a\x1b.bilibili.dynamic.AtListRsp\x12\x46\n\x08\x41tSearch\x12\x1d.bilibili.dynamic.AtSearchReq\x1a\x1b.bilibili.dynamic.AtListRsp\x12\x81\x01\n\x12ReserveButtonClick\x12\x34.bilibili.main.dynamic.feed.v1.ReserveButtonClickReq\x1a\x35.bilibili.main.dynamic.feed.v1.ReserveButtonClickResp\x12\x89\x01\n\x15\x43reatePlusButtonClick\x12\x37.bilibili.main.dynamic.feed.v1.CreatePlusButtonClickReq\x1a\x37.bilibili.main.dynamic.feed.v1.CreatePlusButtonClickRsp\x12\x65\n\tHotSearch\x12+.bilibili.main.dynamic.feed.v1.HotSearchReq\x1a+.bilibili.main.dynamic.feed.v1.HotSearchRsp\x12_\n\x07Suggest\x12).bilibili.main.dynamic.feed.v1.SuggestReq\x1a).bilibili.main.dynamic.feed.v1.SuggestRsp\x12\x80\x01\n\x12\x44ynamicButtonClick\x12\x34.bilibili.main.dynamic.feed.v1.DynamicButtonClickReq\x1a\x34.bilibili.main.dynamic.feed.v1.DynamicButtonClickRsp\x12\x9b\x01\n\x1b\x43reatePermissionButtonClick\x12=.bilibili.main.dynamic.feed.v1.CreatePermissionButtonClickReq\x1a=.bilibili.main.dynamic.feed.v1.CreatePermissionButtonClickRsp\x12w\n\x0f\x43reatePageInfos\x12\x31.bilibili.main.dynamic.feed.v1.CreatePageInfosReq\x1a\x31.bilibili.main.dynamic.feed.v1.CreatePageInfosRspb\x06proto3')

_DYNAMICBUTTONCLICKBIZTYPE = DESCRIPTOR.enum_types_by_name['DynamicButtonClickBizType']
DynamicButtonClickBizType = enum_type_wrapper.EnumTypeWrapper(_DYNAMICBUTTONCLICKBIZTYPE)
_RESERVEBUTTONMODE = DESCRIPTOR.enum_types_by_name['ReserveButtonMode']
ReserveButtonMode = enum_type_wrapper.EnumTypeWrapper(_RESERVEBUTTONMODE)
_RESERVEBUTTONSTATUS = DESCRIPTOR.enum_types_by_name['ReserveButtonStatus']
ReserveButtonStatus = enum_type_wrapper.EnumTypeWrapper(_RESERVEBUTTONSTATUS)
DYNAMIC_BUTTON_CLICK_BIZ_TYPE_NONE = 0
DYNAMIC_BUTTON_CLICK_BIZ_TYPE_LIVE = 1
DYNAMIC_BUTTON_CLICK_BIZ_TYPE_DYN_UP = 2
RESERVE_BUTTON_MODE_NONE = 0
RESERVE_BUTTON_MODE_RESERVE = 1
RESERVE_BUTTON_MODE_UP_CANCEL = 2
RESERVE_BUTTON_STATUS_NONE = 0
RESERVE_BUTTON_STATUS_UNCHECK = 1
RESERVE_BUTTON_STATUS_CHECK = 2


_CREATEDYNREQ = DESCRIPTOR.message_types_by_name['CreateDynReq']
_CREATEINITCHECKREQ = DESCRIPTOR.message_types_by_name['CreateInitCheckReq']
_CREATEPAGEINFOSREQ = DESCRIPTOR.message_types_by_name['CreatePageInfosReq']
_CREATEPAGEINFOSRSP = DESCRIPTOR.message_types_by_name['CreatePageInfosRsp']
_CREATEPAGETOPICINFO = DESCRIPTOR.message_types_by_name['CreatePageTopicInfo']
_CREATEPERMISSIONBUTTONCLICKREQ = DESCRIPTOR.message_types_by_name['CreatePermissionButtonClickReq']
_CREATEPERMISSIONBUTTONCLICKRSP = DESCRIPTOR.message_types_by_name['CreatePermissionButtonClickRsp']
_CREATEPLUSBUTTONCLICKREQ = DESCRIPTOR.message_types_by_name['CreatePlusButtonClickReq']
_CREATEPLUSBUTTONCLICKRSP = DESCRIPTOR.message_types_by_name['CreatePlusButtonClickRsp']
_DYNAMICBUTTONCLICKREQ = DESCRIPTOR.message_types_by_name['DynamicButtonClickReq']
_DYNAMICBUTTONCLICKRSP = DESCRIPTOR.message_types_by_name['DynamicButtonClickRsp']
_HOTSEARCHREQ = DESCRIPTOR.message_types_by_name['HotSearchReq']
_HOTSEARCHRSP = DESCRIPTOR.message_types_by_name['HotSearchRsp']
_HOTSEARCHRSP_ITEM = _HOTSEARCHRSP.nested_types_by_name['Item']
_RESERVEBUTTONCLICKREQ = DESCRIPTOR.message_types_by_name['ReserveButtonClickReq']
_RESERVEBUTTONCLICKRESP = DESCRIPTOR.message_types_by_name['ReserveButtonClickResp']
_SUBMITCHECKREQ = DESCRIPTOR.message_types_by_name['SubmitCheckReq']
_SUBMITCHECKRSP = DESCRIPTOR.message_types_by_name['SubmitCheckRsp']
_SUGGESTREQ = DESCRIPTOR.message_types_by_name['SuggestReq']
_SUGGESTRSP = DESCRIPTOR.message_types_by_name['SuggestRsp']
CreateDynReq = _reflection.GeneratedProtocolMessageType('CreateDynReq', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDYNREQ,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.CreateDynReq)
  })
_sym_db.RegisterMessage(CreateDynReq)

CreateInitCheckReq = _reflection.GeneratedProtocolMessageType('CreateInitCheckReq', (_message.Message,), {
  'DESCRIPTOR' : _CREATEINITCHECKREQ,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.CreateInitCheckReq)
  })
_sym_db.RegisterMessage(CreateInitCheckReq)

CreatePageInfosReq = _reflection.GeneratedProtocolMessageType('CreatePageInfosReq', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPAGEINFOSREQ,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.CreatePageInfosReq)
  })
_sym_db.RegisterMessage(CreatePageInfosReq)

CreatePageInfosRsp = _reflection.GeneratedProtocolMessageType('CreatePageInfosRsp', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPAGEINFOSRSP,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.CreatePageInfosRsp)
  })
_sym_db.RegisterMessage(CreatePageInfosRsp)

CreatePageTopicInfo = _reflection.GeneratedProtocolMessageType('CreatePageTopicInfo', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPAGETOPICINFO,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.CreatePageTopicInfo)
  })
_sym_db.RegisterMessage(CreatePageTopicInfo)

CreatePermissionButtonClickReq = _reflection.GeneratedProtocolMessageType('CreatePermissionButtonClickReq', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPERMISSIONBUTTONCLICKREQ,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.CreatePermissionButtonClickReq)
  })
_sym_db.RegisterMessage(CreatePermissionButtonClickReq)

CreatePermissionButtonClickRsp = _reflection.GeneratedProtocolMessageType('CreatePermissionButtonClickRsp', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPERMISSIONBUTTONCLICKRSP,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.CreatePermissionButtonClickRsp)
  })
_sym_db.RegisterMessage(CreatePermissionButtonClickRsp)

CreatePlusButtonClickReq = _reflection.GeneratedProtocolMessageType('CreatePlusButtonClickReq', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPLUSBUTTONCLICKREQ,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.CreatePlusButtonClickReq)
  })
_sym_db.RegisterMessage(CreatePlusButtonClickReq)

CreatePlusButtonClickRsp = _reflection.GeneratedProtocolMessageType('CreatePlusButtonClickRsp', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPLUSBUTTONCLICKRSP,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.CreatePlusButtonClickRsp)
  })
_sym_db.RegisterMessage(CreatePlusButtonClickRsp)

DynamicButtonClickReq = _reflection.GeneratedProtocolMessageType('DynamicButtonClickReq', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMICBUTTONCLICKREQ,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.DynamicButtonClickReq)
  })
_sym_db.RegisterMessage(DynamicButtonClickReq)

DynamicButtonClickRsp = _reflection.GeneratedProtocolMessageType('DynamicButtonClickRsp', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMICBUTTONCLICKRSP,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.DynamicButtonClickRsp)
  })
_sym_db.RegisterMessage(DynamicButtonClickRsp)

HotSearchReq = _reflection.GeneratedProtocolMessageType('HotSearchReq', (_message.Message,), {
  'DESCRIPTOR' : _HOTSEARCHREQ,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.HotSearchReq)
  })
_sym_db.RegisterMessage(HotSearchReq)

HotSearchRsp = _reflection.GeneratedProtocolMessageType('HotSearchRsp', (_message.Message,), {

  'Item' : _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
    'DESCRIPTOR' : _HOTSEARCHRSP_ITEM,
    '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
    # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.HotSearchRsp.Item)
    })
  ,
  'DESCRIPTOR' : _HOTSEARCHRSP,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.HotSearchRsp)
  })
_sym_db.RegisterMessage(HotSearchRsp)
_sym_db.RegisterMessage(HotSearchRsp.Item)

ReserveButtonClickReq = _reflection.GeneratedProtocolMessageType('ReserveButtonClickReq', (_message.Message,), {
  'DESCRIPTOR' : _RESERVEBUTTONCLICKREQ,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.ReserveButtonClickReq)
  })
_sym_db.RegisterMessage(ReserveButtonClickReq)

ReserveButtonClickResp = _reflection.GeneratedProtocolMessageType('ReserveButtonClickResp', (_message.Message,), {
  'DESCRIPTOR' : _RESERVEBUTTONCLICKRESP,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.ReserveButtonClickResp)
  })
_sym_db.RegisterMessage(ReserveButtonClickResp)

SubmitCheckReq = _reflection.GeneratedProtocolMessageType('SubmitCheckReq', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITCHECKREQ,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.SubmitCheckReq)
  })
_sym_db.RegisterMessage(SubmitCheckReq)

SubmitCheckRsp = _reflection.GeneratedProtocolMessageType('SubmitCheckRsp', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITCHECKRSP,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.SubmitCheckRsp)
  })
_sym_db.RegisterMessage(SubmitCheckRsp)

SuggestReq = _reflection.GeneratedProtocolMessageType('SuggestReq', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTREQ,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.SuggestReq)
  })
_sym_db.RegisterMessage(SuggestReq)

SuggestRsp = _reflection.GeneratedProtocolMessageType('SuggestRsp', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTRSP,
  '__module__' : 'bilibili.dynamic.interfaces.feed.v1.api_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.dynamic.feed.v1.SuggestRsp)
  })
_sym_db.RegisterMessage(SuggestRsp)

_FEED = DESCRIPTOR.services_by_name['Feed']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DYNAMICBUTTONCLICKBIZTYPE._serialized_start=2118
  _DYNAMICBUTTONCLICKBIZTYPE._serialized_end=2267
  _RESERVEBUTTONMODE._serialized_start=2269
  _RESERVEBUTTONMODE._serialized_end=2386
  _RESERVEBUTTONSTATUS._serialized_start=2388
  _RESERVEBUTTONSTATUS._serialized_end=2509
  _CREATEDYNREQ._serialized_start=120
  _CREATEDYNREQ._serialized_end=744
  _CREATEINITCHECKREQ._serialized_start=747
  _CREATEINITCHECKREQ._serialized_end=879
  _CREATEPAGEINFOSREQ._serialized_start=881
  _CREATEPAGEINFOSREQ._serialized_end=919
  _CREATEPAGEINFOSRSP._serialized_start=921
  _CREATEPAGEINFOSRSP._serialized_end=1008
  _CREATEPAGETOPICINFO._serialized_start=1010
  _CREATEPAGETOPICINFO._serialized_end=1069
  _CREATEPERMISSIONBUTTONCLICKREQ._serialized_start=1071
  _CREATEPERMISSIONBUTTONCLICKREQ._serialized_end=1175
  _CREATEPERMISSIONBUTTONCLICKRSP._serialized_start=1177
  _CREATEPERMISSIONBUTTONCLICKRSP._serialized_end=1209
  _CREATEPLUSBUTTONCLICKREQ._serialized_start=1211
  _CREATEPLUSBUTTONCLICKREQ._serialized_end=1237
  _CREATEPLUSBUTTONCLICKRSP._serialized_start=1239
  _CREATEPLUSBUTTONCLICKRSP._serialized_end=1265
  _DYNAMICBUTTONCLICKREQ._serialized_start=1267
  _DYNAMICBUTTONCLICKREQ._serialized_end=1290
  _DYNAMICBUTTONCLICKRSP._serialized_start=1292
  _DYNAMICBUTTONCLICKRSP._serialized_end=1315
  _HOTSEARCHREQ._serialized_start=1317
  _HOTSEARCHREQ._serialized_end=1331
  _HOTSEARCHRSP._serialized_start=1333
  _HOTSEARCHRSP._serialized_end=1452
  _HOTSEARCHRSP_ITEM._serialized_start=1431
  _HOTSEARCHRSP_ITEM._serialized_end=1452
  _RESERVEBUTTONCLICKREQ._serialized_start=1455
  _RESERVEBUTTONCLICKREQ._serialized_end=1607
  _RESERVEBUTTONCLICKRESP._serialized_start=1610
  _RESERVEBUTTONCLICKRESP._serialized_end=1884
  _SUBMITCHECKREQ._serialized_start=1886
  _SUBMITCHECKREQ._serialized_end=1995
  _SUBMITCHECKRSP._serialized_start=1997
  _SUBMITCHECKRSP._serialized_end=2013
  _SUGGESTREQ._serialized_start=2015
  _SUGGESTREQ._serialized_end=2052
  _SUGGESTRSP._serialized_start=2054
  _SUGGESTRSP._serialized_end=2115
  _FEED._serialized_start=2512
  _FEED._serialized_end=3928
# @@protoc_insertion_point(module_scope)