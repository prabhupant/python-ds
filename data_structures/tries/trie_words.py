class node:
    def __init__(self):
        self.node = {"root":{}}
    def add(self,data):
        temp_node = self.node["root"]
        for j in data:
            if j in temp_node.keys():
                temp_node = temp_node[j]
            else:
                temp_node[j] = {}
                temp_node = temp_node[j]
        else:
            temp_node["flag"] = True
    def display(self):
        print()
        print(self.node)
    def check(self,data):
        temp_node = self.node["root"]
        for j in data:
            if j in temp_node.keys():
                temp_node = temp_node[j]
        else:
            if "flag" in temp_node.keys():
                if temp_node["flag"]==True:
                    print("string:{} exists".format(data))
                else:
                    print("string:{} doesn't exist".format(data))
            else:
                print("string:{} doesn't exist".format(data))
    def autocomplete(self,data):
        temp_node = self.node["root"]
        for j in data:
            if j in temp_node.keys():
                temp_node = temp_node[j]
            else:
                return ""
        print(data,":")
        self.rec1(temp_node)
    def rec1(self,temp):
        for i in temp.keys():
            if "flag" in temp[i].keys():
                print(i,end=" ")
            else:
                print(i,end="")
                self.rec1(temp[i])

n1 = node()
n1.add("anesthesia")
n1.add("antiproject")
n1.add("anime")
n1.add("antartica")
n1.check("anime")
n1.autocomplete("an")
n1.display()
