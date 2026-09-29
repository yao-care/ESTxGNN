---
layout: default
title: Brinzolamide
parent: Solo predicción del modelo (L5)
nav_order: 80
evidence_level: L5
indication_count: 1
---

# Brinzolamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Brinzolamida: De Hipertensión Ocular y Glaucoma de Ángulo Abierto a Glaucoma Hereditario Primario

## Resumen en Una Frase

Brinzolamida es un inhibidor de la anhidrasa carbónica que se usa en colirio para reducir la presión intraocular elevada en hipertensión ocular y glaucoma de ángulo abierto.
El modelo TxGNN predice que podría ser efectivo para **glaucoma hereditario primario**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
Es probable que la predicción sea una redetección de su uso ya conocido y no una reposición genuina.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Presión intraocular elevada en hipertensión ocular o glaucoma de ángulo abierto (según la información farmacológica; los textos de indicación de las autorizaciones AEMPS vienen vacíos) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99,48 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la información farmacológica disponible, brinzolamida se une a las anhidrasas carbónicas humanas CA1, CA7, CA12 y CA14. El paquete de datos no incluye una descripción detallada del mecanismo de acción. Por conocimiento farmacológico general, que no se verificó con los datos suministrados, su diana principal es la anhidrasa carbónica II. Su inhibición reduce la secreción de humor acuoso y, con ello, la presión intraocular.

Como el glaucoma se caracteriza por presión intraocular elevada, existe plausibilidad biológica para cualquier subtipo. Sin embargo, el puntaje tan alto (0,995) probablemente refleja que el modelo redescubrió el uso ya conocido del fármaco en glaucoma. Si es así, no constituye una señal real de reposicionamiento.

El subtipo específico "glaucoma hereditario primario" no está respaldado por evidencia propia. No se aportó ningún ensayo ni publicación específica de este subtipo. La similitud con la indicación original está pendiente de evaluar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 80098 | Brinzolamida Cinfa 10 mg/ml colirio en suspensión | Colirio en suspensión | No disponible en los datos |
| 79856 | Brinzolamida Stada 10 mg/ml colirio en suspensión | Colirio en suspensión | No disponible en los datos |
| 80014 | Brinzolamida Vir 10 mg/ml colirio en suspensión | Colirio en suspensión | No disponible en los datos |
| 00129001 | Azopt 10 mg/ml colirio en suspensión | Colirio en suspensión | No disponible en los datos |
| 90850 | Aicisi 10 mg/ml colirio en suspensión | Colirio en suspensión | No disponible en los datos |

Se muestran 5 de las 6 autorizaciones registradas.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Las 4 entradas de "interacciones" del paquete corresponden a dianas farmacológicas (CA1, CA7, CA12 y CA14), no a interacciones con otros medicamentos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura. El puntaje alto probablemente refleja la indicación ya conocida en glaucoma, no un uso nuevo. Además, faltan los datos de seguridad del prospecto de la AEMPS.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones) y confirmar la indicación autorizada frente a la predicha.
- Verificar si "glaucoma hereditario primario" aporta algo distinto de la indicación ya aprobada.
- Buscar evidencia específica del subtipo (ensayos, series de casos, literatura).
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar la seguridad, incluidas las interacciones con otros fármacos, una vez disponibles los datos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

