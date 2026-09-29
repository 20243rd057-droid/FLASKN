net_config = {
    "0001":{
        "ip": "192.168.0.1.",
        "divice": "router",
        "policy": "allow all",
        "status": True,
        "lista": [1,2,3,4,5]
        
    },

    "0002":{
        "ip": "192.168.0.2.",
        "divice": "router",
        "policy": "allow all",
        "status": True
    },


    "0003":{
            "ip": "192.168.0.3.",
            "divice": "router",
            "policy": "allow all",
            "status": True
        },
    "0004":{
        "ip": "192.168.0.4.",
        "divice": "router",
        "policy": "allow all",
        "status": True
    },

    "0005":{
        "ip": "192.168.0.5.",
        "divice": "router",
        "policy": "allow all",
        "status": True
    }

}
#a = [1,2,3, [7.8, 1]]
#yaENUso = a.pop(3)
#print (yaENUso)
#contenido  = net_config.get("0001")
#listaA = contenido.get('lista')
#num = listaA[2]
#print(num)
#print(net_config.get("0001").get("lista")[2])

print(net_config.get("0001").get("lista")[2])
net_config['0002'] = {  "ip":   1   }
print(net_config)
