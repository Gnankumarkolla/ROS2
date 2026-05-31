import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/gnan/janu_ws/src/install/turtlebot_maze_solver'
