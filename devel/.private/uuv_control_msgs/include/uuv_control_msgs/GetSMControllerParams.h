// Generated by gencpp from file uuv_control_msgs/GetSMControllerParams.msg
// DO NOT EDIT!


#ifndef UUV_CONTROL_MSGS_MESSAGE_GETSMCONTROLLERPARAMS_H
#define UUV_CONTROL_MSGS_MESSAGE_GETSMCONTROLLERPARAMS_H

#include <ros/service_traits.h>


#include <uuv_control_msgs/GetSMControllerParamsRequest.h>
#include <uuv_control_msgs/GetSMControllerParamsResponse.h>


namespace uuv_control_msgs
{

struct GetSMControllerParams
{

typedef GetSMControllerParamsRequest Request;
typedef GetSMControllerParamsResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetSMControllerParams
} // namespace uuv_control_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::uuv_control_msgs::GetSMControllerParams > {
  static const char* value()
  {
    return "dc294c7929e39ce02ce0ce70a116b3b3";
  }

  static const char* value(const ::uuv_control_msgs::GetSMControllerParams&) { return value(); }
};

template<>
struct DataType< ::uuv_control_msgs::GetSMControllerParams > {
  static const char* value()
  {
    return "uuv_control_msgs/GetSMControllerParams";
  }

  static const char* value(const ::uuv_control_msgs::GetSMControllerParams&) { return value(); }
};


// service_traits::MD5Sum< ::uuv_control_msgs::GetSMControllerParamsRequest> should match
// service_traits::MD5Sum< ::uuv_control_msgs::GetSMControllerParams >
template<>
struct MD5Sum< ::uuv_control_msgs::GetSMControllerParamsRequest>
{
  static const char* value()
  {
    return MD5Sum< ::uuv_control_msgs::GetSMControllerParams >::value();
  }
  static const char* value(const ::uuv_control_msgs::GetSMControllerParamsRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::uuv_control_msgs::GetSMControllerParamsRequest> should match
// service_traits::DataType< ::uuv_control_msgs::GetSMControllerParams >
template<>
struct DataType< ::uuv_control_msgs::GetSMControllerParamsRequest>
{
  static const char* value()
  {
    return DataType< ::uuv_control_msgs::GetSMControllerParams >::value();
  }
  static const char* value(const ::uuv_control_msgs::GetSMControllerParamsRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::uuv_control_msgs::GetSMControllerParamsResponse> should match
// service_traits::MD5Sum< ::uuv_control_msgs::GetSMControllerParams >
template<>
struct MD5Sum< ::uuv_control_msgs::GetSMControllerParamsResponse>
{
  static const char* value()
  {
    return MD5Sum< ::uuv_control_msgs::GetSMControllerParams >::value();
  }
  static const char* value(const ::uuv_control_msgs::GetSMControllerParamsResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::uuv_control_msgs::GetSMControllerParamsResponse> should match
// service_traits::DataType< ::uuv_control_msgs::GetSMControllerParams >
template<>
struct DataType< ::uuv_control_msgs::GetSMControllerParamsResponse>
{
  static const char* value()
  {
    return DataType< ::uuv_control_msgs::GetSMControllerParams >::value();
  }
  static const char* value(const ::uuv_control_msgs::GetSMControllerParamsResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // UUV_CONTROL_MSGS_MESSAGE_GETSMCONTROLLERPARAMS_H
