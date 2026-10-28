---
layout: default
title: Remimazolam
parent: Solo predicción del modelo (L5)
nav_order: 692
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Remimazolam: nueva indicación predicha, Insomnio (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de la a…"
monitor_inn: "REMIMAZOLAM"
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium"]
---

# Remimazolam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Remimazolam: De Indicación Original No Especificada a Insomnio
{: .text-alpha }

## Resumen en Una Frase

Remimazolam es una benzodiazepina de acción ultracorta administrada por vía intravenosa, autorizada y comercializada en España (Byfavo), aunque los datos compilados no recogen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **insomnio** (puntaje 0,9991), y como segunda predicción para el **delirium por abstinencia alcohólica** (0,9930).
Actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden estas predicciones, por lo que se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 0,9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Autorizado pero no comercializado (registros: 1) |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, remimazolam es una benzodiazepina de acción ultracorta que actúa como modulador alostérico positivo de los receptores GABA-A, con efecto sedante e hipnótico. Este mecanismo es compartido con hipnóticos establecidos (benzodiazepinas y fármacos "Z") usados en el insomnio, por lo que un beneficio es biológicamente plausible.

Sin embargo, esta relación se infiere de la clase farmacológica y no de datos aportados. Remimazolam se formula como agente intravenoso para sedación procedimental y anestesia general, y su inicio y finalización de efecto muy rápidos (metabolismo por esterasas tisulares) se adaptan al uso procedimental más que al mantenimiento del sueño que requiere el insomnio crónico. Tampoco hay una formulación oral en los datos. El puntaje tan alto de TxGNN probablemente refleja la similitud de clase con otros hipnóticos GABAérgicos.

Para la segunda predicción, el delirium por abstinencia alcohólica, la lógica es similar: la pérdida de inhibición GABAérgica tras el cese del alcohol se trata de primera línea con benzodiazepinas. Su vida media corta y su fácil titulación podrían ofrecer ventajas teóricas en UCI, pero podría requerir infusión continua y provocar síntomas de rebote. No hay datos sobre este uso.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1201505001 | BYFAVO 20 MG POLVO PARA SOLUCIÓN INYECTABLE (Paion Pharma GmbH) | Polvo para solución inyectable | No especificada en los datos compilados |

---

## Consideraciones de Seguridad

**Interacciones farmacológicas** (54 interacciones registradas; se muestran las de mayor relevancia):

- **Gravedad mayor:** morfina, morfina liposomal, codeína e hidrocodona (opioides; riesgo de depresión respiratoria y sedación profunda aditiva).
- **Gravedad moderada:** bupropión, dronabinol, nabilona, metoclopramida, opio, sibutramina, etanol, diazóxido, fentolamina, prometazina, disulfiram, lidocaína, clorfeniramina, cetirizina, azelastina nasal y dextrometorfano.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ambas indicaciones predichas se sustentan solo en el modelo (nivel L5), sin ensayos ni literatura. Además, el perfil farmacocinético y la vía intravenosa de remimazolam no encajan bien con el insomnio crónico.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), que es un bloqueo para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda sistemática de ensayos clínicos y literatura para insomnio y delirium por abstinencia alcohólica.
- Evaluar la compatibilidad de vía de administración (no hay formulación oral) y de perfil farmacocinético con cada indicación.
- Valorar con mayor prioridad el uso en abstinencia alcohólica en UCI, donde la vía intravenosa es compatible, y analizar el riesgo de interacción con opioides y alcohol.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

