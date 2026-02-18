// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'routes_model.dart';

// **************************************************************************
// TypeAdapterGenerator
// **************************************************************************

class RouteModelAdapter extends TypeAdapter<RouteModel> {
  @override
  final int typeId = 3;

  @override
  RouteModel read(BinaryReader reader) {
    final numOfFields = reader.readByte();
    final fields = <int, dynamic>{
      for (int i = 0; i < numOfFields; i++) reader.readByte(): reader.read(),
    };
    return RouteModel(
      id: fields[0] as String,
      city: fields[1] as String,
      places: (fields[2] as List).cast<Highlight>(),
      createdAt: fields[3] as DateTime,
    );
  }

  @override
  void write(BinaryWriter writer, RouteModel obj) {
    writer
      ..writeByte(4)
      ..writeByte(0)
      ..write(obj.id)
      ..writeByte(1)
      ..write(obj.city)
      ..writeByte(2)
      ..write(obj.places)
      ..writeByte(3)
      ..write(obj.createdAt);
  }

  @override
  int get hashCode => typeId.hashCode;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is RouteModelAdapter &&
          runtimeType == other.runtimeType &&
          typeId == other.typeId;
}
