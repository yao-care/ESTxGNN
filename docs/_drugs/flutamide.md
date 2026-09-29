---
layout: default
title: Flutamide
parent: Solo predicción del modelo (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
---

# Flutamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Flutamida: De Cáncer de Próstata a Susceptibilidad a Cáncer de Próstata/Cáncer Cerebral

## Resumen en Una Frase

Flutamida es un antiandrógeno no esteroideo cuyo uso clínico conocido es el tratamiento del cáncer de próstata metastásico o localmente avanzado (dato de farmacología; el registro AEMPS del pack no incluye texto de indicación).
El modelo TxGNN predice que podría ser efectiva para **susceptibilidad a cáncer de próstata/cáncer cerebral**, con un puntaje muy alto pero **sin ensayos clínicos ni publicaciones** que respalden esta entrada concreta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de próstata (según farmacología; los textos de indicación de las autorizaciones AEMPS están vacíos) |
| Nueva Indicación Predicha | Susceptibilidad a cáncer de próstata/cáncer cerebral |
| Puntaje de Predicción TxGNN | 99,98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro del fármaco. Según la información de farmacología disponible, flutamida actúa sobre el **receptor de andrógenos (AR)**. Se usa en cáncer de próstata, y mecanísticamente podría ser aplicable a esta nueva entrada.

El componente "cáncer de próstata" de la predicción es plausible: bloquear el receptor de andrógenos es el mecanismo establecido en tumores prostáticos dependientes de andrógenos. Sin embargo, la etiqueta predicha es una **categoría compuesta de susceptibilidad** (próstata/cerebro). No tiene ensayos ni literatura asociados, y no se identificó un vínculo mecanístico para el componente cerebral.

El puntaje TxGNN es muy alto, pero es solo una predicción del modelo. Sin evidencia real vinculada, no debe interpretarse como respaldo clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 59594 | GRISETIN 250 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | Faes Farma S.A. |
| 59593 | PROSTACUR COMPRIMIDOS | Comprimido | Mylan Pharmaceuticals S.L. |
| 62912 | FLUTAMIDA CINFA 250 mg COMPRIMIDOS EFG | Comprimido | Laboratorios Cinfa S.A. |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (antiandrógeno), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función hepática (advertencia de hepatotoxicidad grave) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Advertencias Principales**: el análisis de las indicaciones predichas señala una advertencia de hepatotoxicidad (recuadro de advertencia) que exige monitorizar la función hepática.
- **Interacciones Farmacológicas**: la consulta se completó con 1 registro, pero corresponde a la diana farmacológica (receptor de andrógenos, gen AR), no a una interacción con otro fármaco. No hay interacciones fármaco-fármaco clínicas listadas.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Esta entrada es solo una predicción del modelo (L5): no tiene ensayos ni literatura, y el componente cerebral carece de fundamento mecanístico. La hepatotoxicidad de flutamida hace que la relación beneficio-riesgo sea difícil de justificar sin evidencia.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que es un vacío bloqueante para el cribado de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Aclarar qué enfermedad concreta representa la etiqueta compuesta "susceptibilidad a cáncer de próstata/cáncer cerebral".
- Como referencia, otras predicciones del mismo fármaco tienen más respaldo. "Cáncer de órgano reproductor masculino" (L2) es esencialmente la indicación nativa, con un ensayo de Fase 2 aleatorizado que incluye flutamida (NCT00450463). "Neoplasia benigna del sistema reproductor" (L3) tiene datos humanos limitados en hiperplasia prostática benigna. Ambas merecen evaluación por separado.

*Los resultados son solo de referencia para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

