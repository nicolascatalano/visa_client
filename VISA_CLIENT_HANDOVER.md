# visa_client.py - Descripcion funcional y uso

## Que hace este script
El archivo [visa_client/visa_client.py](visa_client/visa_client.py) es un cliente TCP simple para controlar un instrumento remoto (tipo generador RF) por comandos estilo SCPI.

El script se conecta al equipo en:
- Host: `192.168.0.30`
- Puerto: `5000`

Luego envia una secuencia fija de comandos para dejar el instrumento en un estado conocido y listo para emision RF.

## Flujo de ejecucion
Al ejecutar el script, se hacen varias conexiones TCP cortas (una por comando) en este orden:

1. `Q:*RST`
   - Resetea el instrumento.
2. `Q:*IDN?`
   - Consulta identificacion del equipo e imprime la respuesta.
3. `Q:MOD:STATE OFF`
   - Deshabilita modulacion.
4. `Q:FREQ:CW 436.51 MHz`
   - Configura frecuencia CW en 436.51 MHz.
5. `Q:AMPLITUDE:CW -60 dBm`
   - Configura amplitud de salida en -60 dBm.
6. `Q:SYST:REF:FREQ EXT10MHZ`
   - Selecciona referencia externa de 10 MHz.
7. `Q:RFOutput:STATE ON`
   - Habilita salida RF.
8. `Q:SYST:REF:FREQ?`
   - Consulta referencia activa e imprime la respuesta.

## Como usarlo

### Requisitos
- Python 3.x
- Conectividad IP al instrumento (`192.168.0.30:5000`)
- Instrumento compatible con los comandos usados

### Ejecucion
Desde la raiz del repo:

```powershell
python visa_client/visa_client.py
```

Si estas usando el entorno virtual del proyecto:

```powershell
(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& .venv\Scripts\Activate.ps1)
python visa_client/visa_client.py
```

### Salida esperada
En consola se imprimen dos respuestas del instrumento:
- Respuesta a `*IDN?` (modelo/firmware)
- Respuesta a `SYST:REF:FREQ?` (estado de referencia)

## Notas tecnicas
- El script no tiene manejo de errores (timeouts, equipo no disponible, comando invalido).
- Abre una conexion TCP nueva por cada comando. Es simple y robusto para pruebas rapidas, pero menos eficiente que mantener una sola sesion.
- El prefijo `Q:` forma parte del protocolo esperado por el servidor del instrumento en este entorno.

## Recomendaciones de mejora (opcional)
- Agregar `try/except` y `socket.settimeout(...)`.
- Reutilizar una sola conexion para toda la secuencia.
- Parametrizar host, puerto, frecuencia y amplitud por argumentos de linea de comandos.
- Agregar validacion de respuestas `?` y logging.
