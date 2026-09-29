---
layout: default
title: Ceftazidime
parent: Evidencia moderada (L3-L4)
nav_order: 110
evidence_level: L4
indication_count: 10
---

# Ceftazidime
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

# Ceftazidima: De Antibiótico Antipseudomónico a Hiperamilasemia

## Resumen en Una Frase

Ceftazidima es una cefalosporina de tercera generación con actividad antipseudomónica, comercializada en España con 20 autorizaciones. El modelo TxGNN predice que podría ser útil para **hiperamilasemia**, pero la señal es débil e indirecta: **0 ensayos clínicos** y **1 publicación** que no es específica de ceftazidima.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99,51 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado en el paquete de evidencia. Según la información conocida, ceftazidima es un antibiótico betalactámico que inhibe la síntesis de la pared celular bacteriana y es activo frente a muchos bacilos gramnegativos. Su eficacia antibacteriana está establecida, pero no hay una vía mecanística directa hacia la hiperamilasemia.

La hiperamilasemia es un biomarcador de lesión pancreática, no una infección tratable. El único vínculo plausible es indirecto: la profilaxis antibiótica sistemática podría reducir la pancreatitis posterior a CPRE (colangiopancreatografía retrógrada endoscópica) y, con ella, la elevación de amilasa. Este razonamiento se apoya en un solo registro y no está confirmado para ceftazidima en particular.

El puntaje alto del modelo (99,51 %) debe interpretarse con cautela. Por sí solo no equivale a evidencia clínica, y puede reflejar cercanía en el grafo de conocimiento más que un efecto terapéutico real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11985972](https://pubmed.ncbi.nlm.nih.gov/11985972/) | 2001 | Estudio prospectivo (diseño no confirmado) | J Gastrointest Surg | Evalúa si la profilaxis antibiótica sistemática reduce la pancreatitis post-CPRE. El título indica una reducción, pero el resumen disponible está truncado y no identifica a ceftazidima como el antibiótico estudiado. |

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones. Los textos de indicación aprobada no están disponibles en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 90753 | ALFAGEM 1 G POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION | Polvo para solución inyectable y para perfusión |
| 71574 | CEFTAZIDIMA KABI 1 g POLVO PARA SOLUCION INYECTABLE EFG | Polvo para solución inyectable y para perfusión |
| 83904 | CEFTAZIDIMA QILU 500 MG POLVO PARA SOLUCION INYECTABLE EFG | Polvo para solución inyectable |
| 72674 | CEFTAZIDIMA KABI 2 g POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION EFG | Polvo para solución inyectable y para perfusión |
| 90754 | ALFAGEM 2 G POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION EFG | Polvo para solución inyectable y para perfusión |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la única publicación no es específica de ceftazidima. El vínculo con la hiperamilasemia es indirecto, porque pasaría por la prevención de la pancreatitis post-CPRE. La evidencia actual se limita a una pregunta de investigación.

**Para avanzar se necesita:**
- Obtener el texto completo del estudio PMID 11985972 y confirmar qué antibiótico se usó y qué desenlace se midió (amilasa o pancreatitis).
- Revisar la literatura sobre profilaxis antibiótica en CPRE con ceftazidima como agente concreto.
- Descargar el prospecto de la AEMPS para confirmar las indicaciones autorizadas y completar advertencias, contraindicaciones e interacciones.
- Completar los datos de mecanismo de acción desde DrugBank.

**Otras predicciones del mismo fármaco con más respaldo que la principal:**

| Indicación Predicha | Nivel | Evidencia disponible | Observación |
|------|------|------|------|
| Infección del tracto urinario | L3 | 18 ensayos listados y 20 publicaciones, ninguno un ECA de ceftazidima sola | Los datos directos son de ceftazidima-avibactam (combinación), estudios de práctica real y revisiones. Probablemente sea un uso ya autorizado más que un reposicionamiento; hay que confirmarlo con la ficha técnica. Proceed with Guardrails, a la espera de un ECA específico para ITU. |
| Otitis media infecciosa | L3 | 14 publicaciones, sin ensayos registrados | Series pediátricas antiguas (1990-2000) de ceftazidima en otitis media supurativa crónica por *Pseudomonas*. Se requeriría un estudio prospectivo. |

El resto de las predicciones (síndrome de hiperviscosidad policlonal, analbuminemia congénita, uretritis gonocócica, uretritis por *Ureaplasma*, incompatibilidad de grupo sanguíneo, infección por *Peptostreptococcus*) carecen de respaldo clínico. En algunas, el mecanismo argumenta en contra de la predicción. Se mantienen en Hold, y epiglotitis queda como pregunta de investigación con solo reportes de casos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

