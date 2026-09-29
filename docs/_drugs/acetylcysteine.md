---
layout: default
title: Acetylcysteine
parent: Evidencia alta (L1-L2)
nav_order: 16
evidence_level: L2
indication_count: 10
---

# Acetylcysteine
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Acetilcisteína: De Mucolítico a Enfermedad Trombótica

## Resumen en Una Frase

La acetilcisteína (N-acetilcisteína, NAC) se comercializa en España en múltiples formas orales e inyectables, con productos como Fluimucil. Los datos de AEMPS del Evidence Pack no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para la **enfermedad trombótica**, con **10 ensayos clínicos** (5 de ellos directamente relacionados con trombosis) y **20 publicaciones** que respaldan esta dirección, sobre todo en púrpura trombótica trombocitopénica (PTT) y microangiopatía trombótica asociada al trasplante (MAT-AT).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS (texto de indicación vacío). Se asume uso mucolítico, según el nombre de los productos y el racional de la predicción |
| Nueva Indicación Predicha | Enfermedad trombótica (thrombotic disease) |
| Puntaje de Predicción TxGNN | 99,96% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, la acetilcisteína es un agente mucolítico y antioxidante de uso muy extendido. Mecanísticamente podría ser aplicable a enfermedades trombóticas mediadas por el factor de von Willebrand (VWF).

El vínculo mecanístico propuesto es que la NAC rompe puentes disulfuro y reduce así el tamaño de los multímeros de VWF y su capacidad de unirse a las plaquetas. En la PTT y en la MAT-AT, la acumulación de multímeros ultragrandes de VWF favorece la formación de trombos plaquetarios en la microvasculatura. Sus efectos antioxidantes y de protección endotelial añaden un respaldo secundario.

Existen modelos preclínicos en ratón y babuino de PTT (PMID 28011677). En humanos, los ensayos clínicos se concentran en PTT y MAT-AT. La relación con la indicación original (mucolisis, por rotura de puentes disulfuro en el moco) es de tipo mecanístico: la misma química tiol actúa sobre otro sustrato.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Fase 3 | Completado | 170 | NAC en MAT-AT tras trasplante de progenitores hematopoyéticos. Evidencia directa en una condición trombótica, pero no se dispone de resultados |
| [NCT05907486](https://clinicaltrials.gov/study/NCT05907486) | Fase 3 | Desconocido | 260 | NAC para prevenir eventos trombóticos tras trasplante alogénico. Directamente relevante, sin resultados |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Fase 2/3 | Activo, sin reclutamiento | 44 | NAC como tratamiento de MAT-AT, ensayo multicéntrico de un solo brazo. Resultados pendientes |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Fase 1 temprana | Completado | 3 | Piloto de NAC intravenosa en sospecha de PTT junto con recambio plasmático. Muestra demasiado pequeña para inferir |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Fase 2 | Completado | 40 | RENACTIF: ensayo aleatorizado, doble ciego, cruzado, de NAC frente a placebo en insuficiencia renal. Evalúa el fenotipo protrombótico (biomarcadores), no eventos clínicos |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Fase 1/2 | Desconocido | 200 | Atorvastatina + NAC + danazol en trombocitopenia inmune (PTI) resistente a corticoides. Combinación en un trastorno hemorrágico, no trombótico |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Fase 1 temprana | Completado | 15 | Atorvastatina + NAC sobre el recuento plaquetario en PTI. Relación indirecta con trombosis |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Fase 2 | Desconocido | 44 | Dexametasona a dosis altas + NAC en PTI de nuevo diagnóstico. Combinación, enfermedad no trombótica |
| [NCT06518044](https://clinicaltrials.gov/study/NCT06518044) | Fase 2 | Desconocido | 30 | NAC para la recuperación hematopoyética en anemia aplásica grave tras trasplante. No relacionado con trombosis |
| [NCT07662525](https://clinicaltrials.gov/study/NCT07662525) | N/A | Aún no recluta | 50 | Atorvastatina + NAC + romiplostim en PTI. Combinación, no relacionado con trombosis |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35940529](https://pubmed.ncbi.nlm.nih.gov/35940529/) | 2022 | ECA | Transplantation and Cellular Therapy | NAC como profilaxis de MAT-AT tras trasplante: ensayo aleatorizado controlado con placebo en un hospital de Soochow. El extracto disponible no incluye resultados |
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | Revisión sistemática | Journal of Clinical Medicine | Revisión sistemática con valoración crítica de la NAC en PTT refractaria o recidivante |
| [42338865](https://pubmed.ncbi.nlm.nih.gov/42338865/) | 2026 | Revisión sistemática | Cureus | Revisión sistemática de la NAC como tratamiento adyuvante en PTT |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Cohorte | Annals of Hematology | Cohorte retrospectiva sobre la asociación entre NAC y mortalidad hospitalaria en PTT adquirida. El uso de NAC en PTT sigue siendo controvertido |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Preclínico (animal) | Blood | NAC en modelos de PTT en ratón y babuino |
| [28961512](https://pubmed.ncbi.nlm.nih.gov/28961512/) | 2018 | Preclínico | Redox Biology | NAC atenúa la activación plaquetaria sistémica y la trombosis de vasos cerebrales en diabetes |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Revisión | Expert Review of Hematology | Fármacos reutilizados y nuevos agentes en PTT, entre ellos la NAC |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Revisión | Journal of Clinical Medicine | Fisiopatología, diagnóstico y manejo de la PTT |
| [28382967](https://pubmed.ncbi.nlm.nih.gov/28382967/) | 2017 | Revisión | Nature Reviews Disease Primers | Revisión general de la PTT |
| [39737637](https://pubmed.ncbi.nlm.nih.gov/39737637/) | 2025 | Reporte de caso | Journal of Pediatric Hematology/Oncology | Recambio plasmático y NAC en un caso de PTT congénita con insuficiencia renal aguda |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62663 | Fluimucil Forte 600 mg comprimidos efervescentes | Comprimido efervescente | No indicada en los datos disponibles |
| 66340 | Acetilcisteína Pensa 200 mg polvo para solución oral EFG | Polvo para solución oral | No indicada en los datos disponibles |
| 63268 | Acetilcisteína Teva-ratiopharm 600 mg comprimidos efervescentes EFG | Comprimido efervescente | No indicada en los datos disponibles |
| BE150202 | Fluimucil Forte 600 mg comprimidos efervescentes | Comprimido efervescente | No indicada en los datos disponibles |
| 150202IP | Flumilexa 600 mg comprimidos efervescentes EFG | Comprimido efervescente | No indicada en los datos disponibles |

Hay 20 autorizaciones en total. Además de las formas de la tabla, existen solución inyectable, granulado (para solución oral, en sobre y efervescente), comprimido dispersable y solución oral.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Existe evidencia de nivel L2 con un mecanismo plausible (reducción de multímeros de VWF), modelos preclínicos y varios ensayos de Fase 2/3 en PTT y MAT-AT. Sin embargo, ninguno de los ensayos directamente relevantes aporta resultados verificados en este análisis, y falta la revisión de seguridad basada en el prospecto de AEMPS.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), paso previo al cribado de seguridad.
- Obtener los resultados de NCT03252925 (Fase 3, completado) y del ECA publicado (PMID 35940529), y seguir NCT05907486 y NCT07279610.
- Confirmar la compatibilidad de vía y dosis: los ensayos en PTT usan NAC intravenosa, y en España existe solución inyectable, pero las formas más comunes son orales.
- Completar los datos del mecanismo de acción desde DrugBank.
- Evaluar por separado otras predicciones con mejor perfil de evidencia, como el ojo seco (L2, con la salvedad de que la evidencia procede sobre todo de la formulación quitosano-NAC).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

