---
layout: default
title: Acetylcysteine
parent: Solo predicción del modelo (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Acetylcysteine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Acetilcisteína: De Bronquitis e Intoxicación por Paracetamol a Enfermedad Trombótica

## Resumen en Una Frase

La acetilcisteína es un mucolítico y antioxidante, utilizado originalmente en bronquitis, fibrosis quística, bronquiectasias y como antídoto en la intoxicación por paracetamol.
El modelo TxGNN predice que podría ser efectiva para la **enfermedad trombótica**,
con **7 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, aunque la mayoría de la evidencia se centra en subtipos concretos (púrpura trombótica trombocitopénica y microangiopatía trombótica asociada a trasplante).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Bronquitis, intoxicación por paracetamol, fibrosis quística, bronquiectasias (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Enfermedad trombótica (thrombotic disease) |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L1 (según la clasificación de los datos compilados; ver nota en la Conclusión) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, la acetilcisteína es un compuesto tiólico con actividad mucolítica y antioxidante, con eficacia comprobada en patología respiratoria y en la intoxicación por paracetamol.

El vínculo mecanístico propuesto es que, al ser un tiol, puede reducir los puentes disulfuro de los multímeros ultragrandes del factor de von Willebrand (VWF), disminuyendo la agregación plaquetaria mediada por VWF. Esta es la base racional en la púrpura trombótica trombocitopénica (PTT) y en la microangiopatía trombótica asociada a trasplante (TMA-AT), respaldada por modelos preclínicos en ratón y babuino. Además, posee efectos antioxidantes y de protección endotelial.

Conviene destacar que "enfermedad trombótica" es un término paraguas heterogéneo que agrupa PTT, TMA-AT, trombocitopenia inmune (PTI) y fenotipos trombóticos en insuficiencia renal. La relación con las indicaciones originales (respiratorias y toxicológicas) es indirecta y se basa en el efecto antioxidante y tiólico, no en una similitud de enfermedad.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Fase 3 | Completado | 170 | NAC en microangiopatía trombótica asociada a trasplante de progenitores hematopoyéticos; ensayo tardío más directo, pero no se dispone de resultados |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Fase 2/3 | Activo, sin reclutar | 44 | Ensayo multicéntrico de brazo único de NAC en TMA-AT; sin resultados aún |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Fase 2 | Completado | 40 | Ensayo aleatorizado, doble ciego, cruzado de NAC sobre el fenotipo trombótico en insuficiencia renal; indirecto |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Fase 2 | Desconocido | 44 | Dexametasona a dosis altas + NAC en trombocitopenia inmune de nuevo diagnóstico; combinación que confunde el efecto |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Fase 1/2 | Desconocido | 200 | Atorvastatina, NAC y danazol en PTI resistente a esteroides o recaída; indicación indirecta |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Fase 1 temprana | Completado | 15 | Atorvastatina + NAC sobre recuento plaquetario en PTI; muestra pequeña |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Fase 1 temprana | Completado | 3 | Piloto de NAC intravenosa en sospecha de PTT; muestra insuficiente para inferir eficacia |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | Revisión sistemática | J Clin Med | Revisión sistemática y valoración crítica de NAC en PTT |
| [42338865](https://pubmed.ncbi.nlm.nih.gov/42338865/) | 2026 | Revisión sistemática | Cureus | NAC como terapia adyuvante en PTT refractaria o recurrente |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Estudio de cohortes | Ann Hematol | Asociación entre NAC y mortalidad hospitalaria en PTT adquirida; uso controvertido |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Preclínico (ratón/babuino) | Blood | NAC en modelos preclínicos de PTT |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Revisión | Expert Rev Hematol | Fármacos reposicionados y nuevos agentes en PTT, incluida NAC |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Revisión | Blood | Revisión general de la PTT |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Revisión | J Clin Med | Fisiopatología, diagnóstico y manejo de la PTT |
| [28645643](https://pubmed.ncbi.nlm.nih.gov/28645643/) | 2017 | Revisión | Transfus Clin Biol | Manejo de la PTT: recambio plasmático y rituximab |
| [36410267](https://pubmed.ncbi.nlm.nih.gov/36410267/) | 2022 | Revisión | J Infect Public Health | NAC en COVID-19, con estado protrombótico y estrés oxidativo |
| [32614622](https://pubmed.ncbi.nlm.nih.gov/32614622/) | 2021 | Revisión | Platelets | Nuevas estrategias antiplaquetarias dirigidas a VWF y GPIb |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62663 | Fluimucil Forte 600 mg comprimidos efervescentes | Comprimido efervescente | No disponible en los datos compilados |
| 66340 | Acetilcisteína Pensa 200 mg polvo para solución oral EFG | Polvo para solución oral | No disponible en los datos compilados |
| 63268 | Acetilcisteína Teva-Ratiopharm 600 mg comprimidos efervescentes EFG | Comprimido efervescente | No disponible en los datos compilados |
| 41474 | Flumil 100 mg/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 63512 | Fluimucil Pediátrico 20 mg/ml solución oral | Solución oral | No disponible en los datos compilados |

Se muestran 5 de las 20 autorizaciones vigentes, todas de principio activo único.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto):** úlcera péptica, trastorno hipotensivo, insuficiencia respiratoria, asma, enfermedad bronquial y varices esofágicas.
- **Interacciones farmacológicas:** se identificaron 100 interacciones en la base de datos DDInter. Entre las de nivel conocido: **moderada** con insulina humana inhalada; **menor** con carbón activado. Otras (por ejemplo, morfina, metformina, omeprazol, doxiciclina, vancomicina, prednisona) figuran con nivel de gravedad no determinado.

Las advertencias y contraindicaciones del prospecto no están disponibles; consultar el prospecto de la AEMPS.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3 completado en TMA-AT, un ensayo de Fase 2/3 en curso, revisiones sistemáticas y respaldo preclínico en PTT, y el fármaco está ampliamente comercializado con perfil de seguridad conocido. Sin embargo, no se dispone de resultados publicados de eficacia, la indicación es un término paraguas heterogéneo y la mayor parte de los estudios son pequeños o con combinaciones. Aunque los datos asignan el nivel L1, solo hay un ECA de Fase 3 completado, por lo que un criterio estricto sugeriría un nivel inferior.

**Para avanzar se necesita:**
- Resultados y criterio de valoración principal del ensayo NCT03252925, y seguimiento de NCT07279610.
- Delimitar el subtipo concreto (TMA-AT o PTT) en lugar de "enfermedad trombótica" en general.
- Datos del mecanismo de acción y de advertencias/contraindicaciones del prospecto de la AEMPS (actualmente ausentes).
- Revisión de las contraindicaciones del grafo (asma, úlcera péptica, hipotensión) en las poblaciones objetivo y plan de vigilancia de interacciones.
- Definir dosis y vía de administración (por ejemplo, intravenosa) para la nueva indicación.

**Otras predicciones del modelo (para referencia):** la enfermedad del ojo seco (rank 4) cuenta con evidencia más madura (nivel L2, con ECA publicados), aunque principalmente con la formulación tópica de quitosano-NAC, y podría evaluarse con "Proceed with Guardrails" como línea alternativa. Las demás (glaucoma de ángulo cerrado, enfermedades de cavidad nasal, faringitis, laringofaringitis aguda, enfermedad traqueal, ataque isquémico transitorio, laringotraqueítis) tienen evidencia nula o preclínica (L4-L5) y se recomienda mantenerlas en **Hold**.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

