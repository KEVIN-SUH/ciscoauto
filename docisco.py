import imp


import json
from os import access
from json_file_reader import json_filelist_reader
json_filelist = json_filelist_reader()
for i in json_filelist.filenamelist_without_extension:
    with open("{0}.json".format(i),"r",encoding="UTF-8") as f:
        data = json.load(f)
###########switching###########switching###########switching###########switching###########switching###########switching###########switching###########switching###########switching###########switching###########switching
###########switching###########switching###########switching###########switching###########switching###########switching###########switching###########switching###########switching###########switching###########switching
    if "switching" in data :
        with open("{0}.txt".format(i),"a") as g:
            if "hostname"in data["switching"]:
                g.write("\nconf\n\nhostname {0}\nend".format(data["switching"]["hostname"]))
            if "default_gateway" in data["switching"]:
                g.write("\nconf\n\nip default-gateway {0}\nend".format(data["switching"]["default_gateway"]))
            g.close()    
        if "mls" in data["switching"]:
            with open("{0}.txt".format(i),"a") as g:
                g.write("\nconf\n")
                if "ipv4_use" in data["switching"]["mls"]:
                    if data["switching"]["mls"]["ipv4_use"] == "true":
                        g.write("\nip routing")
                if "ipv6_use" in data["switching"]["mls"]:
                    if data["switching"]["mls"]["ipv6_use"] == "true":
                        g.write("\nipv6 unicast-routing")
                for j in data["switching"]["mls"].keys():
                    g.write("\nint {0}\nno switchport".format(j))
                    if "ip4addr" in data["switching"]["mls"]["{0}".format(j)]:
                        g.write("\nip address {0}".format(data["switching"]["mls"]["{0}".format(j)]["ip4addr"]))
                    if "ip6addr" in data["switching"]["mls"]["{0}".format(j)]:
                        g.write("\nipv6 address {0}".format(data["switching"]["mls"]["{0}".format(j)]["ip6addr"]))   
                g.write("\nno shut\nend") 
            g.close()                         
        if "vlan"in data["switching"]:
            with open("{0}.txt".format(i),"a") as g:
                g.write("\nconf\n")
                for i in list(data["switching"]["vlan"].items()):
                    g.write("\nvlan {0}".format(i[0]))
                    if "name" in data["switching"]["vlan"]["{0}".format(i[0])]:
                        g.write("\nname {0}".format(data["switching"]["vlan"]["{0}".format(i[0])]["name"]))
                    if "svi" in data["switching"]["vlan"]["{0}".format(i[0])]:
                        if data["switching"]["vlan"]["{0}".format(i[0])]["svi"] == "true":
                            g.write("\nint vlan {0}".format(i[0]))
                        if "ip4addr" in data["switching"]["vlan"]["{0}".format(i[0])]:
                            g.write("\nip address {0}\nno shut".format(data["switching"]["vlan"]["{0}".format(i[0])]["ip4addr"]))
                        if "mls" in data["switching"]:
                            if "ipv6_use" in data["switching"]["mls"]:
                                if data["switching"]["mls"]["ipv6_use"] == "true":
                                    if "ip6addr" in data["switching"]["vlan"]["{0}".format(i[0])]:
                                        g.write("\nipv6 address {0}\nno shut".format(data["switching"]["vlan"]["{0}".format(i[0])]["ip6addr"]))
                    if "interfaces" in data["switching"]["vlan"]["{0}".format(i[0])]:
                        int_text=",".join(data["switching"]["vlan"]["{0}".format(i[0])]["interfaces"])  
                        g.write("\nint range {0}".format(int_text))
                    if "voice"in data["switching"]["vlan"]["{0}".format(i[0])]: 
                        if data["switching"]["vlan"]["{0}".format(i[0])]["voice"] == "true":
                            g.write("\nmls qos trust cos\nswitchport voice vlan {0}\nno shut".format(i[0]))   
                    if "switchport_mode" in data["switching"]["vlan"]["{0}".format(i[0])]:
                        if data["switching"]["vlan"]["{0}".format(i[0])]["switchport_mode"] == "access":
                            g.write("\nswitchport mode access\nswitchport access vlan {0}".format(i[0]))
                       
                    if "trunk" in  data["switching"]["vlan"]["{0}".format(i[0])]:
                        if "interfaces" in data["switching"]["vlan"]["{0}".format(i[0])]["trunk"]:
                            int_text=",".join(data["switching"]["vlan"]["{0}".format(i[0])]["trunk"]["interfaces"])  
                            g.write("\nint range {0}".format(int_text))
                        if data["switching"]["vlan"]["{0}".format(i[0])]["trunk"]["switchport_mode"] =="trunk":
                            g.write("\nswitchport mode trunk\nswitchport trunk native vlan {0}\nswitchport trunk allowed vlan {1}".format(i[0],",".join(list(data["switching"]["vlan"].keys()))))
                        if "nonegotiate" in data["switching"]["vlan"]["{0}".format(i[0])]["trunk"]:
                            if data["switching"]["vlan"]["{0}".format(i[0])]["trunk"]["nonegotiate"]=="true":
                                g.write("\nswitchport nonegotiate")                              
                    if "dtp" in  data["switching"]["vlan"]["{0}".format(i[0])]:
                        if "interfaces" in data["switching"]["vlan"]["{0}".format(i[0])]["trunk"]:
                            int_text=",".join(data["switching"]["vlan"]["{0}".format(i[0])]["dtp"]["interfaces"])  
                            g.write("\nint range {0}".format(int_text))
                        if data["switching"]["vlan"]["{0}".format(i[0])]["dtp"]["switchport_mode"] =="dynamic d":
                                g.write("\nswitchport mode dynamic desirable\nswitchport trunk native vlan {0}\nswitchport trunk allowed vlan {1}".format(i[0],",".join(list(data["switching"]["vlan"].keys()))))
                        if data["switching"]["vlan"]["{0}".format(i[0])]["dtp"]["switchport_mode"] =="dynamic a":
                             g.write("\nswitchport mode dynamic auto\nswitchport trunk native vlan {0}\nswitchport trunk allowed vlan {1}".format(i[0],",".join(list(data["switching"]["vlan"].keys()))))
                g.write("\nend")       
            g.close()
########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING
########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING########ROUTING
    if  "routing" in data :
        if "hostname"in data["routing"]:
            with open("{0}.txt".format(i),"a") as g:
                g.write("\nconf\n\nhostname {0}\nend".format(data["routing"]["hostname"]))
            g.close()
        if "interfaces" in data["routing"]:
            with open("{0}.txt".format(i),"a") as g:
                g.write("\nconf\n")
                for i in list(data["routing"]["interfaces"].keys()):
                    g.write("\nint {0}".format(i))
                    if "ip4addr" in data["routing"]["interfaces"]["{0}".format(i)]:
                        g.write("\nip address {0}".format(data["routing"]["interfaces"]["{0}".format(i)]["ip4addr"]))
                    g.write("\nno shut")
                    if "subif" in data["routing"]["interfaces"]["{0}".format(i)]:
                        for j in list(data["routing"]["interfaces"]["{0}".format(i)]["subif"].items()):
                            g.write("\nint {0}.{1}".format(i,j[0]))
                            if "encapsulation" in data["routing"]["interfaces"]["{0}".format(i)]["subif"]["{0}".format(j[0])]:
                                if "native" in data["routing"]["interfaces"]["{0}".format(i)]["subif"]["{0}".format(j[0])] and data["routing"]["interfaces"]["{0}".format(i)]["subif"]["{0}".format(j[0])]["native"]=="true":
                                    g.write("\nencapsulation {0} {1} native".format(data["routing"]["interfaces"]["{0}".format(i)]["subif"]["{0}".format(j[0])]["encapsulation"],j[0]))
                                if not "native" in data["routing"]["interfaces"]["{0}".format(i)]["subif"]["{0}".format(j[0])] or data["routing"]["interfaces"]["{0}".format(i)]["subif"]["{0}".format(j[0])]["native"]=="false":
                                     g.write("\nencapsulation {0} {1}".format(data["routing"]["interfaces"]["{0}".format(i)]["subif"]["{0}".format(j[0])]["encapsulation"],j[0]))
                            if "ip4addr" in data["routing"]["interfaces"]["{0}".format(i)]["subif"]["{0}".format(j[0])]:
                                g.write("\nip address {0}\nno shut".format(data["routing"]["interfaces"]["{0}".format(i)]["subif"]["{0}".format(j[0])]["ip4addr"]))
    
    g.close()                                                            
    print(data)
    f.close()
print("   ----complete----   ")
    