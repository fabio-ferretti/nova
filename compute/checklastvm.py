'''
Created on 14/gen/2013

@author: Fabio Ferretti
'''
from nova import db
from nova import flags
from sleeponlan import sleep_on_lan
from initializer import node_informations
from nova.scheduler.changenodestate import change_node_state

FLAGS = flags.FLAGS

def check_last_vm(host,context):
    
    if host != FLAGS.cluster_name:
	out = open("/home/fabioferretti/output","a")
	out.write("\nhost --> %s" % host)
	out.write("\nFLAGS.cluster_name --> %s" % FLAGS.cluster_name)
	out.close()
        result = db.instance_get_all_by_host(context, host)
        if len(result) == 0:
            #informo il cluster controller che non ho piu nessuna VM attiva
            node_informations(host, context)
            #se il nodo puo' essere svegliato tramite wake on lan viene sospeso
            if FLAGS.wakeable == True:
                sleep_on_lan(FLAGS.my_ip)
                #ultima VM in esecuzione non necessaria la live migration
                return True
        #ci sono altre VM in esecuzione sul compute node
        #devo controllare se gli altri nodi hanno capacita' sufficiente per eseguirle
        return False
    else:
        result = db.instance_get_all_by_host(context, host)
        if len(result) == 0:
            change_node_state(host,"idle")
        #sta eseguendo il cluster controller e le sue VM non migrano mai
        return True
