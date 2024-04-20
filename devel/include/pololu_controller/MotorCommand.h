// Generated by gencpp from file pololu_controller/MotorCommand.msg
// DO NOT EDIT!


#ifndef POLOLU_CONTROLLER_MESSAGE_MOTORCOMMAND_H
#define POLOLU_CONTROLLER_MESSAGE_MOTORCOMMAND_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pololu_controller
{
template <class ContainerAllocator>
struct MotorCommand_
{
  typedef MotorCommand_<ContainerAllocator> Type;

  MotorCommand_()
    : joint_name()
    , position(0.0)
    , speed(0.0)
    , acceleration(0.0)  {
    }
  MotorCommand_(const ContainerAllocator& _alloc)
    : joint_name(_alloc)
    , position(0.0)
    , speed(0.0)
    , acceleration(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _joint_name_type;
  _joint_name_type joint_name;

   typedef double _position_type;
  _position_type position;

   typedef float _speed_type;
  _speed_type speed;

   typedef float _acceleration_type;
  _acceleration_type acceleration;





  typedef boost::shared_ptr< ::pololu_controller::MotorCommand_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pololu_controller::MotorCommand_<ContainerAllocator> const> ConstPtr;

}; // struct MotorCommand_

typedef ::pololu_controller::MotorCommand_<std::allocator<void> > MotorCommand;

typedef boost::shared_ptr< ::pololu_controller::MotorCommand > MotorCommandPtr;
typedef boost::shared_ptr< ::pololu_controller::MotorCommand const> MotorCommandConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pololu_controller::MotorCommand_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pololu_controller::MotorCommand_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pololu_controller::MotorCommand_<ContainerAllocator1> & lhs, const ::pololu_controller::MotorCommand_<ContainerAllocator2> & rhs)
{
  return lhs.joint_name == rhs.joint_name &&
    lhs.position == rhs.position &&
    lhs.speed == rhs.speed &&
    lhs.acceleration == rhs.acceleration;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pololu_controller::MotorCommand_<ContainerAllocator1> & lhs, const ::pololu_controller::MotorCommand_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pololu_controller

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::pololu_controller::MotorCommand_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pololu_controller::MotorCommand_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pololu_controller::MotorCommand_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pololu_controller::MotorCommand_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pololu_controller::MotorCommand_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pololu_controller::MotorCommand_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pololu_controller::MotorCommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c357daac337dac3f7e4bb73a055e6e8c";
  }

  static const char* value(const ::pololu_controller::MotorCommand_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc357daac337dac3fULL;
  static const uint64_t static_value2 = 0x7e4bb73a055e6e8cULL;
};

template<class ContainerAllocator>
struct DataType< ::pololu_controller::MotorCommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pololu_controller/MotorCommand";
  }

  static const char* value(const ::pololu_controller::MotorCommand_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pololu_controller::MotorCommand_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string joint_name       # Name of the joint (specified in the yaml file), or motor_id for default calibration\n"
"float64 position        # Position to move to in PWN\n"
"float32 speed           # Speed to move at (0.0 - 1.0)\n"
"float32 acceleration    # Acceleration to move at (0.0 - 1.0)\n"
;
  }

  static const char* value(const ::pololu_controller::MotorCommand_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pololu_controller::MotorCommand_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.joint_name);
      stream.next(m.position);
      stream.next(m.speed);
      stream.next(m.acceleration);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MotorCommand_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pololu_controller::MotorCommand_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pololu_controller::MotorCommand_<ContainerAllocator>& v)
  {
    s << indent << "joint_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.joint_name);
    s << indent << "position: ";
    Printer<double>::stream(s, indent + "  ", v.position);
    s << indent << "speed: ";
    Printer<float>::stream(s, indent + "  ", v.speed);
    s << indent << "acceleration: ";
    Printer<float>::stream(s, indent + "  ", v.acceleration);
  }
};

} // namespace message_operations
} // namespace ros

#endif // POLOLU_CONTROLLER_MESSAGE_MOTORCOMMAND_H
