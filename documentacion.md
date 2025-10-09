# Tienda Aurelion

## Tema

Tienda Aurelion es una cadena de mercado con varias sedes a lo largo de Cordoba. Dentro de su catalogo ofrece biene de consumo tales como alimentos varios y articulos de limpieza.

## Problema

- Control de productos mas vendidos y productos menos vendidos (Para optimizar el stock de los mismos)
- Hacer combos de productos mas vendidos (descuentos, promociones)
- Ver que medio de pago es mas utilizado para plantear descuentos o sumar postnets nuevos (falta de postnets)
- Ver si hay fraude/perdida en las ventas y cuanto es el % de la misma
- Analisis de clientes por cantidad de gastos/zona/etc para ofrecerles promociones (Tipo tiers de beneficios)

## Solucion

## Datos Requeridos

Los datos fueron provistos por los duenios de la tienda Aurelion

### Detalle_venta

- id_venta
  - Tipo cualitativo
  - Ordinal
- id_producto
  - Tipo cualitativo
  - Ordinal
- nombre_producto
  - Tipo cualitativo
  - Nominal
- cantidad
  - Tipo cuantitativo
  - Razon
- precio_unitario
  - Tipo cuantitativo
  - Razon
- importe
  - Tipo cuantitativo
  - Razon

### Clientes

- id_cliente
  - Tipo cualitativo
  - Ordinal
- nombre_cliente
  - Tipo cualitativo
  - Nominal
- email
  - Tipo cualitativo
  - Nominal
- ciudad
  - Tipo cualitativo
  - Nominal
- fecha_alta
  - Tipo cuantitativo
  - Intervalo

### Ventas

- id_venta
  - Tipo cualitativo
  - Nominal
- id_cliente
  - Tipo cualitativo
  - Nominal
- nombre_cliente
  - Tipo cualitativo
  - Nominal
- fecha
  - Tipo cuantitativo
  - Intervalo
- email
  - Tipo cualitativo
  - Nominal
- medio_pago
  - Tipo cualitativo
  - Nominal

### Productos

- id_producto
- nombre_producto
- categoria
- precio_unitario

## Pseudocodigo

## Diagrama
