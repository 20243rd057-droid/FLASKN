from flask import Flask, jsonify
import json

with open("API.json", "r") as json_api:
    datos_json = json.load(json_api)

app = Flask(__name__)

# Endpoint HTML


@app.route('/json/<mac>')
def json_data(mac):

    print(datos_json[mac]["Name"])
    print(datos_json[mac]["Protocolos"])
    print(datos_json[mac]["VLANs"])
    print(datos_json[mac]["status"])
      
    
    
    return datos_json[mac]["Name"]
    




# Endpoint JSON
@app.route('/servidor_1')
def servidor_1():
    return jsonify({
    "0001": {
        "ip": "192.168.0.1",
        "divice": "Router",
        "policy": ["Ro", "Not Allowed", [0.2, 0.3, 0.5] ],
        "status": True,
    }
})

if __name__ == '__main__':
    app.run(debug=True)