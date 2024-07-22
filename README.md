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