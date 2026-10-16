---
layout: default
title: Talc
parent: Evidencia moderada (L3-L4)
nav_order: 761
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Talc: nueva indicación predicha, Enfermedad trombótica (nivel de evidencia L4). Indicación original: No disponible en los datos compilados (la autorización no incluye tex…"
---

# Talc
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Talco: De Uso Dermatológico en Polvo Cutáneo a Enfermedad Trombótica (predicción del modelo)

## Resumen en Una Frase

El talco está autorizado en España como polvo cutáneo (ICTIOMEN POLVO), aunque la ficha de autorización no incluye un texto de indicación.
El modelo TxGNN predice que podría ser efectivo para **enfermedad trombótica**, pero **no hay ensayos clínicos** y las 11 publicaciones recuperadas describen al talco como **causa** de eventos trombóticos y embólicos, no como tratamiento.
La predicción carece de respaldo clínico y presenta una señal de seguridad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (la autorización no incluye texto de indicación) |
| Nueva Indicación Predicha | Enfermedad trombótica |
| Puntaje de Predicción TxGNN | 99,85 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. El talco (silicato de magnesio) se comercializa en España como polvo cutáneo de uso tópico, y no se dispone de una indicación aprobada documentada en los datos compilados.

La literatura recuperada no respalda un efecto terapéutico en trombosis. Describe que el talco inyectado por vía intravenosa (por ejemplo, en consumidores de drogas que inyectan comprimidos triturados) provoca microembolia pulmonar, hipertensión pulmonar angiotrombótica, granulomatosis y microembolización retiniana y cerebral. El alto puntaje del modelo probablemente refleja una asociación fármaco-enfermedad de tipo efecto adverso en el grafo de conocimiento, no una relación terapéutica.

Por ello, **el reposicionamiento del talco para trombosis es biológicamente poco plausible** y supone una señal de seguridad.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Todas las publicaciones son de tipo revisión, reporte de caso o serie de casos; ninguna es un ECA ni muestra beneficio terapéutico.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7756380](https://pubmed.ncbi.nlm.nih.gov/7756380/) | 1995 | Revisión | Current Opinion in Oncology | Complicaciones intratorácicas de la neoplasia; la trombosis con síndrome de vena cava superior aumenta con los catéteres venosos |
| [4854601](https://pubmed.ncbi.nlm.nih.gov/4854601/) | 1974 | Serie de casos | J Can Assoc Radiol | Granulomatosis por talco e hipertensión pulmonar angiotrombótica en adictos a drogas |
| [1784766](https://pubmed.ncbi.nlm.nih.gov/1784766/) | 1991 | Sin clasificar | Rev Clin Esp | Dos casos de granulomatosis pulmonar angiotrombótica por talco en adictos a drogas intravenosas |
| [6893924](https://pubmed.ncbi.nlm.nih.gov/6893924/) | 1981 | Reporte de caso | Arch Pathol Lab Med | Embolia pulmonar y granulomatosis por celulosa microcristalina inyectada; la trombosis es la lesión vascular principal |
| [7387487](https://pubmed.ncbi.nlm.nih.gov/7387487/) | 1980 | Reporte de caso | Arch Neurol | Síndrome medular medial con granulomatosis sistémica por talco e infartos isquémicos |
| [4692998](https://pubmed.ncbi.nlm.nih.gov/4692998/) | 1973 | Reporte de caso | Am J Med Sci | Microembolización retiniana y cerebral de talco en un consumidor de drogas |
| [23700302](https://pubmed.ncbi.nlm.nih.gov/23700302/) | 2013 | Reporte de caso | Dtsch Med Wochenschr | Insuficiencia cardíaca derecha aguda tras inyección intravenosa de heroína y flunitrazepam triturado |
| [8537192](https://pubmed.ncbi.nlm.nih.gov/8537192/) | 1995 | Serie de casos | Int Ophthalmol | Zona avascular foveal en oclusión de rama venosa retiniana; la retinopatía por talco se cita como enfermedad vaso-oclusiva |
| [35648447](https://pubmed.ncbi.nlm.nih.gov/35648447/) | 2022 | Reporte de caso | Tex Heart Inst J | Síndrome de Trousseau en una paciente con neoplasia de colon oculta; sin relación terapéutica con el talco |
| [8010794](https://pubmed.ncbi.nlm.nih.gov/8010794/) | 1994 | Serie de casos | Ann Thorac Surg | Cirugía toracoscópica en quilotórax; sin relación con tratamiento de trombosis |
| [41646593](https://pubmed.ncbi.nlm.nih.gov/41646593/) | 2026 | Reporte de caso | Cureus | Neumotórax recurrente tras neumonectomía manejado con ECMO; sin relación con trombosis |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 48911 | ICTIOMEN POLVO | Polvo cutáneo | No disponible en los datos compilados |

Titular: Casen Recordati S.L. (autorización vigente, monofármaco).

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: no se encontraron interacciones en la consulta realizada.
- **Señal de seguridad de la literatura**: la administración intravenosa o inhalada de talco se asocia con embolia, granulomatosis, hipertensión pulmonar angiotrombótica, microembolización retiniana/cerebral y enfermedad respiratoria (endobronquitis, estenosis de la vía aérea, neumoconiosis). Esto es incompatible con un uso en trombosis.

No se dispone de datos de advertencias ni contraindicaciones del prospecto; consultar el prospecto de la AEMPS.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo; la literatura apunta a que el talco causa eventos trombóticos y embólicos, no a que los trate. No existen ensayos clínicos ni un mecanismo plausible, y hay una señal de seguridad clara.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada).
- Obtener datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Confirmar si la asociación del grafo de conocimiento es de tipo efecto adverso y no terapéutico.
- Valorar otras indicaciones predichas solo si aparece evidencia directa; las demás (exóstosis, artritis reumatoide, bronquitis, déficit de cofactor II de heparina, entre otras) tienen evidencia L4-L5 y tampoco muestran respaldo terapéutico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

