#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2,sqrt,pow

class my_node(Node) :
    def __init__(self) :
        super().__init__("pub_sub_turtle_node")
        self.pub = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.create_subscription(Pose,"/turtle1/pose",self.call_back,10)
        self.create_timer(0.5,self.timer_call)
        self.curpos = Pose()

    def timer_call(self):
        setpos = Pose()
        setpos.x = 3.0
        setpos.y = 7.0
        msg = Twist()
        distance_rob = self.dis(setpos)
        if abs(self.angvelocity(setpos)-self.curpos.theta) > 0.01 :
            msg.linear.x = 0.0
            msg.angular.z = self.angvelocity(setpos) - self.curpos.theta
            if abs(msg.angular.z) < 0.1:
                msg.linear.x = self.livelocity(setpos)
        

        
        self.pub.publish(msg)


     


    def call_back(self,x) :
        msg = "X = {:.3f} And Y = {:.3f} And Theta = {:.3f}".format(x.x,x.y,x.theta)
        self.get_logger().info(msg)
        self.curpos.x = x.x
        self.curpos.y = x.y
        self.curpos.theta = x.theta

    def dis (self,setpos):
        return sqrt(pow(setpos.x - self.curpos.x,2) + pow(setpos.y - self.curpos.y,2))

    def livelocity (self,setpos) :
        return 0.5*self.dis(setpos)
    def angvelocity (self,setpos) :
        return atan2(setpos.y - self.curpos.y,setpos.x - self.curpos.x)
    def disangvelocity (self,setpos) :
        return 0.5 * (self.angvelocity(setpos) - self.curpos.theta)
    





    
def main(args=None) :
    rclpy.init(args=args)
    x = my_node()
    rclpy.spin(x)
    rclpy.shutdown()


main()