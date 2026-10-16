---
layout: default
title: Biotin
parent: Solo predicción del modelo (L5)
nav_order: 106
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Biotin: nueva indicación predicha, Dispepsia (nivel de evidencia L5). Indicación original: Deficiencia nutricional de biotina (según el grafo de conocimiento"
---

# Biotin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Biotina: De Deficiencia Nutricional de Biotina a Dispepsia

## Resumen en Una Frase

La biotina es una vitamina del grupo B, utilizada originalmente para tratar la deficiencia nutricional de biotina.
El modelo TxGNN predice que podría ser efectiva para **dispepsia**, pero actualmente no hay **ningún ensayo clínico** y solo hay **6 publicaciones** de relevancia limitada, ninguna de las cuales evalúa la biotina como tratamiento de la dispepsia.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Deficiencia nutricional de biotina (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Dispepsia |
| Puntaje de Predicción TxGNN | 99.43% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la biotina actúa como cofactor de carboxilasas que participan en el metabolismo de carbohidratos, grasas y aminoácidos. Su eficacia en la deficiencia de biotina es conocida, y mecanísticamente podría tener alguna relación con la dispepsia.

La relación entre ambas indicaciones es débil. La deficiencia de biotina puede asociarse a síntomas gastrointestinales (por ejemplo, náuseas y anorexia), lo que podría explicar una asociación laxa con la dispepsia. Sin embargo, no se ha establecido un vínculo mecanístico directo.

El puntaje elevado de TxGNN (0.994) es solo una predicción del modelo. Sin datos de mecanismo de acción, no es posible verificar un razonamiento basado en el mecanismo. Cabe señalar que la segunda predicción del modelo, la gastroparesia (99.42%), carece por completo de evidencia clínica o bibliográfica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Reporte de caso | The Journal of Dermatology | Deficiencia de biotina en un lactante de 5 meses alimentado solo con fórmula de aminoácidos, con diagnóstico neonatal de dispepsia; presentó alopecia y dermatitis, y niveles bajos de biotina en suero y orina. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Revisión | Eksperimental'naia i klinicheskaia gastroenterologiia | Suplemento con inulina, oligofructosa, vitaminas (incluida biotina) y minerales para corregir la microbiota intestinal en pacientes con patología broncopulmonar tras antibióticos; la biotina es solo un componente de una mezcla. |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Cohorte | International Journal of Molecular Medicine | Células endocrinas del antro gástrico en pacientes con síndrome del intestino irritable; no evalúa biotina. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Cohorte | World Journal of Gastrointestinal Endoscopy | Células endocrinas de la mucosa oxíntica en pacientes con síndrome del intestino irritable; no evalúa biotina. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Cohorte | Journal of Clinical Pathology | Interleucina 10 en la gastritis asociada a *Helicobacter pylori*; no evalúa biotina. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Cohorte | Kidney International | Linfocitos T de intestino delgado en nefropatía IgA; no evalúa biotina. |

Ninguna de estas publicaciones prueba la biotina como tratamiento de la dispepsia.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 24616 | MEDEBIOTIN FUERTE COMPRIMIDOS | Comprimido | No disponible en los datos compilados |
| 34236 | MEDEBIOTIN FUERTE SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |

Ambas autorizaciones pertenecen a Laboratorio Reig Jofre, S.A., son de monofármaco y están vigentes.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): enfermedad renal, piouréter, sarcoidosis, hiperparatiroidismo, osteítis fibrosa, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, nefrolitiasis (incluida la susceptibilidad asociada a SLC26A1), nefropatía aguda por uratos, estreñimiento y lesiones óseas metastásicas líticas.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5): no hay ensayos clínicos ni literatura que pruebe la biotina en dispepsia, y el mecanismo de acción no está disponible para respaldar el vínculo.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA)
- Información de seguridad del prospecto de la AEMPS (advertencias y contraindicaciones), necesaria antes de cualquier evaluación de seguridad
- Textos de indicaciones aprobadas de las autorizaciones españolas
- Estudios clínicos o preclínicos que evalúen la biotina en dispepsia
- Análisis de compatibilidad de vías de administración y revisión de las contraindicaciones renales y de calcio señaladas por el grafo de conocimiento
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

