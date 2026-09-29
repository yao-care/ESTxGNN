---
layout: default
title: Finasteride
parent: Solo predicción del modelo (L5)
nav_order: 233
evidence_level: L5
indication_count: 6
---

# Finasteride
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

# Finasterida: De Hiperplasia Prostática Benigna a Hipertricosis Universal Congénita Tipo Ambras

## Resumen en Una Frase

Finasterida es un inhibidor de la 5-alfa reductasa tipo 2 (SRD5A2), usado en la hiperplasia prostática benigna según la base de datos farmacológica consultada.
El modelo TxGNN predice que podría ser efectiva para la **hipertricosis universal congénita tipo Ambras**, pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
La predicción se apoya solo en el modelo y no tiene evidencia real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperplasia prostática benigna (los textos de indicación de las autorizaciones españolas están vacíos; dato tomado de la ficha farmacológica del objetivo SRD5A2) |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No hay un dato de mecanismo de acción (MOA) en el registro del fármaco. Sí consta que finasterida actúa sobre la 5-alfa reductasa tipo 2 (gen *SRD5A2*). Esta enzima convierte la testosterona en dihidrotestosterona (DHT), por lo que el fármaco reduce los niveles de DHT.

La relación con la nueva indicación es débil. El síndrome de Ambras es un trastorno congénito raro, asociado a reordenamientos genómicos que afectan la regulación de *TRPS1*, y no a la señalización androgénica. Inhibir la 5-alfa reductasa no tiene una justificación biológica clara para esta enfermedad. La puntuación alta parece reflejar la cercanía en el grafo de conocimiento entre finasterida y las enfermedades del crecimiento del vello, más que un vínculo mecanístico demostrado.

Por eso la predicción debe tratarse como una hipótesis del modelo, sin respaldo clínico ni de literatura.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Hay 20 autorizaciones en total. Se muestran las 5 principales. Las formas farmacéuticas registradas incluyen comprimidos recubiertos con película y una solución para pulverización cutánea.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 71064 | Finasterida Normon 1 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorios Normon S.A. |
| 68168 | Finasterida Tecnigen 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Tecnimede España Industria Farmacéutica S.A. |
| 76704 | Finasterida Cinfa 1 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorios Cinfa S.A. |
| 74134 | Capikern 1 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Kern Pharma S.L. |
| 68042 | Finasterida Benel 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Farmalider S.A. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura. Además, el mecanismo conocido de finasterida (bloqueo de la vía androgénica) no se relaciona de forma plausible con el síndrome de Ambras. Las otras cinco indicaciones predichas tampoco tienen evidencia directa. La hipertricosis general (puesto 2) solo cuenta con revisiones narrativas antiguas que no muestran eficacia de finasterida, y la hipertricosis es por definición independiente de andrógenos.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS para completar advertencias y contraindicaciones, un requisito bloqueante para cualquier evaluación de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Aportar evidencia preclínica o de mecanismo que vincule la inhibición de la 5-alfa reductasa con la biología de *TRPS1* o del síndrome de Ambras.
- Buscar reportes de caso o estudios específicos de finasterida en hipertricosis congénita.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original, que siguen pendientes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

