# P3DX_Nodes_Basic
Basic access nodes to the P3DX Robot

### odometry_Interface.
It allows access to the odometry provided by the RosAria package in the topical / odom.

### odometry_Interface_socket
It allows to send by sockets the odometry that the RosAria package provides in the topic / odom.

### Laser_interface.
Allows access to the SickLMS 200 measurements in the topical / scan.

### Sonar_Interface.
Allows access to the measurements of the robot's radar, in the topical / RosAria / sonar.

### battery_interface.
Allows access to the robot's battery.

### pioneer_teleop
It allows to teleoperate the robot with the keyboard. (It is recommended not to use this node, and instead use the rosaria client node).
