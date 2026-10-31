---
layout: default
title: Omeprazole
parent: Solo predicción del modelo (L5)
nav_order: 590
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
monitor_inn: "Omeprazole"
predicted_indications: ["duodenal obstruction"]
description: "Omeprazole: nueva indicación predicha, Duodenal obstruction (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Omeprazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Omeprazole: Duodenal obstruction
{: .text-alpha }

## Resumen en Una Frase

Omeprazol es un inhibidor de la bomba de protones, utilizado originalmente para el tratamiento de la úlcera gástrica, la úlcera duodenal, la enfermedad por reflujo gastroesofágico y el síndrome de Zollinger-Ellison.
El modelo TxGNN predice que podría ser efectivo para el **reflujo duodenogástrico**, pero la evidencia es limitada: **1 ensayo clínico** (no interventivo y sin relación directa con el fármaco) y **15 publicaciones**, en su mayoría estudios pequeños, en animales o de contexto general.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Duodenal obstruction |
| Puntaje de Predicción TxGNN | 0.9964 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 13) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, omeprazol es un inhibidor de la bomba de protones que suprime la secreción de ácido gástrico; los datos farmacológicos lo vinculan con la diana ATP4A (la H+/K+-ATPasa gástrica), y su eficacia en reflujo gastroesofágico, esofagitis y úlcera péptica está comprobada.

El reflujo duodenogástrico (paso de bilis y contenido duodenal al estómago y, en ocasiones, al esófago) comparte una fisiopatología solapada con esas indicaciones. Algunos estudios clínicos pequeños sugieren que omeprazol podría reducir el reflujo biliar en el esófago de Barrett y en el reflujo biliar esofágico pediátrico, lo que respalda parcialmente la predicción.

Sin embargo, la supresión ácida no bloquea directamente el reflujo biliar. Además, estudios en ratas indican que combinar bloqueo ácido con reflujo duodenogástrico puede estimular el crecimiento de la mucosa y promover la carcinogénesis gástrica. Por ello, la puntuación alta del modelo refleja sobre todo la cercanía con el mecanismo del reflujo gastroesofágico, no una demostración de eficacia.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | N/A (diagnóstico) | Completado | 157 | Imagen endoscópica trimodal para distinguir la dispepsia funcional de la enfermedad por reflujo. No evalúa omeprazol, por lo que no aporta evidencia directa de eficacia. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | Estudio clínico | Gut | Efecto de omeprazol 20 mg dos veces al día sobre el reflujo biliar duodenogástrico y duodenogastroesofágico en el esófago de Barrett |
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Estudio clínico | Scand J Gastroenterol | Efecto de omeprazol sobre el reflujo duodenogástrico antral en el esófago de Barrett; trabajos previos sugieren que podría reducirlo |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Estudio prospectivo | J Pediatr Gastroenterol Nutr | Tratamiento con omeprazol del reflujo biliar esofágico en niños |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Cohorte/Revisión | Eur J Pediatr | Reflujo duodenogástrico primario en seis niños y adolescentes con síntomas atípicos que no respondían a antiácidos |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revisión | Eur J Clin Pharmacol | Actualización sobre el uso clínico y la farmacocinética de los inhibidores de la bomba de protones |
| [8076761](https://pubmed.ncbi.nlm.nih.gov/8076761/) | 1994 | Estudio clínico | Gastroenterology | Relación entre pH, reflujo duodenogastroesofágico y esófago de Barrett |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Estudio animal | Dig Dis Sci | En ratas, el bloqueo ácido con omeprazol promueve la carcinogénesis gástrica inducida por reflujo duodenogástrico |
| [8943968](https://pubmed.ncbi.nlm.nih.gov/8943968/) | 1996 | Estudio animal | Dig Dis Sci | El reflujo duodenogástrico estimula el crecimiento de la mucosa, potenciado por el bloqueo ácido |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Estudio animal | Acta Cir Bras | Posible efecto protector de omeprazol frente al adenocarcinoma gástrico en ratas con reflujo duodenogástrico |
| [20697939](https://pubmed.ncbi.nlm.nih.gov/20697939/) | 2010 | Estudio clínico (indirecto) | Chin J Integr Med | Acupuntura en el reflujo gastroesofágico; relación solo indirecta |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 63301 | Omeprazol Kern Pharma 20 mg cápsulas duras gastrorresistentes EFG | Cápsula dura gastrorresistente | No disponible en los datos compilados |
| 66871 | Omeprazol Serraclinics 40 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | No disponible en los datos compilados |
| 86474 | Omeprazol Viatris Pharmaceuticals 20 mg cápsulas duras gastrorresistentes | Cápsula dura gastrorresistente | No disponible en los datos compilados |
| 89376 | Omereflux 20 mg cápsulas duras gastrorresistentes | Cápsula dura gastrorresistente | No disponible en los datos compilados |
| 88991 | Omeprazol Noridem 40 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | No disponible en los datos compilados |

Hay 20 autorizaciones vigentes en total, todas de omeprazol como principio activo único.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del prospecto): insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, osteoporosis, osteoporosis posmenopáusica, fractura ósea y gastritis atrófica crónica.
- **Riesgo específico de esta indicación**: estudios en ratas indican que el bloqueo ácido combinado con reflujo duodenogástrico puede promover la carcinogénesis gástrica y el crecimiento de la mucosa. Requiere evaluación antes de cualquier uso en esta indicación.
- **Interacciones y dianas farmacológicas**: los datos registran la interacción farmacológica con ATP4A (bomba de protones gástrica, diana principal) y con ClC-2 (canal de cloruro), sin nivel de gravedad asignado. No se dispone de una lista de interacciones con otros fármacos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La puntuación del modelo es muy alta, pero la evidencia clínica es escasa y mixta: el único ensayo registrado no evalúa omeprazol, los estudios clínicos son pequeños y los datos animales señalan un posible riesgo carcinogénico. El mecanismo (supresión ácida) no actúa directamente sobre el reflujo biliar.

**Para avanzar se necesita:**
- Ensayos controlados y aleatorizados de omeprazol frente a placebo o comparador en reflujo duodenogástrico, con medición objetiva del reflujo biliar.
- Evaluación de seguridad a largo plazo, en particular el riesgo de carcinogénesis gástrica con bloqueo ácido sostenido.
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS, aún no disponibles en los datos compilados.
- Datos detallados del mecanismo de acción y de las indicaciones autorizadas en España.
- Análisis de compatibilidad de vías de administración y de similitud con las indicaciones originales.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

