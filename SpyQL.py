import sqlite3
import random

def inicializar_bd():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

#   SECCION DE TABLAS, AQUI ESTAN TODAS LAS TABLAS NECESARIAS,
#   DIVIDO POR LAS MISIONES


# Mision 1
    cursor.execute('''
        CREATE TABLE departamentos (
                   id_dep INTEGER PRIMARY KEY,
                   nombre TEXT,
                   nivel_seguridad INTEGER
                   )
''')
    
# Mision 2
    cursor.execute ('''
        CREATE TABLE empleados (
                    id_emp INTEGER PRIMARY KEY,
                    nombre TEXT,
                    apellido TEXT,
                    rol TEXT, 
                    id_dep INTEGER,
                    salario REAL,
                    FOREIGN KEY (id_dep) REFERENCES departamentos(id_dep)
                    )
    ''')

# Mision 3
    cursor.execute('''
        CREATE TABLE registros_de_red (
                   id_registros INTEGER PRIMARY KEY,
                   id_servidor INTEGER,
                   tipo_evento TEXT,
                   criticidad TEXT
                   )     
    ''')

# Mision 4
    cursor.execute('''
        CREATE TABLE terminales_red (
                   id_terminal INTEGER PRIMARY KEY,
                   nombre_servidor TEXT,
                   direccion_ip TEXT,
                   estado_nodo TEXT
                   )
    ''')

# Mision 5
    cursor.execute ('''
        CREATE TABLE transacciones_negras (
                    id_transaccion INTEGER PRIMARY KEY,
                    cuenta_origen TEXT,
                    monto REAL,
                    tipo_operacion TEXT
                    )
    ''')

# Mision 6
    cursor.execute ('''
        CREATE TABLE infraestructura_zonas (
                    id_nodo INTEGER PRIMARY KEY,
                    zona_edificio TEXT,
                    tipo_dispositivo TEXT,
                    estado TEXT
                    )    
    ''')

# Mision 7 y Mision 8 reutiliza tablas. -VidaEcologica-

# Mision 9
    cursor.execute('''
            CREATE TABLE proyectos_secretos (
                id_proyecto INTEGER PRIMARY KEY,
                nombre_proyecto TEXT,
                id_supervisor INTEGER
            )
        ''')

# Mision 10 
    cursor.execute ('''
        CREATE TABLE terminales_bloqueadas (
                    id_bloqueo INTEGER PRIMARY KEY,
                    hash_seguridad TEXT,
                    fecha_registro TEXT
        )
    ''')

# Fin de las Tablas
# Iniciamos los datos que van a rellenar esas tablas

# Datos Mision 1
    deps = [
    (1, 'Ciberseguridad', 5),
    (2, 'Desarrollo de Armamento', 4),
    (3, 'Recursos Humanos', 1)
]
    cursor.executemany('INSERT INTO departamentos VALUES (?,?,?)', deps)

# Datos Mision 2
    empleados = [
        (101, 'Carmen', 'Rosa', 'Ingenieria Principal', 2, 8500.00),
        (102, 'Sebastian', 'Pernia', 'Director de Seguridad', 1, 12000.00),
        (103, 'Casimiro', 'Olegario', 'Analista de Sistemas', 2, 4500.00),
        (104, 'Berenice', 'Cartaya', 'Especialista de Phishing', 2, 3800.00),
        (105, 'Daniel', 'Torbet', 'Asistente', 3, 25.00)
    ]
    cursor.executemany('INSERT INTO empleados VALUES (?,?,?,?,?,?)', empleados)

# Datos Mision 3
    registros = [
        (1, 10, 'Intrusión Detectada', 'ALTA'),
        (2, 15, 'Mantenimiento Semanal', 'BAJA'),
        (3, 22, 'Fuga de Datos', 'ALTA'),
        (4, 35, 'Actualización de OS', 'BAJA'),
        (5, 42, 'Fuerza Bruta SSH', 'ALTA'),
        (6, 50, 'Reinicio de Servidor', 'MEDIA'),
    ]
    cursor.executemany('INSERT INTO registros_de_red VALUES (?,?,?,?)', registros)

# Datos Mision 4
    terminales = [
        (1, 'SRV-SEC-ALFA-01', '192.168.1.10', 'ACTIVO'),
        (2, 'PROXY-BACKUP-CORE', '10.0.0.5', 'INACTIVO'),
        (3, 'SRV-SEC-BETA-02', '192.168.2.15', 'ACTIVO'),
        (4, 'DATA-STORAGE-OMEGA', '10.100.4.1', 'ACTIVO'),
        (5, 'GATEWAY-EXTERNAL', '172.16.0.1', 'ACTIVO'),
        (6, 'SRV-DATA-EPSILON', '192.168.3.50', 'MANTENIMIENTO')
    ]
    cursor.executemany('INSERT INTO terminales_red VALUES (?,?,?,?)', terminales)

# Datos Mision 5
    transacciones = [
        (1, 'ACC-9921', 15000.50, 'DESVIO'),
        (2, 'ACC-4412', 45000.00, 'SOBORNO'),
        (3, 'ACC-9921', 8500.25, 'DESVIO'),
        (4, 'ACC-1082', 120000.00, 'LAVADO'),
        (5, 'ACC-4412', 3200.00, 'SOBORNO'),
        (6, 'ACC-5521', 62000.75, 'LAVADO')
    ]
    cursor.executemany('INSERT INTO transacciones_negras VALUES (?,?,?,?)', transacciones)

# Datos Mision 6
    nodos = [
        (1, 'SECTOR A', 'Servidor', 'ACTIVO'),
        (2, 'SECTOR A', 'Router', 'ACTIVO'),
        (3, 'SECTOR B', 'Servidor', 'ACTIVO'),
        (4, 'SECTOR B', 'Switch', 'INACTIVO'),
        (5, 'SECTOR C', 'Firewall', 'ACTIVO'),
        (6, 'SECTOR A', 'SERVIDOR', 'ACTIVO'),
        (7, 'SECTOR C', 'SERVIDOR', 'ACTIVO'),
    ]
    cursor.executemany('INSERT INTO infraestructura_zonas VALUES (?,?,?,?)', nodos)

# Datos adicionales Mision 7
    nuevos_nodos = [
        (8, 'SECTOR B', 'Firewall', 'ACTIVO'),
        (9, 'SECTOR B', 'Router', 'ACTIVO'),
        (10, 'SECTOR C', 'Switch', 'ACTIVO'),
        (11, 'SECTOR A', 'Terminal', 'ACTIVO'),
    ]
    cursor.executemany('INSERT INTO infraestructura_zonas VALUES (?,?,?,?)', nuevos_nodos)

# Datos Mision 9
    proyectos = [
        (1, 'Proyecto Icaro', 101), # Supervisor Carmen Rosa
        (2, 'Proyecto Chronos', None), # Sin Supervisor (Punto Ciego)
        (3, 'Proyecto Titan', 102), # Otro supervisor
        (4, 'Proyecto Nemesis', None) # Sin Supervisor (Punto Ciego)
    ]
    cursor.executemany('INSERT INTO proyectos_secretos VALUES (?,?,?)', proyectos)

# Datos Mision 10
    bloqueos = [
        (1, 'KEY-99218-XYZ', '2026-07-15'),
        (2, 'KEY-44123-ABC', '2026-07-16'),
        (3, 'KEY-10829-JKL', '2026-07-17')
    ]
    cursor.executemany('INSERT INTO terminales_bloqueadas VALUES (?,?,?)', bloqueos)

# Fin
    conn.commit()
    return conn

# Validador

def validar_consulta(conn, query_usuario, query_maestro):
    cursor = conn.cursor()
    try:
        es_dml = any(keyword in query_usuario.lower() for keyword in ["update", "delete", "insert"])

        if es_dml:
            cursor.execute("SAVEPOINT validacion_temporal;")

            # 1. Ejecutar maestro y capturar el estado resultante de las tablas afectadas
            cursor.execute(query_maestro)
            # Obtenemos la foto de la tabla (ej. terminales_bloqueadas o registros_de_red)
            cursor.execute("SELECT * FROM terminales_bloqueadas")
            estado_maestro_bloqueadas = cursor.fetchall()
            cursor.execute("SELECT * FROM registros_de_red")
            estado_maestro_registros = cursor.fetchall()

            # Restaurar estado inicial
            cursor.execute("ROLLBACK TO validacion_temporal;")

            # 2. Ejecutar usuario y capturar el estado resultante
            cursor.execute(query_usuario)
            cursor.execute("SELECT * FROM terminales_bloqueadas")
            estado_usuario_bloqueadas = cursor.fetchall()
            cursor.execute("SELECT * FROM registros_de_red")
            estado_usuario_registros = cursor.fetchall()

            # Liberar el savepoint
            cursor.execute("RELEASE validacion_temporal;")

            # 3. Comparar que ambas tablas hayan quedado exactamente iguales
            es_valido = (estado_maestro_bloqueadas == estado_usuario_bloqueadas and 
                         estado_maestro_registros == estado_usuario_registros)
            
            if es_valido:
                cursor.execute(query_usuario)
                
            return es_valido
        
        else: 
            cursor.execute(query_maestro)
            resultado_maestro = cursor.fetchall()

            cursor.execute(query_usuario)
            resultado_usuario = cursor.fetchall()

            return resultado_maestro == resultado_usuario
        
    except sqlite3.Error as e:
        print(f"\n [Sistema]: Error en la sintaxis SQL: {e}")
        return False
    finally: 
        cursor.close() # Esto es para que siempre se cierre la consulta y evitar saturar la memoria
# Fin

# Iniciamos con la definicion de cada nivel 
# Mision 1
def jugar_mision_1(conn):
    # Tomamos un proyecto al azar
    id_proyecto_azar = random.choice([1,2,3])

    # Esto es para que el enunciado sea variado
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM departamentos WHERE id_dep = ?", (id_proyecto_azar,))
    nombre_dep = cursor.fetchone()[0]
    cursor.close()

    enunciado = f"Bienvenido Agente, debes infiltrate en la Base de Datos de la corporación. \n Tu primera misión 1 es conocer el apellido y el rol de los empleados del departamento '{nombre_dep}'."
    query_maestro = f"SELECT apellido, rol FROM empleados WHERE id_dep = {id_proyecto_azar}"
    intentos = 3

    print("\n<><><><><><><><><><><><><><><><><><>")
    print(" CONEXIÓN ESTABLECIDA: Servidor General OMNICORP ")
    print("<><><><><><><><><><><><><><><><><><>")
    print(enunciado)
    print("Consejos: Las tablas disponibles son 'empleados' y 'departamentos'. \n")

    while intentos > 0:
        query_jugador = input(f"[{intentos} intentos restantes] SQL_SHELL> ")

        if validar_consulta(conn, query_jugador, query_maestro):
            print("\n [SISTEMA]: ¡Acceso Concedido! \n Extrayendo datos. . . \n Descarga Completa.")
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print("[SISTEMA - ALERTA] Acceso negado, por favor comunicarse con su superior.")
            else:
                print("\n[SISTEMA - ALARMA]: Se ha detectado una intrusión al sistema. Desconexión forzosa.")
                return False
    
# Mision 2
def jugar_mision_2(conn):
    nivel_corte_azar = random.choice([4, 5])

    enunciado = (
        f"Avanzaste, pero el cortafuegos bloquea el paso.\n"
        f"Necesitas extraer el 'nombre' del empleado y el 'nivel_seguridad' de su departamento, "
        f"pero SOLO para aquellos departamentos con un nivel de seguridad IGUAL O MAYOR a {nivel_corte_azar}.\n"
        f"Te aconsejo usar un JOIN \npara cruzar 'empleados' y 'departamentos'."
    )
    consejo = (
    f"SELECT [necesitas los empleados, departamentos] \nFROM [departamento] \nINNER JOIN - \nWHERE"
)
    query_maestro = f"""
        SELECT empleados.nombre, departamentos.nivel_seguridad 
        FROM empleados 
        INNER JOIN departamentos ON empleados.id_dep = departamentos.id_dep 
        WHERE departamentos.nivel_seguridad >= {nivel_corte_azar}
    """

    intentos = 3
    print("\n<><><><><><><><><><><><><><><><><><>")
    print(" CONEXIÓN: Servidor General OMNICORP ")
    print("<><><><><><><><><><><><><><><><><><>")
    print(enunciado)
    print("Tablas: 'empleados' (id_emp, nombre, apellido, rol, id_dep, sueldo)")
    print("        'departamentos' (id_dep, nombre, nivel_seguridad)\n")
    
    print(consejo)

    while intentos > 0:
        query_jugador = input(f"[{intentos} intentos restantes] SQL_SHELL> ")
        
        if validar_consulta(conn, query_jugador, query_maestro):
            print("\n[SISTEMA]: Credenciales de alto nivel obtenidas.")
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print("[SISTEMA - ALERTA] Acceso negado, por favor comunicarse con su superior.")
            else:
                print("\n[SISTEMA - ALARMA]: Se ha detectado una intrusión al sistema. Desconexión forzosa.")
                return False

# Mision 3
def jugar_mision_3(conn):
    rango_inicio = random.choice([10, 15])
    rango_fin = random.choice([40, 45])
    
    enunciado = (
        f"Sigue así. El analizador de tráfico requiere un filtrado estricto.\n"
        f"Extrae todas las columnas de la tabla 'registros_de_red' para aquellos eventos\n"
        f"cuyo 'id_servidor' esté entre {rango_inicio} y {rango_fin} (inclusive),\n"
        f"pero asegúrate de que la 'criticidad' NO sea 'BAJA'."
    )
    
    # Query maestro con BETWEEN y NOT
    query_maestro = f"""
        SELECT * FROM registros_de_red 
        WHERE id_servidor BETWEEN {rango_inicio} AND {rango_fin} 
        AND NOT criticidad = 'BAJA'
    """
    consejo = (
        f"SELECT (todos) FROM [departamento] \nWHERE [donde] BETWEEN inicia AND fin\n AND NOT (detalle final)."
        )
    intentos = 3
    # Imprimir enunciado
    print("\n<><><><><><><><><><><><><><><><><><>")
    print(" CONEXIÓN: Servidor General OMNICORP ")
    print("<><><><><><><><><><><><><><><><><><>")
    print(enunciado)
    print("Tablas: 'registros_de_red' (id_registro, id_servidor, tipo_evento, criticidad)\n")
    print(consejo)

    # Bucle
    while intentos > 0:
        query_jugador = input(f"[{intentos} intentos restantes] SQL_SHELL> ")
        
        if validar_consulta(conn, query_jugador, query_maestro):
            print("\n[SISTEMA]: Descifrando logs de intrusión corporativa...")
            print("Agente: El camino hacia el nodo central está despejado.\n")
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print("[SISTEMA - ALERTA]: Filtro erróneo. Los cortafuegos están recalculando la ruta.")
            else:
                print("\n[SISTEMA - ALARMA]:  Intrusión detectada. Conexión cerrada.")
                return False

# Mision 4
def jugar_mision_4(conn):
    variante = random.choice(['SEC', 'DATA'])
    
    if variante == 'SEC':
        enunciado = (
            f"Cuidado agente, el sistema de rastreo enemigo está activo.\n"
            f"Necesitamos aislar las terminales de seguridad. Selecciona todas las columnas\n"
            f"de 'terminales_red' cuyo 'nombre_servidor' COMIENCE exactamente con las siglas 'SRV-SEC'.\n"
            f"Además, el 'estado_nodo' debe ser 'ACTIVO'."
        )
        query_maestro = "SELECT * FROM terminales_red WHERE nombre_servidor LIKE 'SRV-SEC%' AND estado_nodo = 'ACTIVO'"
    else:
        enunciado = (
            f"Atención agente, OmniCorp está ocultando un repositorio de datos.\n"
            f"Extrae todas las columnas de la tabla 'terminales_red' para los servidores\n"
            f"cuyo 'nombre_servidor' CONTENGA la palabra 'DATA' en cualquier posición.\n"
            f"Asegúrate de que el 'estado_nodo' sea 'ACTIVO'."
        )
        query_maestro = "SELECT * FROM terminales_red WHERE nombre_servidor LIKE '%DATA%' AND estado_nodo = 'ACTIVO'"
        
    # Enunciado
    intentos = 3
    print("\n!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>!<")
    print(" CONEXIÓN: Servidor General OMNICORP ")
    print("!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>!<")
    print(enunciado)
    print("Tablas: 'terminales_red' (id_terminal, nombre_servidor, direccion_ip, estado_nodo)\n")
    print("Sin pistas esta vez.")
    # Bucle
    while intentos > 0:
        query_jugador = input(f"[{intentos} intentos restantes] SQL_SHELL> ")
        
        if validar_consulta(conn, query_jugador, query_maestro):
            print("\n[SISTEMA]: <Nodo Encontrado> Patrón de texto coincidente. Extrayendo logs...")
            print("Agente: Guardando coordenadas del servidor en el dispositivo.\n")
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print("[SISTEMA - ALERTA]: El escaneo falló. El acceso a estos archivos es clasificado.")
            else:
                print("\n[SISTEMA - ALARMA]: Barrido de seguridad completado. Expulsando todas las conexiones.")
                return False

# Mision 5
def jugar_mision_5(conn):
    operacion_azar = random.choice(['DESVIO', 'SOBORNO', 'LAVADO'])
    calculo_azar = random.choice(['SUM', 'AVG', 'MAX'])
    
    # Configuramos el enunciado según la combinación aleatoria
    if calculo_azar == 'SUM':
        detalle_calculo = "la SUMA TOTAL (sum)"
        query_maestro = f"SELECT sum(monto) AS total FROM transacciones_negras WHERE tipo_operacion = '{operacion_azar}'"
    elif calculo_azar == 'AVG':
        detalle_calculo = "el PROMEDIO (avg)"
        query_maestro = f"SELECT avg(monto) AS promedio FROM transacciones_negras WHERE tipo_operacion = '{operacion_azar}'"
    else:
        detalle_calculo = "el MONTO MÁXIMO (max)"
        query_maestro = f"SELECT max(monto) AS maximo FROM transacciones_negras WHERE tipo_operacion = '{operacion_azar}'"

    enunciado = (
        f"Debemos conocer el libro contable de OMNICORP.\n"
        f"Usa una función de agregado para calcular {detalle_calculo} de la columna 'monto'\n"
        f"ÚNICAMENTE para las transacciones cuyo 'tipo_operacion' sea '{operacion_azar}'.\n"
        f"Recuerda asignarle un alias a la columna calculada para que el informe se vea limpio."
    )
        
    # Bucle
    intentos = 3
    print("\n!<!!<!!<!!<!!<!!<!!<!!<!!<!!<!!<!!<")
    print(" C0N3XI0N: S3rv¡d0r G3n3ra1 0MNIC0RP ")
    print("!<!!<!!<!!<!!<!!<!!<!!<!!<!!<!!<!!<")
    print(enunciado)
    print("Tablas: 'transacciones_negras' (id_transaccion, cuenta_origen, monto, tipo_operacion)\n")
    
    while intentos > 0:
        query_jugador = input(f"[{intentos} intentos restantes] SQL_SHELL> ")
        
        if validar_consulta(conn, query_jugador, query_maestro):
            print("\n[SIST3MA]: Valores financieros interceptados con éxito.")
            print("Agente: Desviando fondos a cuentas seguras. Conexión limpia.\n")
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print("[SISTEMA - ALERTA]: El balance no cuadra.")
                print("\nRecuerda que no debes mezclar campos normales con funciones de agregado.")
            else:
                print("\n[SISTEMA - ALARMA]: Intrusión detectada - Desconectando conexión, rastreando.")
                return False           

# Mision 6
def jugar_mision_6(conn):
    criterio_azar = random.choice(['zona_edificio', 'tipo_dispositivo'])
    
    if criterio_azar == 'zona_edificio':
        enunciado = (
            "Estamos mapeando la densidad de la red corporativa.\n"
            "Cuenta cuántos nodos ('COUNT(*)') están operativos por cada 'zona_edificio'.\n"
            "Para ello, selecciona la columna 'zona_edificio' junto al conteo,\n"
            "asegúrate de filtrar solo los que tengan 'estado' = 'ACTIVO' y agrúpalos como corresponde."
        )
        query_maestro = "SELECT zona_edificio, count(*) FROM infraestructura_zonas WHERE estado = 'ACTIVO' GROUP BY zona_edificio"
    else:
        enunciado = (
            "Estamos identificando hardware militar en el servidor.\n"
            "Necesitamos saber cuántos dispositivos activos hay de cada clase.\n"
            "Selecciona la columna 'tipo_dispositivo' junto al conteo de registros ('COUNT(*)'),\n"
            "filtra solo los nodos con 'estado' = 'ACTIVO' y agrúpalos por ese tipo de hardware."
        )
        query_maestro = "SELECT tipo_dispositivo, count(*) FROM infraestructura_zonas WHERE estado = 'ACTIVO' GROUP BY tipo_dispositivo"
        
    # BUCLE
    intentos = 3
    print("\n!<!!ERROR!!<!!<!!<!ERROR!!<!!<!!<!!<")
    print(" C0N3XI0N: S3rv¡d0r ??????? 0MNIC0RP ")
    print("!<!!<!!<ERROR!<!!<!!<!/<!!-!!ERROR!!<\n")
    print(enunciado)
    print("Tablas: 'infraestructura_zonas' (id_nodo, zona_edificio, tipo_dispositivo, estado)\n")
    
    while intentos > 0:
        query_jugador = input(f"[{intentos} intentos restantes] SQL_SHELL> ")
        
        if validar_consulta(conn, query_jugador, query_maestro):
            print("\n[SISTEMA]: <Datos Agrupados> Infraestructura mapeada por completo.")
            print("Agente: Los planos de la red han sido enviados al cuartel general.\n")
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print("[SISTEMA - ALERTA]: Error en la agrupación.")
                print("\nRecuerda incluir en el GROUP BY la columna no agregada del SELECT.")
            else:
                print("\n[SISTEMA - ALARMA]: Bloqueo de subred activado. Escaneo interrumpido.")
                return False

# Mision 7
def jugar_mision_7(conn):
    umbral_azar = random.choice([2, 3])
    
    enunciado = (
        f"\nEstamos logrando interceptando subredes congestionadas.\n"
        f"Necesitamos identificar qué zonas del edificio concentran el tráfico pesado.\n"
        f"Selecciona la columna 'zona_edificio' junto al conteo de dispositivos ('COUNT(*)'),\n"
        f"filtra solo los registros cuyo 'estado' sea 'ACTIVO', agrúpalos por 'zona_edificio'\n"
        f"y muestra ÚNICAMENTE los grupos que tengan MÁS DE {umbral_azar} dispositivos activos.\n"
        
    )
    
    # Query maestro. NOTA: WHERE (filtra las filas antes del cálculo) y HAVING (filtra el resultado del COUNT)
    query_maestro = f"""
        SELECT zona_edificio, count(*) 
        FROM infraestructura_zonas 
        WHERE estado = 'ACTIVO' 
        GROUP BY zona_edificio 
        HAVING count(*) > {umbral_azar}
    """
        
    # Bucle
    intentos = 3
    print("\n+-+[]<!!<!!<!!<!!CountingSort!!<!!<!!<")
    print(" C0N3XI0N: SERvidor //ERROR// Corporacion Omni ")
    print("!<!SERVIDOR<!SERVIDOR!!<LEONSKENEDY!<!!<\n")
    print(enunciado)
    print("Tablas: 'infraestructura_zonas' (id_nodo, zona_edificio, tipo_dispositivo, estado)\n")
    
    while intentos > 0:
        query_jugador = input(f"[{intentos} intentos restantes] SQL_SHELL> ")
        
        if validar_consulta(conn, query_jugador, query_maestro):
            print("\n[SISTEMA OVERRIDE]: Filtro de agregación exitoso.")
            print("[SISTEMA]: Nodos críticos aislados. El cortafuegos principal está perdiendo estabilidad.\n")
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print("[SISTEMA - ALERTA]: Error en la consulta. \nRecuerda: las condiciones sobre funciones como COUNT(*) van en el HAVING, no en el WHERE.")
            else:
                print("\n[SISTEMA - ALARMA]: Contramedidas automáticas aplicadas. Expulsión del servidor.")
                return False

# Mision 8
def jugar_mision_8(conn):
    orden_azar = random.choice(['ASC', 'DESC'])
    
    if orden_azar == 'ASC':
        enunciado = (
            "Debemos priorizar el cortafuegos de menor resistencia.\n"
            "Selecciona las columnas 'cuenta_origen' y 'monto' de la tabla 'transacciones_negras'.\n"
            "Ordena los resultados por la columna 'monto' de forma ASCENDENTE (de menor a mayor).\n"
        )
        query_maestro = "SELECT cuenta_origen, monto FROM transacciones_negras ORDER BY monto ASC"
    else:
        enunciado = (
            "Logramos identificar los activos más valiosos.\n"
            "Selecciona las columnas 'cuenta_origen' y 'monto' de la tabla 'transacciones_negras'.\n"
            "Ordena los resultados por la columna 'monto' de forma DESCENDENTE (de mayor a menor)."
        )
        query_maestro = "SELECT cuenta_origen, monto FROM transacciones_negras ORDER BY monto DESC"
        
    # Bucle
    intentos = 3
    print("\n")
    print(" CONEXION??? SERvidor //ERROR// Corporacion Omni ")
    print("\n")
    print(enunciado)
    print("Tablas: 'transacciones_negras' (id_transaccion, cuenta_origen, monto, tipo_operacion)\n")
    
    while intentos > 0:
        query_jugador = input(f"[{intentos} intentos restantes] SQL_SHELL> ")
        
        if validar_consulta(conn, query_jugador, query_maestro):
            print("\n[SISTEMA]: La lista se ha estructurado perfectamente.")
            print("Objetivos ordenados y listos para la inyección de código.\n")
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print("[SISTEMA - ALERTA]: El orden es incorrecto. \nRecuerda usar ASC o DESC al final de la cláusula según corresponda.")
            else:
                print("\n[SISTEMA - ALARMA]: Error repetido. Desconexión del terminal.")
                return False

# Mision 9
def jugar_mision_9(conn):
    variante_azar = random.choice(['DESATENDIDOS', 'ASIGNADOS'])
    
    if variante_azar == 'DESATENDIDOS':
        enunciado = (
            "Estamos escaneando puntos ciegos en la seguridad de OmniCorp.\n"
            "Necesitamos listar los proyectos secretos que NO tienen un supervisor asignado.\n"
            "Selecciona las columnas 'id_proyecto' y 'nombre_proyecto' de la tabla 'proyectos_secretos'.\n"
            "Usa un LEFT JOIN con la tabla 'empleados' (vinculando por 'id_supervisor' e 'id_emp')\n"
            "y aplica un filtro en el WHERE usando 'IS NULL' para aislar los proyectos huérfanos."
        )
        query_maestro = """
            SELECT P.id_proyecto, P.nombre_proyecto 
            FROM proyectos_secretos P 
            LEFT JOIN empleados E ON P.id_supervisor = E.id_emp 
            WHERE E.id_emp IS NULL
        """
    else:
        enunciado = (
            "Identificando las cabezas de los proyectos enemigos.\n"
            "Necesitamos listar los proyectos que SÍ tienen un supervisor asignado actualmente.\n"
            "Selecciona las columnas 'id_proyecto' y 'nombre_proyecto' de la tabla 'proyectos_secretos'.\n"
            "Usa un LEFT JOIN con la tabla 'empleados' (vinculando por 'id_supervisor' e 'id_emp')\n"
            "y aplica un filtro en el WHERE usando 'IS NOT NULL' para asegurar que tengan supervisor."
        )
        query_maestro = """
            SELECT P.id_proyecto, P.nombre_proyecto 
            FROM proyectos_secretos P 
            LEFT JOIN empleados E ON P.id_supervisor = E.id_emp 
            WHERE E.id_emp IS NOT NULL
        """
        
    # Bucle
    intentos = 3
    print("\n")
    print(" <> Servidor OMNICORP <> ")
    print("\n")
    print(enunciado)
    print("Tablas: 'proyectos_secretos' (id_proyecto, nombre_proyecto, id_supervisor)")
    print("        'empleados' (id_emp, nombre, apellido, rol, id_dep)\n")
    
    while intentos > 0:
        query_jugador = input(f"[{intentos} intentos restantes] SQL_SHELL> ")
        
        if validar_consulta(conn, query_jugador, query_maestro):
            print("\n[SISTEMA]: Peligro, brecha de seguridad hallada. Reporte de inmediato.")
            print("Agente: Estoy accediendo a la documentación oculta del proyecto corporativo...\n")
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print("[SISTEMA - ALERTA]: Consulta errónea.\n Recuerda que el JOIN debe mantener la tabla izquierda íntegra.")
            else:
                print("\n[SISTEMA - ALARMA]: Barrido de integridad completado. Acceso revocado.")
                return False

# Mision 10
def jugar_mision_10(conn):
    variante_azar = random.choice(['DESENCRIPTAR_HASH', 'FORMATO_FECHA'])
    
    if variante_azar == 'DESENCRIPTAR_HASH':
        enunciado = (
            "Debemos extraer la firma digital del enemigo.\n"
            "El núcleo del hash de seguridad contiene el código de acceso real.\n"
            "Usa la función 'substr()' para extraer únicamente los 5 números centrales de la columna 'hash_seguridad'.\n"
            "Sabiendo que los registros tienen la forma 'KEY-XXXXX-XYZ', debes cortar desde la posición 5 y tomar 5 caracteres.\n"
            "\nRenombra la columna calculada como 'codigo_limpio' en tu SELECT."
            "\nConsejo: SELECT substr(hash_seguridad, 5, 5)"
        )
        # Querymaestro substr(hash_seguridad, 5, 5) extrae los números centrales
        query_maestro = "SELECT substr(hash_seguridad, 5, 5) AS codigo_limpio FROM terminales_bloqueadas"
    else:
        enunciado = (
            "Estamos formateando las marcas de tiempo para el reporte.\n"
            "La fecha de registro está en formato estándar ISO (YYYY-MM-DD), pero la resistencia la necesita en día/mes/año.\n"
            "Usa la función nativa 'strftime()' de SQLite para reformatear la columna 'fecha_registro' a '%d/%m/%Y'.\n"
            "\nPasa los parámetros correspondientes: strftime('%d/%m/%Y', fecha_registro) y asígnale el alias 'fecha_limpia'."
            "\nConsejo: SELECT strftime('%d/%m/%Y', fecha_registro)."
        )
        query_maestro = "SELECT strftime('%d/%m/%Y', fecha_registro) AS fecha_limpia FROM terminales_bloqueadas"
        
    # Bucle
    intentos = 3
    print("\n")
    print(" <...> Servidor OMNICORP <...> ")
    print("\n")
    print(enunciado)
    print("Tablas: 'terminales_bloqueadas' (id_bloqueo, hash_seguridad, fecha_registro)\n")
    
    while intentos > 0:
        query_jugador = input(f"[{intentos} intentos restantes] SQL_SHELL> ")
        
        if validar_consulta(conn, query_jugador, query_maestro):
            print("\n[SISTEMA]: Funciones ejecutadas con éxito.")
            print("El texto corrupto se ha limpiado y las credenciales son legibles.\n")
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print("[SISTEMA - ALERTA]: Error de sintaxis o transformación. \nRevisa los argumentos de la función nativa.")
            else:
                print("\n[SISTEMA - ALARMA]: Incoherencia de datos detectada por el servidor. Desconexión.")
                return False

# Mision 11
def jugar_mision_11(conn):
    # Variabilidad: El sistema elegirá al azar si pedirte el empleado con el salario máximo o mínimo
    variante_azar = random.choice(['MAXIMO', 'MINIMO'])
    
    if variante_azar == 'MAXIMO':
        enunciado = (
            "Identificando la cuenta del administrador supremo.\n"
            "Necesitamos aislar los datos del empleado que percibe el sueldo más alto de la corporación.\n"
            "Selecciona las columnas 'nombre', 'apellido' y 'salario' de la tabla 'empleados'.\n"
            "Consejo: Usa una subconsulta en la cláusula WHERE que calcule el valor máximo ('max(salario)')\n"
            "para compararlo con el salario de la consulta principal."
        )
        # Filtro de un solo valor usando una subconsulta que devuelve el salario máximo
        query_maestro = """
            SELECT nombre, apellido, salario 
            FROM empleados 
            WHERE salario = (SELECT max(salario) FROM empleados)
        """
    else:
        enunciado = (
            "Detectando la cuenta de menor actividad (vulnerabilidad de acceso).\n"
            "Para evitar levantar sospechas, interceptaremos la cuenta con el sueldo más bajo.\n"
            "Selecciona las columnas 'nombre', 'apellido' y 'salario' de la tabla 'empleados'.\n"
            "Consejo: Usa una subconsulta en la cláusula WHERE que calcule el valor mínimo ('min(salario)')\n"
            "para filtrarlo."
        )
        query_maestro = """
            SELECT nombre, apellido, salario 
            FROM empleados 
            WHERE salario = (SELECT min(salario) FROM empleados)
        """
        
    # Bucle
    intentos = 3
    print("\n")
    print(" <> Servidor OMNICORP <> ")
    print("\n")
    print(enunciado)
    print("Tablas: 'empleados' (id_emp, nombre, apellido, rol, id_dep, salario)\n")
    
    while intentos > 0:
        query_jugador = input(f"[{intentos} intentos restantes] SQL_SHELL> ")
        
        if validar_consulta(conn, query_jugador, query_maestro):
            print("\n[SISTEMA]: Subconsulta resuelta con éxito.")
            print("Agente: Las credenciales del objetivo han sido clonadas. Acceso total al mainframe.\n")
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print("[SISTEMA - ALERTA]: Error en la estructura anidada.\n Recuerda encerrar la subconsulta completamente entre paréntesis ().")
            else:
                print("\n[SISTEMA - ALARMA]: Bloqueo criptográfico activado. Terminal bloqueada.")
                return False

# Mision 12
def jugar_mision_12(conn):
    sabotaje_azar = random.choice(['BORRAR_LOGS', 'ALTERAR_CREDENCIALES'])
    
    if sabotaje_azar == 'BORRAR_LOGS':
        enunciado = (
            "Con esto estaremos borrando las huellas de la intrusión.\n"
            "Las alarmas están sonando. Necesitamos eliminar inmediatamente todos los registros\n"
            "de la tabla 'registros_de_red' cuya 'criticidad' sea 'ALTA' para limpiar tu rastro.\n"
            "Usa el comando DML correcto para purgar estas filas del servidor."
        )
        query_maestro = "DELETE FROM registros_de_red WHERE criticidad = 'ALTA'"
    else:
        enunciado = (
            "Debemos bloquear a los administradores.\n"
            "Para asegurar tu escape, debes alterar los hashes de acceso de la tabla 'terminales_bloqueadas'.\n"
            "Modifica la columna 'hash_seguridad' para que su valor sea 'BLOQUEADO'.\n"
            "Aplica este cambio ÚNICAMENTE para el registro cuyo 'id_bloqueo' sea igual a 1."
        )
        query_maestro = "UPDATE terminales_bloqueadas SET hash_seguridad = 'BLOQUEADO' WHERE id_bloqueo = 1"
        
    intentos = 3
    print("\n<><><><><><><><><><><><><><><><><><>")
    print(" CONEXIÓN: Servidor General OMNICORP ")
    print("<><><><><><><><><><><><><><><><><><>")
    print(enunciado)
    print("\n[INFO]: Esta operación modificará los datos reales de la sesión en memoria.\n")
    
    while intentos > 0:
        query_jugador = input(f"[{intentos} intentos restantes] SQL_SHELL> ")
        
        # Validación previa opcional para advertir al jugador
        if query_jugador.strip().lower().startswith("select"):
            print("\n[ALERTA]: Las consultas de selección no alteran el sistema.")
            intentos -= 1
            continue
            
        # Toda la captura de errores SQL y la validación ocurren dentro de esta función
        if validar_consulta(conn, query_jugador, query_maestro):
            print("\n[SISTEMA]: Parámetros de red alterados.")
            print("Agente: Efectuando COMMIT definitivo... Huellas borradas. Conexión cerrada con éxito.\n")
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print("[SISTEMA - ALERTA]: El comando no afectó las filas correctas o tiene un error de filtro.")
            else:
                print("\n[ADMINISTRADOR OMNICORP]: Fallaste, tu retraso le permitió al antivirus aislar tu conexión. Fin del juego.")
                return False
# Fin de las misiones

# Iniciamos el que arranca el juego

if __name__ == "__main__":
    conexion = inicializar_bd()
    
    print("==================================================")
    print("   BIENVENIDO A SPYQL - Proyecto para ayudar el estudio SQL     ")
    print("===================ZONEJACK=======================")
    print("\nEncarnas un agente infiltrandose en la Base de Datos de Omnicorp, compañia malvada.")
    
    # Lista con todas las funciones de tus misiones en orden
    misiones = [
        jugar_mision_1, jugar_mision_2, jugar_mision_3, jugar_mision_4,
        jugar_mision_5, jugar_mision_6, jugar_mision_7, jugar_mision_8,
        jugar_mision_9, jugar_mision_10, jugar_mision_11, jugar_mision_12
    ]
    
    hackeo_exitoso = True
    
    # Recorremos cada misión de forma limpia y plana - aporte de Gemini
    for i, mision in enumerate(misiones, start=1):
        if not mision(conexion):
            hackeo_exitoso = False
            break  # Si falla una misión, se aborta el juego inmediatamente
            
    if hackeo_exitoso:
        print("==================================================")
        print("  ¡MISIÓN CUMPLIDA, AGENTE DE SQL!      ")
        print(" Hackeo exitoso. OmniCorp neutralizado.           ")
        print("==================================================")
