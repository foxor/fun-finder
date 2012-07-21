# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='fun_finder.proto',
  package='fun_finder',
  serialized_pb='\n\x10\x66un_finder.proto\x12\nfun_finder\"9\n\x13\x46unExperimentClient\x12\r\n\x05index\x18\x01 \x02(\x05\x12\x13\n\x0b\x66unProperty\x18\x02 \x02(\x05\"T\n\x0e\x46unGuessClient\x12\x10\n\x08\x62\x61seline\x18\x01 \x03(\x05\x12\x30\n\x07\x63hanges\x18\x02 \x03(\x0b\x32\x1f.fun_finder.FunExperimentClient\"I\n\x13\x46unExperimentServer\x12\r\n\x05index\x18\x01 \x02(\x05\x12\x10\n\x08property\x18\x02 \x02(\x05\x12\x11\n\tdeviation\x18\x03 \x02(\x05\"T\n\x0e\x46unGuessServer\x12\x10\n\x08\x62\x61seline\x18\x01 \x03(\x05\x12\x30\n\x07\x63hanges\x18\x02 \x03(\x0b\x32\x1f.fun_finder.FunExperimentServer\"Z\n\nFunMessage\x12\x0e\n\x06gameId\x18\x01 \x02(\t\x12*\n\x06\x63onfig\x18\x02 \x02(\x0b\x32\x1a.fun_finder.FunGuessClient\x12\x10\n\x08\x66unScore\x18\x03 \x03(\x05\"\\\n\x0bGameRatings\x12\x0e\n\x06gameId\x18\x01 \x02(\t\x12*\n\x06\x63onfig\x18\x02 \x02(\x0b\x32\x1a.fun_finder.FunGuessClient\x12\x11\n\tfunScores\x18\x03 \x03(\x05\"o\n\x13\x46unTrainingExercise\x12(\n\x08\x61llGames\x18\x01 \x03(\x0b\x32\x16.fun_finder.FunMessage\x12.\n\nhypothesis\x18\x02 \x03(\x0b\x32\x1a.fun_finder.FunGuessServer\"T\n\x0fGameInitMessage\x12\x31\n\rinitialConfig\x18\x01 \x02(\x0b\x32\x1a.fun_finder.FunGuessClient\x12\x0e\n\x06gameId\x18\x02 \x02(\tB!\n\x0e\x63om.fun_finderB\x0f\x46unFinderProtos')




_FUNEXPERIMENTCLIENT = descriptor.Descriptor(
  name='FunExperimentClient',
  full_name='fun_finder.FunExperimentClient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='index', full_name='fun_finder.FunExperimentClient.index', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='funProperty', full_name='fun_finder.FunExperimentClient.funProperty', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=32,
  serialized_end=89,
)


_FUNGUESSCLIENT = descriptor.Descriptor(
  name='FunGuessClient',
  full_name='fun_finder.FunGuessClient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='baseline', full_name='fun_finder.FunGuessClient.baseline', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='changes', full_name='fun_finder.FunGuessClient.changes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=91,
  serialized_end=175,
)


_FUNEXPERIMENTSERVER = descriptor.Descriptor(
  name='FunExperimentServer',
  full_name='fun_finder.FunExperimentServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='index', full_name='fun_finder.FunExperimentServer.index', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='property', full_name='fun_finder.FunExperimentServer.property', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='deviation', full_name='fun_finder.FunExperimentServer.deviation', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=177,
  serialized_end=250,
)


_FUNGUESSSERVER = descriptor.Descriptor(
  name='FunGuessServer',
  full_name='fun_finder.FunGuessServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='baseline', full_name='fun_finder.FunGuessServer.baseline', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='changes', full_name='fun_finder.FunGuessServer.changes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=252,
  serialized_end=336,
)


_FUNMESSAGE = descriptor.Descriptor(
  name='FunMessage',
  full_name='fun_finder.FunMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='gameId', full_name='fun_finder.FunMessage.gameId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='config', full_name='fun_finder.FunMessage.config', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='funScore', full_name='fun_finder.FunMessage.funScore', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=338,
  serialized_end=428,
)


_GAMERATINGS = descriptor.Descriptor(
  name='GameRatings',
  full_name='fun_finder.GameRatings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='gameId', full_name='fun_finder.GameRatings.gameId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='config', full_name='fun_finder.GameRatings.config', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='funScores', full_name='fun_finder.GameRatings.funScores', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=430,
  serialized_end=522,
)


_FUNTRAININGEXERCISE = descriptor.Descriptor(
  name='FunTrainingExercise',
  full_name='fun_finder.FunTrainingExercise',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='allGames', full_name='fun_finder.FunTrainingExercise.allGames', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hypothesis', full_name='fun_finder.FunTrainingExercise.hypothesis', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=524,
  serialized_end=635,
)


_GAMEINITMESSAGE = descriptor.Descriptor(
  name='GameInitMessage',
  full_name='fun_finder.GameInitMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='initialConfig', full_name='fun_finder.GameInitMessage.initialConfig', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gameId', full_name='fun_finder.GameInitMessage.gameId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=637,
  serialized_end=721,
)

_FUNGUESSCLIENT.fields_by_name['changes'].message_type = _FUNEXPERIMENTCLIENT
_FUNGUESSSERVER.fields_by_name['changes'].message_type = _FUNEXPERIMENTSERVER
_FUNMESSAGE.fields_by_name['config'].message_type = _FUNGUESSCLIENT
_GAMERATINGS.fields_by_name['config'].message_type = _FUNGUESSCLIENT
_FUNTRAININGEXERCISE.fields_by_name['allGames'].message_type = _FUNMESSAGE
_FUNTRAININGEXERCISE.fields_by_name['hypothesis'].message_type = _FUNGUESSSERVER
_GAMEINITMESSAGE.fields_by_name['initialConfig'].message_type = _FUNGUESSCLIENT
DESCRIPTOR.message_types_by_name['FunExperimentClient'] = _FUNEXPERIMENTCLIENT
DESCRIPTOR.message_types_by_name['FunGuessClient'] = _FUNGUESSCLIENT
DESCRIPTOR.message_types_by_name['FunExperimentServer'] = _FUNEXPERIMENTSERVER
DESCRIPTOR.message_types_by_name['FunGuessServer'] = _FUNGUESSSERVER
DESCRIPTOR.message_types_by_name['FunMessage'] = _FUNMESSAGE
DESCRIPTOR.message_types_by_name['GameRatings'] = _GAMERATINGS
DESCRIPTOR.message_types_by_name['FunTrainingExercise'] = _FUNTRAININGEXERCISE
DESCRIPTOR.message_types_by_name['GameInitMessage'] = _GAMEINITMESSAGE

class FunExperimentClient(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FUNEXPERIMENTCLIENT
  
  # @@protoc_insertion_point(class_scope:fun_finder.FunExperimentClient)

class FunGuessClient(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FUNGUESSCLIENT
  
  # @@protoc_insertion_point(class_scope:fun_finder.FunGuessClient)

class FunExperimentServer(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FUNEXPERIMENTSERVER
  
  # @@protoc_insertion_point(class_scope:fun_finder.FunExperimentServer)

class FunGuessServer(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FUNGUESSSERVER
  
  # @@protoc_insertion_point(class_scope:fun_finder.FunGuessServer)

class FunMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FUNMESSAGE
  
  # @@protoc_insertion_point(class_scope:fun_finder.FunMessage)

class GameRatings(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMERATINGS
  
  # @@protoc_insertion_point(class_scope:fun_finder.GameRatings)

class FunTrainingExercise(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FUNTRAININGEXERCISE
  
  # @@protoc_insertion_point(class_scope:fun_finder.FunTrainingExercise)

class GameInitMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMEINITMESSAGE
  
  # @@protoc_insertion_point(class_scope:fun_finder.GameInitMessage)

# @@protoc_insertion_point(module_scope)
