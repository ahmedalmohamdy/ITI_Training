#!/usr/bin/env python3

import rclpy

from rclpy.node import Node

from std_msgs.msg import String



class my_node(Node):

    def __init__(self):

        super().__init__(node_name="pub_node")

        self.create_timer(1,self.timer_call)

        self.pub_obj=self.create_publisher(String,"str_topic",10)

        self.counter=0



    def timer_call(self):

        msg=String()

        msg.data=f"Ahmed Almohamdy is publish{self.counter} ,"

        self.pub_obj.publish(msg)



def main(args=None):

    rclpy.init(args=args)

    node=my_node()

    rclpy.spin(node)

    rclpy.shutdown()



main()