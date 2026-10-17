# ==============================================================================
# SISTEMA DE DISPOSITIVOS BIOMÉDICOS
# Descripción: Sistema para la gestión, control de parámetros de seguridad eléctrica
# y asistencia motora mediante un guante robótico basado en señales EMG para
# rehabilitación física post-EVC.
# ==============================================================================

# Creación de la clase base
class DispositivoBiomedico:
    """Clase principal que representa un equipo médico general."""
    def __init__(self, id_equipo: str, nombre: str, voltaje_operacion: float):
        self.id_equipo = id_equipo
        self.nombre = nombre
        # Aplicación de Encapsulamiento (atributo privado con __)
        self.__voltaje_operacion = 0.0
        self.set_voltaje_operacion(voltaje_operacion)
        # Atributo protegido con _
        self._encendido = False

    # Aplicación de Encapsulamiento (Getters y Setters con validación)
    def get_voltaje_operacion(self) -> float:
        """Getter para consultar el voltaje de forma segura."""
        return self.__voltaje_operacion

    def set_voltaje_operacion(self, nuevo_voltaje: float) -> None:
        """Setter con validación: no permite voltajes negativos o nulos."""
        if nuevo_voltaje > 0:
            self.__voltaje_operacion = float(nuevo_voltaje)
        else:
            print(f"[ERROR] Voltaje inválido: {nuevo_voltaje}V. Debe ser mayor a 0.")

    # Métodos operativos
    def encender(self) -> str:
        self._encendido = True
        return f"El dispositivo {self.nombre} (ID: {self.id_equipo}) ha sido ENCENDIDO a {self.__voltaje_operacion}V."

    def apagar(self) -> str:
        self._encendido = False
        return f"El dispositivo {self.nombre} (ID: {self.id_equipo}) ha sido APAGADO."

    def describir(self) -> str:
        estado = "Encendido" if self._encendido else "Apagado"
        return f"Dispositivo: {self.nombre} | ID: {self.id_equipo} | Estado: {estado} | Voltaje: {self.__voltaje_operacion}V"


# Uso de super() y Herencia
class GuanteRehabilitacion(DispositivoBiomedico):
    """Subclase especializada en un guante robótico de asistencia EMG."""
    def __init__(self, id_equipo: str, nombre: str, voltaje_operacion: float, umbral_emg_mv: float, dedos_activos: int):
        # Llamada al constructor de la clase padre
        super().__init__(id_equipo, nombre, voltaje_operacion)
        # Dos atributos nuevos propios de la subclase
        self.umbral_emg_mv = float(umbral_emg_mv)
        self.dedos_activos = int(dedos_activos)
        self._asistencia_activa = False

    # Método operativo propio de la subclase
    def procesar_senal_emg(self, valor_medido_mv: float) -> str:
        if not self._encendido:
            return f"[ALERTA] Enciende primero el guante {self.nombre} para procesar EMG."
        
        if valor_medido_mv >= self.umbral_emg_mv:
            self._asistencia_activa = True
            return f"[EMG DETECTADO: {valor_medido_mv} mV] Supera umbral ({self.umbral_emg_mv} mV). Activando {self.dedos_activos} servomotores."
        else:
            self._asistencia_activa = False
            return f"[EMG DÉBIL: {valor_medido_mv} mV] Debajo del umbral. Sistema en reposo."

    # Sobrescritura de métodos (Polimorfismo)
    def describir(self) -> str:
        estado = "Encendido" if self._encendido else "Apagado"
        asistencia = "Activa" if self._asistencia_activa else "En reposo"
        return f"Guante EMG: {self.nombre} | ID: {self.id_equipo} | Estado: {estado} | Asistencia: {asistencia} | Umbral: {self.umbral_emg_mv} mV | Dedos: {self.dedos_activos}"


# Instanciación y pruebas
if __name__ == "__main__":
    print("--- 1. Instanciación de 3 objetos ---")
    equipo_base = DispositivoBiomedico("BIO-01", "Monitor de Signos", 12.0)
    guante_der = GuanteRehabilitacion("GNT-R", "Guante Mano Derecha", 5.0, 150.0, 2)
    guante_izq = GuanteRehabilitacion("GNT-L", "Guante Mano Izquierda", 5.0, 180.0, 5)

    print("\n--- 2. Pruebas de Encapsulamiento ---")
    print(f"Voltaje inicial: {guante_der.get_voltaje_operacion()}V")
    guante_der.set_voltaje_operacion(-4.0)  # Intento inválido
    guante_der.set_voltaje_operacion(5.5)   # Cambio válido
    print(f"Voltaje actualizado: {guante_der.get_voltaje_operacion()}V")

    print("\n--- 3. Pruebas de Herencia y Operación ---")
    print(equipo_base.encender())
    print(guante_der.encender())

    print("\n--- 4. Pruebas de Polimorfismo (describir) ---")
    print(equipo_base.describir())
    print(guante_der.describir())

    print("\n--- 5. Método de la subclase (Señales EMG) ---")
    print(guante_der.procesar_senal_emg(80.0))   # No activa
    print(guante_der.procesar_senal_emg(200.0))  # Sí activa

    print("\n--- 6. Independencia de instancias ---")
    print(f"Objeto 2: {guante_der.nombre} -> Dedos: {guante_der.dedos_activos}")
    print(f"Objeto 3: {guante_izq.nombre} -> Dedos: {guante_izq.dedos_activos}")

