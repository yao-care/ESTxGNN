---
layout: default
title: Miconazole
parent: Solo predicción del modelo (L5)
nav_order: 352
evidence_level: L5
indication_count: 1
---

# Miconazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Miconazol: De Infecciones Fúngicas Cutáneas a Acné

## Resumen en Una Frase

Miconazol es un antifúngico imidazólico de uso tópico, utilizado en infecciones cutáneas por hongos como la tiña del pie, la tiña inguinal, la tiña corporal, la candidiasis cutánea y la pitiriasis versicolor.
El modelo TxGNN predice que podría ser efectivo para **acné**, pero la evidencia es débil: **1 ensayo clínico** (suspendido, y que no evalúa miconazol solo) y **4 publicaciones** (un estudio clínico pequeño, una revisión, un estudio en pacientes con foliculitis por *Malassezia* y un estudio *in vitro*).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones fúngicas cutáneas (según el uso clínico registrado en farmacología; los registros de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99,54 % |
| Nivel de Evidencia | L3 (límite inferior; ver justificación abajo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según el conocimiento de la clase, miconazol es un antifúngico azólico que inhibe la enzima fúngica CYP51 (lanosterol 14-alfa-desmetilasa) y bloquea así la síntesis de ergosterol. Esto es una inferencia por clase y no un dato del registro.

Con ese mecanismo se plantean tres vínculos posibles con el acné:

1. **Actividad antibacteriana:** los azoles muestran actividad *in vitro* contra *Cutibacterium (Propionibacterium) acnes*, la bacteria asociada al acné (PMID 20045949).
2. **Actividad contra *Malassezia*:** este hongo causa la foliculitis por *Pityrosporum*, una afección que clínicamente imita al acné y con frecuencia se confunde con él (PMID 8593718).
3. **Efectos antiinflamatorios y antibacterianos en la piel:** descritos para miconazol en una revisión (PMID 18627330).

Conviene ser prudente con el puntaje de 99,54 %: es solo una predicción del modelo y no evidencia clínica. Parte de la señal podría deberse a que la foliculitis por *Malassezia* se clasifica a veces como acné. Por eso el beneficio de miconazol en el acné vulgar propiamente dicho **no está demostrado**.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Fase 2/3 | Suspendido | 80 | Compara una crema combinada de beclometasona + gentamicina + clotrimazol en dermatosis contaminada con lesiones bilaterales simétricas. Sin resultados publicados. |

**Valoración:** el ensayo evalúa una combinación con otro azol (clotrimazol), no miconazol. No se puede aislar la contribución de un azol y la indicación exacta no está confirmada como acné vulgar. Por estar suspendido y sin resultados, no sostiene un nivel de evidencia L1 ni L2.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Estudio clínico (split-face, pequeño) | Skin Research and Technology | Evaluación clínica y bioinstrumental del acné catamenial inflamatorio leve. El resumen disponible no detalla resultados ni confirma el papel de miconazol. |
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Revisión | Expert Opinion on Pharmacotherapy | Revisa los efectos múltiples de miconazol en trastornos de la piel, más allá de su acción antifúngica. |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Estudio clínico (ensayos terapéuticos) | Clinical and Experimental Dermatology | 62 pacientes con foliculitis por *Pityrosporum*, a menudo mal diagnosticada como acné vulgar. Es foliculitis por *Malassezia*, no acné vulgar. |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | Estudio *in vitro* | Biological & Pharmaceutical Bulletin | Actividad de antifúngicos azólicos frente a *P. acnes* aislado de pacientes con acné vulgar. |

No se encontró ningún ensayo controlado aleatorizado. La evidencia es indirecta: un estudio *in vitro*, un estudio en una afección parecida al acné y una revisión narrativa.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 50271 | DAKTARIN 20 MG/G CREMA | Crema | Esteve Pharmaceuticals S.A. |
| 52875 | FUNGISDIN 8,7 MG/ML SOLUCIÓN PARA PULVERIZACIÓN CUTÁNEA | Solución para pulverización cutánea | Isdin S.A. |
| 55962 | DAKTARIN 20 MG/G GEL ORAL | Gel oral | Esteve Pharmaceuticals S.A. |

El registro no incluye el texto de indicación aprobada para estas autorizaciones.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** no hay interacciones fármaco-fármaco clasificadas por nivel. Sí constan datos farmacológicos de dianas humanas de miconazol: TRPM2, TRPV5 y CYP8B1. La bioactividad registrada indica que miconazol se une a CYP8B1 y lo inhibe. Estos datos no equivalen a una evaluación clínica de interacciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- El puntaje de TxGNN es muy alto, pero la evidencia real es escasa e indirecta: el único ensayo está suspendido y evalúa otro azol en combinación, y la literatura son estudios *in vitro*, una revisión y un estudio de foliculitis por *Malassezia* que puede confundirse con acné.
- Miconazol está comercializado en España en formas cutáneas (crema y pulverización), lo que facilitaría un estudio, pero hoy solo se sustenta como pregunta de investigación.

**Para avanzar se necesita:**
- Estudios clínicos controlados de miconazol en acné vulgar confirmado, distinguiéndolo de la foliculitis por *Malassezia*.
- Datos de mecanismo de acción confirmados (consulta a la API de DrugBank).
- Advertencias, contraindicaciones e interacciones de la ficha técnica de AEMPS, hoy no disponibles, antes de cualquier cribado de seguridad.
- Análisis de compatibilidad de vía y de similitud con la indicación original, hoy pendientes.

*Los resultados son solo para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

