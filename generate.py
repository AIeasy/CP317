'''
generate class
get information from chrome class
pass information to info class
pass information returned by info class to ics class
'''

from info import str_to_calobj
class generate:
    def __init__(self):
        self.info_list = []
        self.calobj_list=[]
        return
    def get_info(self,lis):
        self.info_list = lis
        return
    def pass_to_info(self):
        obj_lis = str_to_calobj(self.info_list)
        self.calobj_list = obj_lis
        return
    def return_objlist(self):
        return self.calobj_list
    