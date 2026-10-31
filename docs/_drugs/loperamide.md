---
layout: default
title: Loperamide
parent: Solo predicción del modelo (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "Loperamide"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "chronic follicular conjunctivitis", "serous conjunctivitis except viral", "parasitic conjunctivitis", "conjunctival folliculosis", "Angelucci syndrome"]
description: "Loperamide: nueva indicación predicha, Conjuntivitis contagiosa aguda (acute contagious conjunctivitis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Loperamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Loperamide: Conjuntivitis contagiosa aguda (acute contagious conjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Loperamida es un antidiarreico de uso extendido, originalmente utilizado para el tratamiento de la enfermedad diarreica y la disentería.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis contagiosa aguda**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Conjuntivitis contagiosa aguda (acute contagious conjunctivitis) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 17) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, loperamida es un agonista periférico del receptor opioide mu (OPRM1) que actúa sobre las neuronas del plexo mientérico intestinal y reduce la motilidad gastrointestinal. Su eficacia en la diarrea está bien establecida.

**Sin embargo, no existe un vínculo mecanístico establecido con la conjuntivitis.** La señalización opioide a nivel de la superficie ocular no es un mecanismo antiinfeccioso ni antiinflamatorio reconocido para esta enfermedad. El puntaje alto de TxGNN (modelo de aprendizaje profundo) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas (varios subtipos de conjuntivitis comparten puntajes casi idénticos, 0.9965), y no evidencia biológica.

Como dato aislado, la base farmacológica menciona que loperamida, por ser un fármaco catiónico anfifílico, mostró actividad anti-SARS-CoV-2 en cribados de reposicionamiento, probablemente por inducción de fosfolipidosis. Esto no respalda su uso en conjuntivitis.

Entre las demás predicciones (conjuntivitis y subtipos, síndrome de Angelucci, gastroduodenitis, disentería amebiana), la que tiene algo de literatura es la disentería amebiana, pero esa literatura apunta a **daño potencial**, no a beneficio (ver más abajo).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para conjuntivitis contagiosa aguda.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para conjuntivitis contagiosa aguda.

Como contexto, en otras indicaciones predichas del mismo fármaco se identificaron estas publicaciones, todas con señales de seguridad y no de eficacia:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Reporte de caso | J Travel Med | Colitis amebiana fulminante tras uso de loperamida; el uso intenso del fármaco pudo influir en la evolución (megacolon tóxico). Predicción: disentería amebiana |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Revisión | Am J Med | Tratamientos no líquidos y quimioprofilaxis de la diarrea aguda; los agentes inespecíficos pueden reducir los síntomas. Predicción: disentería amebiana |
| [41924411](https://pubmed.ncbi.nlm.nih.gov/41924411/) | 2026 | Reporte de caso | Cureus | Depresión respiratoria inducida por loperamida en inflamación gastrointestinal grave posquimioterapia, por mayor absorción sistémica. Predicción: gastroduodenitis |

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas monofármaco, ninguna cancelada). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 88777 | Loperamida Opko 2 mg cápsulas duras EFG | Cápsula dura | No disponible |
| 89192 | Loperamida Grindeks 2 mg cápsulas duras | Cápsula dura | No disponible |
| 36747 | Salvacolina 0,2 mg/ml solución oral | Solución oral | No disponible |
| 9091IP | Fortasec Flas 2 mg liofilizado oral | Liofilizado oral | No disponible |
| 67219 | Diarfin 2 mg cápsulas duras | Cápsula dura | No disponible |

Otras presentaciones incluyen comprimidos, comprimidos bucodispersables y liofilizados orales. Todas las formas disponibles son de **administración oral**; no hay formulación oftálmica, lo que supondría un obstáculo adicional para la indicación predicha.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, íleo paralítico, obstrucción intestinal, miopatía visceral familiar, disentería, enfermedad diarreica infecciosa y enfermedad infecciosa intestinal.
- **Señales de la literatura:** en disentería invasiva, los antimotilidad pueden empeorar la evolución (caso de colitis amebiana fulminante). Con la barrera intestinal comprometida puede aumentar la absorción sistémica y producirse depresión respiratoria.
- **Interacciones farmacológicas:** la consulta se completó y solo registró la interacción farmacológica con su diana, el receptor opioide mu (OPRM1); no se identificaron interacciones con otros fármacos.

Consultar el prospecto para información de seguridad completa, ya que las advertencias y contraindicaciones oficiales no están disponibles.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para conjuntivitis contagiosa aguda es exclusivamente computacional (L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible; además, el fármaco solo existe en formas orales. Las demás predicciones del listado tampoco cuentan con evidencia de eficacia, y las pocas publicaciones disponibles señalan riesgos.

**Para avanzar se necesita:**
- Datos de mecanismo de acción y una hipótesis biológica que justifique un efecto en la superficie ocular
- Estudios preclínicos (in vitro o en modelos animales) de actividad en conjuntivitis
- Evaluación de la viabilidad de una formulación oftálmica
- Obtención y análisis del prospecto de la AEMPS (advertencias y contraindicaciones oficiales), pendiente para el cribado de seguridad
- Revisión de la similitud con las indicaciones originales y de la compatibilidad de vías de administración
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

