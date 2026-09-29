---
layout: default
title: Phenobarbital
parent: Solo predicción del modelo (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Phenobarbital
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

# Fenobarbital: De Epilepsia (Crisis Convulsivas) a Neoplasia del Nervio Trigémino

## Resumen en Una Frase

Fenobarbital es un barbitúrico antiepiléptico, utilizado para tratar casi todos los tipos de crisis convulsivas, salvo las crisis de ausencia.
El modelo TxGNN predice que podría ser efectivo para **Neoplasia del Nervio Trigémino**, pero **no hay ensayos clínicos** y solo **1 publicación** (una serie de casos sobre otra enfermedad), por lo que la predicción carece de respaldo real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Crisis epilépticas, excepto ausencias (dato farmacológico; los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, fenobarbital es un modulador alostérico positivo del receptor GABA-A. Su eficacia como antiepiléptico está comprobada. Además, se une al receptor X de pregnano (PXR, gen NR1I2), que regula la inducción de enzimas hepáticas.

**La predicción no parece razonable desde el punto de vista mecanístico.** Fenobarbital no tiene actividad antitumoral conocida. Inhibir la actividad neuronal por vía GABAérgica no se relaciona con el control del crecimiento de un tumor del nervio trigémino. El puntaje alto (99.96%) probablemente refleja la cercanía en el grafo de conocimiento con nodos relacionados con crisis convulsivas, y no un mecanismo oncológico.

La única publicación recuperada trata sobre el síndrome de Sturge-Weber, una enfermedad neurocutánea que cursa con epilepsia. Esto refuerza la idea de que la asociación viene de la epilepsia y no de un efecto sobre tumores.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie de casos | Anales españoles de pediatría | Revisión de 14 casos de síndrome de Sturge-Weber seguidos durante 25 años (características clínicas, evolución y respuesta terapéutica). No aporta evidencia sobre actividad antitumoral de fenobarbital. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 35052 | LUMINAL 100 MG COMPRIMIDOS | Comprimido | Kern Pharma S.L. |
| 3275 | LUMINALETAS 15 MG COMPRIMIDOS | Comprimido | Kern Pharma S.L. |
| 49002 | GARDENAL 50 mg COMPRIMIDOS | Comprimido | Sanofi Aventis S.A. |
| 3905 | LUMINAL 200 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | Kern Pharma S.L. |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó con un único registro, y es farmacológico, no una interacción con otro fármaco. Fenobarbital actúa sobre el receptor X de pregnano (PXR/NR1I2), una vía asociada a la inducción enzimática. Esto sugiere vigilar la exposición de otros medicamentos metabolizados por el hígado.

Consultar el prospecto para información de advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos, la única publicación no se relaciona con tumores y no hay un vínculo mecanístico plausible. El puntaje del modelo es el único sustento de esta predicción.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS para completar las advertencias y contraindicaciones.
- Obtener el mecanismo de acción desde DrugBank.
- Considerar que otras predicciones del mismo fármaco son más plausibles y merecen revisión prioritaria. Se trata de epilepsias reflejas (convulsiones por comer, por sobresalto, por sonido, por lectura), con nivel L4, además de la neuralgia del trigémino. En esta última, el fármaco de referencia es la carbamazepina y fenobarbital actúa sobre todo como medicación concomitante que reduce sus niveles.
- Solo se justificaría reabrir la neoplasia del nervio trigémino si aparece evidencia preclínica o clínica directa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

