---
layout: default
title: Nystatin
parent: Evidencia moderada (L3-L4)
nav_order: 386
evidence_level: L3
indication_count: 10
---

# Nystatin
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
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

# Nistatina: Evaluación de Reposicionamiento hacia Vulvovaginitis

## Resumen en Una Frase

La nistatina es un antifúngico poliénico comercializado en España como suspensión oral (Mycostatin). El texto de su indicación aprobada no figura en los datos recibidos.
El modelo TxGNN predice que podría ser efectiva para **vulvovaginitis**, y no hay **ensayos clínicos** registrados. Hay **20 publicaciones**, en su mayoría revisiones narrativas y resúmenes de evidencia sobre candidiasis vulvovaginal.
Es probable que se trate de un uso ya conocido de la nistatina, más que de un reposicionamiento genuino.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Vulvovaginitis |
| Puntaje de Predicción TxGNN | 99,92 % |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

La nistatina es un antifúngico poliénico que se une al ergosterol de la membrana de *Candida*, lo que provoca fuga de contenido celular y muerte del hongo. Los datos de mecanismo de acción de DrugBank no estaban disponibles en el paquete de evidencia, así que esta descripción procede del conocimiento farmacológico general.

*Candida* es la causa dominante de la vulvovaginitis infecciosa (85-90 % de los casos de candidiasis vulvovaginal son por *C. albicans*, según las revisiones de BMJ Clinical Evidence). Por eso el vínculo mecanístico es directo. La nistatina se introdujo en los años 50 para tratar la candidiasis vulvovaginal, aunque después fue superada por imidazoles y triazoles como primera opción (Ernest, 1992).

La predicción es plausible solo para la vulvovaginitis de origen candidiásico. No hay respaldo para las formas no fúngicas (bacteriana, atrófica, de hipersensibilidad).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Revisión | Pharmaceutics | Manejo actual de la candidiasis vulvovaginal resistente a fluconazol. Analiza alternativas como ácido bórico, nistatina, oteseconazol e ibrexafungerp. |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Revisión | BMJ Clinical Evidence | Resumen de evidencia sobre candidiasis vulvovaginal, segunda causa más común de vaginitis. |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Revisión | Journal of Women's Health | Evidencia clínica del ácido bórico en candidiasis vulvovaginal recurrente. Las especies no albicans son más resistentes a los azoles. |
| [21718579](https://pubmed.ncbi.nlm.nih.gov/21718579/) | 2010 | Revisión | BMJ Clinical Evidence | Versión anterior del resumen de evidencia sobre candidiasis vulvovaginal. |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Estudio clínico / in vitro | Mycoses | 283 pacientes con candidiasis vulvovaginal complicada. Se correlacionó la sensibilidad in vitro a fluconazol y nistatina con el resultado clínico. |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Estudio clínico (sin verificar) | Ceska Gynekologie | Diagnóstico y tratamiento de vulvovaginitis mixtas con productos vaginales combinados de nifuratel y nistatina. |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | Preclínico (modelo en rata) | BMC Microbiology | La nistatina potencia la respuesta inmune contra *C. albicans* y protege la ultraestructura del epitelio vaginal. |
| [32104010](https://pubmed.ncbi.nlm.nih.gov/32104010/) | 2020 | In vitro | Infection and Drug Resistance | Actividad antifúngica de nanopartículas de ZnO y nistatina en aislados de *C. albicans* resistentes a fluconazol. |
| [41149932](https://pubmed.ncbi.nlm.nih.gov/41149932/) | 2025 | In vitro / epidemiológico | Journal of Fungi | Etiología de la candidiasis vulvovaginal en Ecuador y sensibilidad in vitro de aislados a varios antifúngicos, incluida la nistatina. |
| [1436934](https://pubmed.ncbi.nlm.nih.gov/1436934/) | 1992 | Revisión | Obstetrics and Gynecology Clinics of North America | Antifúngicos tópicos. La nistatina fue superada por imidazoles y triazoles como primera elección. |

No se identificó ningún ensayo controlado aleatorizado específico de nistatina a partir de los títulos y resúmenes disponibles.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 28262 | MYCOSTATIN 100.000 UI/ml SUSPENSIÓN ORAL (Substipharm) | Suspensión oral | No disponible en los datos recibidos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El vínculo mecanístico con *Candida* es directo y la literatura sobre candidiasis vulvovaginal es abundante. Sin embargo, casi toda es revisión narrativa o resumen de evidencia, sin ensayos registrados. Además, esto parece un uso ya conocido más que un reposicionamiento genuino, por lo que el nivel se mantiene en L3 y no en L1.

**Para avanzar se necesita:**
- Confirmar la indicación etiquetada y los datos de ECA frente a fuentes primarias, y comprobar si la vía es compatible (Mycostatin en España es solo suspensión oral, sin forma vaginal en los datos recibidos).
- Limitar el alcance a la vulvovaginitis candidiásica. No extenderlo a la vulvovaginitis no fúngica (bacteriana, atrófica, de hipersensibilidad).
- Obtener las advertencias y contraindicaciones del prospecto de la AEMPS, indispensables antes de cualquier cribado de seguridad.
- Obtener los datos de mecanismo de acción de DrugBank.
- Definir el subgrupo de etiología fúngica en la vulvitis (predicción de rango 8, nivel L4). Las otras ocho predicciones no tienen respaldo mecanístico ni clínico y quedan en Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

