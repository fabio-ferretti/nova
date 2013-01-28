'''
Created on 23/gen/2013

@author: faust
'''
from nova import db
from nova import flags
from nova import compute
from nova.compute import vm_states
from checklastvm import check_last_vm

import nova.context
import time
import os

FLAGS = flags.FLAGS

def check_for_migration(manager,host,contexta): 

    #La migrazione deve essere eseguita solamente dai compute node
    if host != FLAGS.cluster_name:
	    contexto = nova.context.get_admin_context()
	    results = db.service_get_all_compute_sorted_desc(contexto)
	    istanze_attive_nodo_locale = db.instance_get_all_by_host(contexto, host)
	    for result in results:
		(service, instance_cores) = result
		if service['host'] != host:
		    istanze_attive_nodo_remoto = db.instance_get_all_by_host(contexto, service['host'])
		    #condizione che abilita la migrazione
		    if len(istanze_attive_nodo_locale) <= len(istanze_attive_nodo_remoto):
		        for istanza in istanze_attive_nodo_locale:
			    repeat = True
			    while repeat:
				manager.live_migration(contexto, istanza['id'], service['host'])
		        	_instance_update(contexto, istanza['id'], vm_state=vm_states.MIGRATING)
				old_instance = istanza
				time.sleep(15)
				new_instances = db.instance_get_all_by_host(contexto, service['host'])
				for new_instance in new_instances:
					if new_instance['uuid'] == old_instance['uuid']:
						#Istanza migrata correttamente
		        			_instance_update(contexto, istanza['id'], vm_state=vm_states.ACTIVE)
						repeat = False
			check_last_vm(host,contexto)
			

		    
def _instance_update(contex, instance_id, **args):
	"""Update an instance in the database using kwargs as value."""
	return db.instance_update(contex, instance_id, args)    

	
