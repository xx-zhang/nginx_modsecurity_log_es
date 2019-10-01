import redis 
import json 

from xdsl.test import test_insert_example

class Py3Destination4Es(object):
    def send(self, msg):
        self.outfile = open("/spool/log/example.txt", "a")
        # for key,v in msg.items():
        #     self.outfile.write(str(key) + " = " + str(v) + "\n");

        full_item = msg['LEGACY_MSGHDR'] + msg['MESSAGE']
        self.outfile.write(str(full_item))
        # self.outfile.write( str(json.loads(str(full_item)) ))
        self.outfile.write('==kkc=\n\n=====')

        for k, v in msg.items():
            self.outfile.write(str(k) + "\n")
            self.outfile.write(str(v)+"[{}]".format(str(type(v))) + "\n")
            self.outfile.write("___________侧_______EBD______\n\n")
        

        self.outfile.flush()
        self.outfile.close()
        
        return True
