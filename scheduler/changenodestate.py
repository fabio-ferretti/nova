'''
Created on 21/gen/2013

@author: Fabio Ferretti
'''
from nova import flags
from nova.openstack.common import cfg

FLAGS = flags.FLAGS

def change_node_state(host,state):
    
    path_nodes = ''.join([FLAGS.list_nodes_path, "nodes"])
    nodes = open(path_nodes, 'r').readlines()
    
    temp_nodes = []
    for node in nodes:
        elements_node = node.rsplit(' ')
        if host == elements_node[0]:
            i = 0
            temp_element = []
            for element in elements_node:
                if i != 2:
                    temp_element.append(elements_node[i])
                else:
                    temp_element.append(state)
                i = i + 1
            temp = ' '.join(temp_element)
            temp_nodes.append(temp)
        else:
            temp_nodes.append(node)
                
    open(path_nodes, 'w').writelines(temp_nodes)