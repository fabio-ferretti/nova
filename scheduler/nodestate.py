'''
Created on 17/gen/2013
V&A
'''
from nova import flags
from nova.openstack.common import cfg
    
FLAGS = flags.FLAGS

def is_node_suspended(host):  
    
    path_nodes = ''.join([FLAGS.list_nodes_path, "nodes"])
    nodes = open(path_nodes, 'r').readlines()
    
    for node in nodes:
        elements_node = node.rsplit(' ')
        if host == elements_node[0]:
            if elements_node[2] == 'suspended':
                #il nodo e' sospeso
                return True
    #il nodo non e' sospeso
    return False

def is_node_active(host):  
    
    path_nodes = ''.join([FLAGS.list_nodes_path, "nodes"])
    nodes = open(path_nodes, 'r').readlines()
    
    for node in nodes:
        elements_node = node.rsplit(' ')
        if host == elements_node[0]:
            if elements_node[2] == 'active':
                #il nodo e' attivo
                return True
    #il nodo non e' attivo
    return False

def get_macaddress_node_suspended(host):
    
    path_nodes = ''.join([FLAGS.list_nodes_path, "nodes"])
    nodes = open(path_nodes, 'r').readlines()
    
    for node in nodes:
        elements_node = node.rsplit(' ')
        if host == elements_node[0]:
            return elements_node[4]
    return None