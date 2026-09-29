
dispositivos_red = {
    101: {
        "ip": "192.168.1.10",
        "device_name": "Router Principal",
        "policy": "ALLOW_ALL",
        "status": "Activo"
    },
    102: {
        "ip": "192.168.1.20",
        "device_name": "Servidor Web",
        "policy": "BLOCK_IP",
        "status": "Activo"
    },
    103: {
        "ip": "192.168.1.30",
        "device_name": "Switch A",
        "policy": "REQUIRED_IP",
        "status": "Inactivo"
    },
    104: {
        "ip": "192.168.1.40",
        "device_name": "Firewall",
        "policy": "REQUIRED_IP",
        "status": "Activo"
    },
    105: {
        "ip": "192.168.1.50",
        "device_name": "PC Administrador",
        "policy": "ALLOW_ALL",
        "status": "Inactivo"
    }
}


def validar_politica(dispositivo):
    """
    Valida la política configurada en el dispositivo y devuelve un mensaje.
    """
    politica = dispositivo['policy']
    ip = dispositivo['ip']
    
    if politica == "ALLOW_ALL":
        return "Configuración válida"
        
    elif politica == "BLOCK_IP":
        return "Configuración inválida (IP bloqueada)"
        
    elif politica == "REQUIRED_IP":
        if ip == "192.168.1.40":
            return "Configuración válida"
        else:
            return "Configuración inválida (IP incorrecta)"
            
    return "Configuración inválida"


def mostrar_dispositivos(dispositivos):
    """
    Recorre el diccionario principal y muestra la información detallada de cada dispositivo.
    """
    print("--- DETALLE DE DISPOSITIVOS ---")
    for id_disp, info in dispositivos.items():
        resultado = validar_politica(info)
        
        print(f"1.\tID: {id_disp}")
        print(f"2.\tNombre: {info['device_name']}")
        print(f"3.\tIP: {info['ip']}")
        print(f"4.\tPolítica: {info['policy']}")
        print(f"5.\tEstado: {info['status']}")
        print(f"6.\tResultado: {resultado}")
        print("") 



def generar_resumen(dispositivos):
    """
    Genera estadísticas generales de la red contabilizando estados y validez.
    """
    activos = 0
    inactivos = 0
    validas = 0
    invalidas = 0
    
    for info in dispositivos.values():
        
        # Contar estados
        if info['status'] == "Activo":
            activos += 1
        elif info['status'] == "Inactivo":
            inactivos += 1
            
        resultado = validar_politica(info)
        if "inválida" in resultado:
            invalidas += 1
        else:
            validas += 1
            
    print("RESUMEN DE LA RED")
    print(f"1.\tDispositivos Activos: {activos}")
    print(f"2.\tDispositivos Inactivos: {inactivos}")
    print(f"3.\tConfiguraciones Válidas: {validas}")
    print(f"4.\tConfiguraciones Inválidas: {invalidas}")
    print("-" * 30)
    print("¡Mucha Suerte!")



if __name__ == "__main__":
    mostrar_dispositivos(dispositivos_red)
    generar_resumen(dispositivos_red)

    