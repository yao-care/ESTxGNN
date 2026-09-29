---
layout: default
title: Phenytoin
parent: Solo predicción del modelo (L5)
nav_order: 422
evidence_level: L5
indication_count: 10
---

# Phenytoin
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

# Fenitoína: De Epilepsia a Neoplasia del Nervio Trigémino

## Resumen en Una Frase

La fenitoína es un anticonvulsivo bloqueador de canales de sodio dependientes de voltaje, utilizado originalmente para tratar la epilepsia (crisis tónico-clónicas y parciales complejas).
El modelo TxGNN predice que podría ser efectiva para **neoplasia del nervio trigémino**, pero **no hay ensayos clínicos** y las **5 publicaciones** recuperadas tratan de neuralgia del trigémino y síndrome de Sturge-Weber, no de tumores. Esta predicción carece de respaldo real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia (fuente: datos de farmacología; las autorizaciones de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, la fenitoína es un bloqueador de canales de sodio dependiente del uso, y la base de datos de farmacología la vincula con el canal Nav1.2 (gen *SCN2A*). Su eficacia en epilepsia está comprobada.

**Este mecanismo no respalda un efecto antitumoral.** El bloqueo de canales de sodio suprime descargas neuronales anómalas, pero no hay evidencia de actividad antineoplásica. Es probable que el vínculo del modelo provenga de nodos vecinos en el grafo de conocimiento relacionados con el nervio trigémino. La literatura recuperada confirma esta sospecha: habla de neuralgia del trigémino y Sturge-Weber, no de neoplasia.

Como indicación relacionada, la neuralgia del trigémino (predicción n.º 9) sí tiene una justificación mecanística coherente. Se detalla más abajo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revisión | Expert Rev Neurother | Revisión de tratamientos médicos y quirúrgicos de la neuralgia del trigémino. No trata neoplasias. |
| [21751615](https://pubmed.ncbi.nlm.nih.gov/21751615/) | 2011 | Revisión | J Assoc Physicians India | Síndrome de Sturge-Weber (angiomatosis encefalotrigeminal) con crisis epilépticas. No es un tumor. |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie de casos | An Esp Pediatr | Experiencia con 14 casos de Sturge-Weber: características clínicas y respuesta terapéutica. |
| [4155965](https://pubmed.ncbi.nlm.nih.gov/4155965/) | 1971 | Sin clasificar | Birth Defects Orig Artic Ser | Trastornos dermatológicos en personas con discapacidad intelectual institucionalizadas, incluidas reacciones iatrogénicas a fármacos. |
| [5514358](https://pubmed.ncbi.nlm.nih.gov/5514358/) | 1970 | Sin clasificar | Trans Am Neurol Assoc | Tamaño de fibras de la raíz posterior del trigémino y analgesia en neuralgia del trigémino. Sin resumen disponible. |

Ninguna publicación evalúa fenitoína en neoplasia del nervio trigémino.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 56245 | Fenitoína Rubio 50 mg/ml solución inyectable | Solución inyectable |
| 65372 | Fenitoína Altan 50 mg/ml solución inyectable | Solución inyectable |
| 65340 | Fenitoína Kern Pharma 50 mg/ml solución inyectable EFG | Solución inyectable |
| 45695 | Epanutin 100 mg cápsulas duras | Cápsula dura |
| 5970 | Sinergina 100 mg comprimidos | Comprimido |

Hay 6 autorizaciones en total, de las cuales se muestran 5. Los registros no incluyen texto de indicación aprobada.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Otras Indicaciones Predichas con Más Sustento

El modelo devolvió 10 predicciones. La primera es un probable artefacto del grafo. Otras tienen más respaldo:

| Indicación | Puntaje | Nivel | Evidencia disponible | Decisión |
|------|------|------|------|------|
| Neuralgia del trigémino | 99.97% | L3 | Ensayo [NCT03712254](https://clinicaltrials.gov/study/NCT03712254) (completado, 15 pacientes, fenitoína en exacerbaciones agudas). Estudios retrospectivos de fenitoína IV ([32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/), [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/)). ECA de fosfenitoína IV, 2026 ([42096672](https://pubmed.ncbi.nlm.nih.gov/42096672/)). Una revisión ([28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/)) cuestiona su base de evidencia. | Proceed with Guardrails |
| Convulsiones reflejas (por sobresalto, audiógenas, por lectura, por micción, etc.) | 99.97–99.98% | L4–L5 | Solo evidencia preclínica, informes de casos y justificación por efecto de clase. Sin ensayos específicos. | Hold |
| Déficit de beta-cetotiolasa | 99.95% | L5 | Sin ensayos ni literatura. Sin vínculo mecanístico. | Hold |

Para la neuralgia del trigémino, las salvaguardas propuestas son:
- Limitar el uso al rescate agudo.
- Administrar por vía IV con monitorización, por el riesgo cardíaco y de hipotensión.
- Confirmar el lugar actual de la fenitoína en las guías antes de recomendarla.

El ECA de 2026 evaluó fosfenitoína, un profármaco, no fenitoína directamente.

---

## Conclusión y Próximos Pasos

**Decisión: Hold** (para neoplasia del nervio trigémino)

**Justificación:**
No existen ensayos clínicos ni literatura sobre fenitoína en neoplasia del trigémino, y no hay mecanismo antitumoral plausible. El puntaje alto del modelo parece un artefacto del grafo.

**Para avanzar se necesita:**
- Reorientar la evaluación hacia la neuralgia del trigémino, la única indicación con evidencia clínica directa (L3).
- Obtener la ficha técnica de AEMPS para advertencias y contraindicaciones, que hoy no están disponibles.
- Completar el mecanismo de acción desde DrugBank.
- Confirmar la posición de la fenitoína IV en las guías vigentes, por ejemplo la guía de la Academia Europea de Neurología ([30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/)).

*Los resultados son solo para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

