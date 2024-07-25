Lógica de Alertas de Compra y Venta
Definir Umbrales: Establece umbrales de porcentaje para las alertas de compra y venta. Por ejemplo, alertas de compra cuando el precio baja un 1%, 2%, 3%, etc., y alertas de venta cuando sube un 1%, 2%, 3%, etc.

Estado Inicial: Guarda el precio inicial cuando el bot comienza a monitorear.

Monitoreo Continuo: Verifica periódicamente el precio actual y calcula el cambio porcentual desde el precio inicial.

Generar Alertas: Basado en el cambio porcentual, genera alertas correspondientes para compra o venta.

Mejora de la Lógica de Alertas para Velas Alcistas y Bajistas

Objetivo

Detectar patrones de velas alcistas y bajistas para generar alertas más precisas de compra y venta.
Conceptos Clave

- Velas Alcistas y Bajistas: Utilizar datos de OHLC (Open, High, Low, Close) para identificar velas alcistas (precio de cierre > precio de apertura) y bajistas (precio de cierre < precio de apertura).
- Volumen de Transacciones: Considerar el volumen de transacciones para validar la fuerza de las velas.
- Promedios Móviles: Usar promedios móviles para suavizar las fluctuaciones de precios y detectar tendencias.

Estrategia
- Obtener Datos de OHLC: Utiliza una API que proporcione datos de OHLC y volumen.
- Analizar Patrones: Implementa lógica para identificar patrones de velas alcistas y bajistas.
- Generar Alertas: Basado en los patrones identificados y el volumen de transacciones, genera alertas de compra y venta.

------- ACTUALIZACIÓN DE LA INFO -----------

Inicio del Monitoreo: El precio inicial hace 4 horas era $64063.

Precios en Intervenciones Clave:

Hace 3:45 horas: $64272 (1% abajo del precio actual)
Hace 3:30 horas: $64620 (0.5% abajo del precio actual)
Precio actual: $64960
Fluctuación Anterior: Entre $64060 y $64480 durante 14 horas antes del incremento.

Condiciones para Alerta:

Si el precio baja más del 0.5% en media hora, enviar una alerta.
Lógica para Generar Alertas

Monitorear el Precio Inicial:

Guardar el precio inicial cada vez que comienza el monitoreo.
Por ejemplo, cada hora se guarda el precio actual.

Calcular Cambios Porcentuales:

Comparar el precio actual con el precio de hace media hora.
Si el precio ha bajado más del 0.5% en media hora, enviar una alerta de compra.
Generar Alertas Basadas en Patrón de Precios:

Mantener un registro de los precios históricos y compararlos para detectar tendencias de subida o bajada.
Ejemplo Detallado para Explicación

Precios y Cambios
Hace 4:00 horas:
Precio: $64063
1.5% abajo del precio actual.

Hace 3:45 horas:
Precio: $64272
1% abajo del precio actual.

Hace 3:30 horas:
Precio: $64620
0.5% abajo del precio actual.

Precio Actual:
Precio: $64960
Ha subido un 1.55% desde el precio inicial de hace 4 horas.

Generación de Alerta
Evaluación de la Bajada:
Si el precio baja más del 0.5% en media hora.
Por ejemplo, si el precio baja de $64960 a menos de $64620 en media hora.

Momento de la Alerta de Compra:
Al inicio de la subida sostenida, cuando el precio alcanzó $64272 hace 3:45 horas, una alerta de compra podría haberse generado.
El precio estuvo estable entre $64060 y $64480 durante 14 horas antes de la subida, indicando una buena oportunidad de compra al inicio de la subida.

1- Monitoreo Inicial:

Comenzamos monitoreando el precio de Bitcoin cada 30 minutos.
Guardamos los precios históricos con marca de tiempo.

2- Detectar Cambios Porcentuales:
Calculamos el cambio porcentual del precio en los últimos 30 minutos.
Si el precio ha bajado más del 0.5%, generamos una alerta de compra.

3- Momento Ideal para Compra:
Al inicio de una subida sostenida (cuando el precio estaba estable entre $64060 y $64480), una alerta de compra puede ayudar al usuario a aprovechar la subida.
Este comportamiento es importante para ayudar al usuario a tomar decisiones informadas y maximizar ganancias.

4- Automatización:
El sistema revisa los precios cada 30 minutos y genera alertas automáticamente basado en cambios porcentuales.
Esto asegura que el usuario reciba notificaciones oportunas y relevantes.
