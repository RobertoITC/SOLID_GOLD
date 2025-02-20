# Sistema de Gestión y Ejemplos SOLID

## 📋 Descripción
Este repositorio contiene ejemplos prácticos de implementación de los principios SOLID en diferentes contextos empresariales. Cada ejemplo está diseñado para demostrar cómo los principios SOLID pueden mejorar la mantenibilidad, flexibilidad y escalabilidad del código.

## 🎯 Ejemplos Incluidos

### 1. Gestión de Notificaciones

[Espacio para imagen de Figma]

**Descripción:** Sistema que permite enviar notificaciones por diferentes medios (correo electrónico y SMS) sin acoplarse a una implementación específica.

**Principios SOLID aplicados:**
- **SRP**: Cada clase tiene una única responsabilidad (Notificación y Servicio de Notificación)
- **DIP**: El servicio depende de una abstracción (`Notification`) y no de clases concretas

**Beneficio:** Facilita la adición de nuevos tipos de notificación sin modificar el servicio principal.

### 2. Sistema de Pagos

[Espacio para imagen de Figma]

**Descripción:** Sistema de pagos desacoplado que soporta múltiples métodos de pago.

**Principios SOLID aplicados:**
- **DIP**: `PaymentSystem` depende de `Payment` en lugar de implementaciones específicas
- **SRP**: Cada componente maneja su propia lógica de procesamiento

### 3. Gestión de Envíos y Seguimiento

[Espacio para imagen de Figma]

**Descripción:** Sistema para gestión logística con diferentes roles y responsabilidades.

**Principio SOLID principal:**
- **ISP**: Interfaces específicas para cada rol:
 - `Trackable`: Seguimiento de paquetes
 - `Deliverable`: Manejo de entregas
 - `Routable`: Optimización de rutas

### 4. Calculadora de Descuentos

[Espacio para imagen de Figma]

**Descripción:** Sistema de descuentos extensible.

**Principios SOLID aplicados:**
- **OCP**: Permite añadir nuevos tipos de descuento sin modificar código existente
- **SRP**: Separación clara de responsabilidades en el procesamiento de pagos

### 5. Sistema de Vehículos

[Espacio para imagen de Figma]

**Descripción:** Sistema de transporte genérico que soporta diferentes tipos de vehículos.

**Principios SOLID aplicados:**
- **LSP**: Sustitución transparente de tipos de vehículos
- **DIP**: Dependencia de abstracciones para mayor flexibilidad

🗒️[Link del Figma](https://www.figma.com/design/p2FKkjb88WxlCv3OSQy3zr/SOLID?node-id=0-1&t=a4ByNnH5YT2MHJi3-1)
