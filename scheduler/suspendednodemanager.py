'''
V&A
@author: Fabio Ferretti
'''
#OBSOLETO

from wakeonlan import wake_on_lan
from nodes import flags

FLAGS = flags.FLAGS

def enable_suspended_node():
    
    path_nodes = ''.join([FLAGS.list_nodes_path, "nodes"])
    suspended_nodes = open(path_nodes, 'r').readlines()
    if len(suspended_nodes) == 0:
        print "node_to_enable = None"
        return None
    node_to_enable = suspended_nodes[0] 
    del suspended_nodes[0]
    open(path_nodes, 'w').writelines(suspended_nodes)
    
    #Risveglio il nodo selezionato
    
    macaddress = node_to_enable.split(' ')[0]
    
    wake_on_lan(macaddress)
    
    print macaddress
    
    return node_to_enable

if __name__ == '__main__':
    enable_suspended_node()