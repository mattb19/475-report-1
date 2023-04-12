import rospy
import math

# import the plan message
from ur5e_control.msg import Plan
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    # initialize the node
    rospy.init_node('simple_planner', anonymous = True)
    # add a publisher for sending joint position commands
    plan_pub = rospy.Publisher('/plan', Plan, queue_size = 10)
    # set a 10Hz frequency for this loop
    loop_rate = rospy.Rat   
    # define a plan variable
    plan = Plan()
    
    plan_point1 = Twist()
    # just a quick solution to send two target points
    # define a point close to the initial position
    plan_point1.linear.x = -0.71
    plan_point1.linear.y = -0.13
    plan_point1.linear.z = 0.44
    plan_point1.angular.x = -3.11
    plan_point1.angular.y = -0.08
    plan_point1.angular.z = 1.95
    # add this point to the plan
    plan.points.append(plan_point1)

    plan_point2 = Twist()
    # define a point away from the initial position
    plan_point2.linear.x = -0.63
    plan_point2.linear.y = -0.13
    plan_point2.linear.z = 0.05
    plan_point2.angular.x = 3.13
    plan_point2.angular.y = -0.08
    plan_point2.angular.z = 1.95
    # add this point to the plan
    plan.points.append(plan_point2)

    plan_point3 = Twist()
    # define a point away from the initial position
    plan_point3.linear.x = -0.89
    plan_point3.linear.y = -0.13
    plan_point3.linear.z = 0.27
    plan_point3.angular.x = -3.1
    plan_point3.angular.y = -0.01
    plan_point3.angular.z = 1.94
    # add this point to the plan
    plan.points.append(plan_point3)

    plan_point4 = Twist()
    # define a point away from the initial position
    plan_point4.linear.x = -0.91
    plan_point4.linear.y = -0.13
    plan_point4.linear.z = 0.02
    plan_point4.angular.x = 2.88
    plan_point4.angular.y = -0.03
    plan_point4.angular.z = 1.95
    # add this point to the plan
    plan.points.append(plan_point4)


    while not rospy.is_shutdown():
        # publish the plan
        plan_pub.publish(plan)
        # wait for 0.1 seconds until the next loop and repeat
        loop_rate.sleep()