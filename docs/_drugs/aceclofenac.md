---
layout: default
title: Aceclofenac
parent: Solo predicción del modelo (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Aceclofenac
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

# Aceclofenaco: De Dolor e Inflamación Musculoesquelética a Síndrome de Braquiolmia-Amelogénesis Imperfecta

## Resumen en Una Frase

Aceclofenaco es un antiinflamatorio no esteroideo (AINE) utilizado originalmente para el dolor y la inflamación de trastornos musculoesqueléticos, como la artrosis, la artritis reumatoide y la espondilitis anquilosante.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de braquiolmia-amelogénesis imperfecta**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en las fichas de AEMPS recibidas; según la literatura, dolor e inflamación musculoesquelética (artrosis, artritis reumatoide, espondilitis anquilosante) |
| Nueva Indicación Predicha | Síndrome de braquiolmia-amelogénesis imperfecta |
| Puntaje de Predicción TxGNN | 99,89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 16 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, aceclofenaco es un AINE de la familia de los derivados del ácido fenilacético, con actividad inhibidora de la ciclooxigenasa (COX). Reduce la inflamación y el dolor mediados por prostaglandinas.

La nueva indicación es un trastorno genético que afecta al esqueleto y a los dientes. No se identifica ninguna vía plausible por la cual inhibir la COX pudiera modificar la enfermedad.

El puntaje tan alto del modelo (99,89%) parece un artefacto de la predicción sobre el grafo de conocimiento. No lo respalda ningún ensayo ni publicación. En este caso, la razonabilidad mecanística es **baja**.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 16 autorizaciones. El Evidence Pack no incluye el texto de indicación aprobada para ninguna de ellas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 70982 | Aceclofenaco Aurovitas Spain 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 69551 | Aracenac 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 79696 | Aceclofenaco Stada 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 69552 | Aceclofenaco Arafarma Group 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 67487 | Aceclofenaco Kern Pharma 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

Las formas farmacéuticas registradas también incluyen comprimido recubierto, polvo para suspensión oral y crema.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni publicaciones. Además, no existe un mecanismo plausible que vincule la inhibición de la COX con esta enfermedad genética esquelética y dental.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Descarga y análisis del prospecto de AEMPS (advertencias y contraindicaciones), imprescindible antes del cribado de seguridad.
- Cualquier evidencia preclínica o clínica específica de aceclofenaco en esta enfermedad. Sin ella, no se recomienda continuar.

**Nota sobre otras predicciones del paquete:** de las 10 indicaciones predichas, solo la **espinopatía inflamatoria** (puesto 8, puntaje 99,63%) tiene evidencia directa. Incluye dos ensayos controlados en espondilitis anquilosante (PMID 8823693 y 8823692, ambos de 1996), y su nivel es L2 con recomendación "Proceed with Guardrails". Es probable que sea un uso ya coherente con la ficha técnica y no un reposicionamiento real. Se sugiere evaluarla por separado, con vigilancia de riesgos gastrointestinales, cardiovasculares y renales propios de los AINE.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

