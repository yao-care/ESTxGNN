---
layout: default
title: Saquinavir
parent: Solo predicción del modelo (L5)
nav_order: 484
evidence_level: L5
indication_count: 6
---

# Saquinavir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Saquinavir: De Infección por VIH-1 a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Saquinavir es un inhibidor de la proteasa del VIH-1, comercializado en España para el tratamiento de la infección por VIH-1 (el registro de la AEMPS no incluye el texto de la indicación, por lo que este dato se deduce de la clase del fármaco).
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina (FIV)**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción concreta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 (deducida de la clase del fármaco) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Saquinavir inhibe la proteasa aspártica del VIH-1. Con ello bloquea el corte de la poliproteína Gag-Pol y produce viriones inmaduros, no infecciosos. Actualmente no se dispone de datos detallados de mecanismo de acción en DrugBank, así que esta descripción proviene de la clase farmacológica conocida.

El VIH-1 y el virus de la inmunodeficiencia felina (FIV) son ambos lentivirus, y esta cercanía probablemente explica el puntaje alto del modelo. Sin embargo, la proteasa del FIV difiere de la del VIH-1 en su especificidad de sustrato. Por eso la inhibición cruzada por saquinavir es incierta y no está respaldada por los datos disponibles.

El puntaje de 99.97% refleja más bien la proximidad en el grafo de conocimiento con otras enfermedades lentivirales que una actividad validada. Además, el síndrome de inmunodeficiencia felina es una enfermedad veterinaria, no una indicación clínica humana.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 96026002 | INVIRASE 500 mg comprimidos recubiertos con película | Comprimido recubierto con película | Roche Registration GmbH |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del grafo de conocimiento (nivel L5), sin ensayos ni publicaciones. Además, la eficacia de saquinavir sobre la proteasa del FIV es incierta y la indicación es veterinaria.

**Para avanzar se necesita:**
- Ensayos in vitro de susceptibilidad de la proteasa del FIV a saquinavir.
- Confirmar si existe un interés veterinario real, ya que no es una indicación humana.
- Obtener el texto de indicaciones y el prospecto de la AEMPS, con advertencias y contraindicaciones.
- Completar los datos de mecanismo de acción desde DrugBank.

**Nota sobre otras predicciones del mismo paquete:** el resultado con mayor respaldo es "complejo relacionado con el SIDA" (L1, Proceed with Guardrails). Se trata en la práctica de un uso ya autorizado para el VIH, no de un reposicionamiento real. "Infección por VIH congénito" alcanza L2 con evidencia pediátrica limitada. "Infección por virus de inmunodeficiencia simia" solo tiene evidencia preclínica (L4), útil para el diseño de modelos animales.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

