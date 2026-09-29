---
layout: default
title: Codeine
parent: Evidencia moderada (L3-L4)
nav_order: 144
evidence_level: L4
indication_count: 4
---

# Codeine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Codeína: De Dolor y Tos a Enfermedad de la Cavidad Nasal

## Resumen en Una Frase

La codeína es un opioide utilizado para el dolor sistémico, la tos y, en algunos casos, la diarrea.
El modelo TxGNN predice que podría ser efectiva para **enfermedad de la cavidad nasal**,
pero hay **0 ensayos clínicos** y solo **2 publicaciones** (dos casos clínicos), que describen daño por mal uso de opioides y no un efecto terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dolor sistémico y tos (según la farmacología; los textos de indicación de AEMPS no están disponibles) |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 99,93% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información farmacológica disponible, la codeína actúa sobre el receptor opioide μ (gen OPRM1), y esto explica su uso analgésico y antitusivo. Ese mecanismo no aporta una razón para tratar una enfermedad de la cavidad nasal.

Las dos publicaciones recuperadas apuntan en sentido contrario al tratamiento. Una describe necrosis de la cavidad nasal y la faringe por abuso intranasal de hidrocodona-paracetamol. La otra describe un rinolito ("opioma") formado alrededor de una mezcla endurecida de codeína y opio. El puntaje tan alto del modelo (0,999) probablemente refleja una asociación en el grafo de conocimiento con patología nasal inducida por opioides, no un efecto terapéutico.

En conclusión, la predicción no está respaldada mecanísticamente y debe interpretarse como una asociación de daño, no de beneficio.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22965281](https://pubmed.ncbi.nlm.nih.gov/22965281/) | 2012 | Reporte de caso | The Laryngoscope | El abuso intranasal de hidrocodona-paracetamol provoca necrosis de la cavidad nasal y la faringe. Es un opioide distinto de la codeína y describe un daño, no un beneficio. |
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Reporte de caso | Ear, Nose & Throat Journal | Rinolito inusual formado alrededor de un cuerpo extraño compuesto por codeína y opio ("opioma") en un varón de 21 años. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 65343 | NOTUSIN SOLUCION ORAL | Solución oral |
| 24797 | HISTAVERIN 2 mg/ml JARABE | Jarabe |
| 32357 | TOSEINA 2 mg/ml SOLUCION ORAL | Solución oral |
| 5255 | CODEISAN 1,26 mg/ml JARABE | Jarabe |
| 1778 | CODEISAN 28,7 mg COMPRIMIDOS | Comprimido |

## Consideraciones de Seguridad

- **Señal de urticaria (predicción de menor rango, rango 4)**: la literatura describe la codeína como un liberador no mediado por IgE de histamina desde los mastocitos, usada como control positivo en pruebas cutáneas intradérmicas. También hay casos de erupción urticarial por codeína oral.
- **Uso intranasal**: los casos recuperados asocian el uso intranasal indebido de opioides con necrosis y rinolitiasis.
- Para advertencias, contraindicaciones e interacciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos, la literatura disponible describe daño y no beneficio, y no existe un mecanismo terapéutico plausible. El puntaje alto de TxGNN no compensa la ausencia de evidencia de eficacia.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de AEMPS (advertencias y contraindicaciones), un dato bloqueante para el cribado de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Evidencia real de eficacia (estudios preclínicos o clínicos) que apoye un beneficio en enfermedad de la cavidad nasal.
- Otras predicciones del mismo paquete: laringofaringitis aguda (L5, solo predicción, solapa con el uso antitusivo actual), cefalea trigémino-autonómica (L4, casos indirectos, riesgo de uso excesivo) y urticaria alérgica (L4, dirección causal, no terapéutica). Ninguna cambia la decisión de Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

