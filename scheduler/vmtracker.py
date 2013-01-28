'''
@author: Fabio Ferretti
'''
#Moduli per fare le statistiche delle VM attive che sono spente, in pausa ma non terminate

from nova import db
from nova import flags

FLAGS = flags.FLAGS

def set_vm_information(id_vm, context, information):

    vm_information = ''.join([FLAGS.output_path, "vm_information"])
    out_file = open(vm_information,"a")
    out_file.write("\nset_vm_information\n")
    out_file.write("\nid_vm uuid --> %s \n" % id_vm['uuid'])
    out_file.write("\nid_vm id --> %s \n" % id_vm['id'])
    out_file.write("\nid_vm host --> %s \n" % id_vm['host'])
    out_file.write("\nid_vm launched_at --> %s \n" % id_vm['launched_at'])
    out_file.write("\nid_vm display_name --> %s \n" % id_vm['display_name'])
    out_file.write("\nid_vm power_state --> %s \n" % id_vm['power_state'])

    out_file.write("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n")

    #out_file.write("\ndb.instance_get_all --> %s \n" % db.instance_get_all(context))

    #instance_id = db.instance_get_all(context)   

    #out_file.write("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n")

    #out_file.write("\ndb.instance_get --> %s \n" % db.instance_get(context, instance_id[0]))

    out_file.close()

def get_vm_information(id_vm):
    
    print 'get_vm_information'
    
def reset_vm_information():
    
    print 'reset_vm_information'