---
layout: default
title: Lamotrigine
parent: Solo predicción del modelo (L5)
nav_order: 300
evidence_level: L5
indication_count: 9
---

# Lamotrigine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Lamotrigina: De Epilepsia y Trastorno Bipolar a Neoplasia del Nervio Trigémino

## Resumen en Una Frase

La lamotrigina es un anticonvulsivo utilizado para tratar la epilepsia y el trastorno bipolar.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, pero **no hay ensayos clínicos** ni estudios que respalden un efecto antitumoral. Las 2 publicaciones asociadas tratan sobre la neuralgia del trigémino, no sobre el tumor.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia y trastorno bipolar (según la ficha farmacológica; los textos de indicación de las autorizaciones de la AEMPS vienen vacíos) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la lamotrigina bloquea de forma dependiente del uso los canales de sodio dependientes de voltaje (la ficha farmacológica cita Nav1.2 como diana) y reduce la liberación de glutamato. Esto explica su eficacia comprobada en epilepsia.

**Con la información disponible, la predicción es poco razonable como tratamiento antitumoral.** No existe un mecanismo antineoplásico plausible para este fármaco. El puntaje alto probablemente proviene del nodo vecino "neuralgia del trigémino" en el grafo de conocimiento, donde el bloqueo de canales de sodio sí puede calmar el dolor neuropático.

Un posible beneficio sería el control sintomático del dolor facial, no el tratamiento del tumor. Por eso la señal del modelo debe leerse como una asociación con la neuralgia del trigémino y no como una indicación oncológica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revisión | Expert Rev Neurother | Revisión de los tratamientos médicos y quirúrgicos de la neuralgia del trigémino. Trata el dolor, no el tumor. |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Reporte de caso | Stereotact Funct Neurosurg | Radiocirugía Gamma Knife en un paciente con neuralgia del trigémino causada por una malformación cavernosa. No involucra lamotrigina como tratamiento antitumoral. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 67151 | LAMOTRIGINA SANDOZ 100 mg comprimidos dispersables/masticables EFG | Comprimido masticable y dispersable |
| 67318 | LAMOTRIGINA NORMON 25 mg comprimidos dispersables/masticables EFG | Comprimido masticable y dispersable |
| 64391 | LAMICTAL 2 mg comprimidos masticables/dispersables | Comprimido masticable y dispersable |
| 67320 | LAMOTRIGINA NORMON 100 mg comprimidos dispersables/masticables EFG | Comprimido masticable y dispersable |
| 68645 | LAMOTRIGINA COMBIX 200 mg comprimidos dispersables/masticables EFG | Comprimido masticable y dispersable |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios sobre tumores del nervio trigémino, y no existe un mecanismo antineoplásico plausible. El puntaje del modelo parece reflejar la cercanía con la neuralgia del trigémino, no un efecto antitumoral.

**Para avanzar se necesita:**
- Reorientar la evaluación hacia **neuralgia del trigémino**, la segunda predicción del modelo (99.89%). Allí hay 4 ensayos, entre ellos NCT00913107 (Fase 2/3, completado, n=21, lamotrigina vs. carbamazepina) y NCT00203229 (doble ciego, controlado con placebo, completado, n=20). Las revisiones la sitúan como alternativa o terapia adicional. Con nivel L2 y decisión "Proceed with Guardrails", es la línea con más respaldo. Las precauciones serían titulación lenta por el riesgo de erupción cutánea/síndrome de Stevens-Johnson y revisar las interacciones con valproato y estrógenos.
- Obtener los resultados publicados de esos ensayos, ya que el paquete no los incluye.
- Completar los datos de seguridad (advertencias y contraindicaciones del prospecto de la AEMPS) y el mecanismo de acción detallado, que hoy no están disponibles.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

