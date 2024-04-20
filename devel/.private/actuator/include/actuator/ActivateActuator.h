// Generated by gencpp from file actuator/ActivateActuator.msg
// DO NOT EDIT!


#ifndef ACTUATOR_MESSAGE_ACTIVATEACTUATOR_H
#define ACTUATOR_MESSAGE_ACTIVATEACTUATOR_H

#include <ros/service_traits.h>


#include <actuator/ActivateActuatorRequest.h>
#include <actuator/ActivateActuatorResponse.h>


namespace actuator
{

struct ActivateActuator
{

typedef ActivateActuatorRequest Request;
typedef ActivateActuatorResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct ActivateActuator
} // namespace actuator


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::actuator::ActivateActuator > {
  static const char* value()
  {
    return "ae4e2550a20f18efb89cde3cf018b8b4";
  }

  static const char* value(const ::actuator::ActivateActuator&) { return value(); }
};

template<>
struct DataType< ::actuator::ActivateActuator > {
  static const char* value()
  {
    return "actuator/ActivateActuator";
  }

  static const char* value(const ::actuator::ActivateActuator&) { return value(); }
};


// service_traits::MD5Sum< ::actuator::ActivateActuatorRequest> should match
// service_traits::MD5Sum< ::actuator::ActivateActuator >
template<>
struct MD5Sum< ::actuator::ActivateActuatorRequest>
{
  static const char* value()
  {
    return MD5Sum< ::actuator::ActivateActuator >::value();
  }
  static const char* value(const ::actuator::ActivateActuatorRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::actuator::ActivateActuatorRequest> should match
// service_traits::DataType< ::actuator::ActivateActuator >
template<>
struct DataType< ::actuator::ActivateActuatorRequest>
{
  static const char* value()
  {
    return DataType< ::actuator::ActivateActuator >::value();
  }
  static const char* value(const ::actuator::ActivateActuatorRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::actuator::ActivateActuatorResponse> should match
// service_traits::MD5Sum< ::actuator::ActivateActuator >
template<>
struct MD5Sum< ::actuator::ActivateActuatorResponse>
{
  static const char* value()
  {
    return MD5Sum< ::actuator::ActivateActuator >::value();
  }
  static const char* value(const ::actuator::ActivateActuatorResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::actuator::ActivateActuatorResponse> should match
// service_traits::DataType< ::actuator::ActivateActuator >
template<>
struct DataType< ::actuator::ActivateActuatorResponse>
{
  static const char* value()
  {
    return DataType< ::actuator::ActivateActuator >::value();
  }
  static const char* value(const ::actuator::ActivateActuatorResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ACTUATOR_MESSAGE_ACTIVATEACTUATOR_H
