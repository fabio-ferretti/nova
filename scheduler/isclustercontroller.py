'''
Created on 17/gen/2013
V&A
'''
from nova import flags
from nova.openstack.common import cfg
    
FLAGS = flags.FLAGS 
    
def is_cluster_controller(host):
    
    path_nodes = ''.join([FLAGS.list_nodes_path, "nodes"])
    nodes = open(path_nodes, 'r').readlines()
    
    for node in nodes:
        elements_node = node.rsplit(' ')
        if host == elements_node[0]:
            if elements_node[1] == 'cluster':
                #il nodo e un Cluster Controller
                return True
    #il nodo e un Compute Node
    return False