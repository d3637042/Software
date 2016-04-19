#!/usr/bin/env python

import rospy, sys, os, cv2, pickle
from navigation.graph import Graph
from navigation.graph_search import GraphSearchProblem
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from navigation.srv import *
from navigation.generate_duckietown_map import graph_creator

class graph_search_server():
    def __init__(self):
        print 'Graph Search Service Started'

        # Input: csv file
        self.map_name = rospy.get_param('/map_name')

        # Loading map
        self.script_dir = os.path.dirname(__file__)
        self.map_path = self.script_dir + '/maps/' + self.map_name

        gc = graph_creator()
        self.duckietown_graph = gc.build_graph_from_csv(csv_filename=self.map_name)
        self.duckietown_problem = GraphSearchProblem(self.duckietown_graph, None, None)
    
        print "Map loaded successfully!\n"

        self.image_pub = rospy.Publisher("~map_graph",Image, queue_size = 1, latch=True)
        self.bridge = CvBridge()

        # Send graph through publisher
        self.duckietown_graph.draw(self.script_dir, highlight_edges=None, map_name = self.map_name)
        cv_image = cv2.imread(self.map_path + '.png', cv2.CV_LOAD_IMAGE_COLOR)
        self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))

    def handle_graph_search(self,req):
	    # Checking if nodes exists
        if (req.source_node not in self.duckietown_graph) or (req.target_node not in self.duckietown_graph):
            print "Source or target node do not exist."
            self.publishImage(req, [])
            return GraphSearchResponse([])

        # Running A*
        self.duckietown_problem.start = req.source_node
        self.duckietown_problem.goal = req.target_node
        path = self.duckietown_problem.astar_search()

        # Publish graph solution
        self.publishImage(req, path)

        return GraphSearchResponse(path.actions)        

    def publishImage(self, req, path):
        if path:
            self.duckietown_graph.draw(self.script_dir, highlight_edges=path.edges(), map_name = self.map_name, highlight_nodes = [req.source_node, req.target_node])
        else:
            self.duckietown_graph.draw(self.script_dir, highlight_edges=None, map_name = self.map_name)
        cv_image = cv2.imread(self.map_path + '.png', cv2.CV_LOAD_IMAGE_COLOR)
        self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))

if __name__ == "__main__":	
    rospy.init_node('graph_search_server_node')
    gss = graph_search_server()
    print 'Starting server...\n'
    s = rospy.Service('graph_search', GraphSearch, gss.handle_graph_search)
    rospy.spin()