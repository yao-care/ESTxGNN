---
layout: default
title: Vildagliptin
parent: Solo predicción del modelo (L5)
nav_order: 558
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptina: De Diabetes Mellitus Tipo 2 a Síndrome de la Persona Rígida Clásico

## Resumen en Una Frase

La vildagliptina es un inhibidor de la dipeptidil peptidasa-4 (DPP-4), utilizado en el manejo de la diabetes tipo 2.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de la persona rígida clásico**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus tipo 2 (según los datos de farmacología; el texto de indicación de la AEMPS no está disponible) |
| Nueva Indicación Predicha | Síndrome de la persona rígida clásico |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información conocida, la vildagliptina es un inhibidor de DPP-4. Los datos de farmacología la vinculan con las dianas DPP4, DPP8, DPP9 y TRPV4. Su eficacia en la diabetes tipo 2 está comprobada. Mecanísticamente, su aplicabilidad al síndrome de la persona rígida es solo especulativa.

El único vínculo concebible es el solapamiento autoinmune con la diabetes tipo 1 positiva para GAD65, ya que el síndrome de la persona rígida también se asocia a anticuerpos anti-GAD. Es una hipótesis sin respaldo directo: no se ha establecido ningún mecanismo por el cual inhibir DPP-4 mejore la rigidez muscular o los espasmos.

El puntaje del modelo es idéntico al de la forma focal (síndrome de la extremidad rígida focal), lo que sugiere que ambas comparten vecindad en el grafo de conocimiento. Esto indica una asociación estadística del modelo, no evidencia terapéutica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones registradas. El texto de indicación aprobada no está disponible en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 86670 | Vildagliptina Vir 50 mg comprimidos EFG | Comprimido | Industria Química y Farmacéutica Vir S.A. |
| 07414005IP1 | Galvus 50 mg comprimidos | Comprimido | Novartis Europharm Limited |
| 83995 | Vildagliptina Teva 50 mg comprimidos EFG | Comprimido | Teva B.V. |
| 86303 | Vildagliptina Pensa 50 mg comprimidos EFG | Comprimido | Towa Pharmaceutical S.A. |
| 07414005IP2 | Galvus 50 mg comprimidos | Comprimido | Novartis Europharm Limited |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no se identificaron interacciones entre fármacos. Los 4 registros de la consulta corresponden a dianas farmacológicas de la vildagliptina: DPP4, DPP8, DPP9 y TRPV4.
- **Señal de seguridad de la clase**: la literatura recuperada para otra indicación predicha incluye un reporte de caso de pancreatitis aguda probablemente asociada a vildagliptina (PMID 42539684). La relación entre los inhibidores de DPP-4 y la pancreatitis sigue siendo controvertida.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos, sin literatura y sin un mecanismo plausible establecido. El puntaje alto refleja probablemente la vecindad en el grafo de conocimiento, no relevancia terapéutica.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de la AEMPS para advertencias y contraindicaciones.
- Obtener datos del mecanismo de acción desde DrugBank.
- Buscar evidencia preclínica o mecanística que vincule la inhibición de DPP-4 con el síndrome de la persona rígida y la autoinmunidad anti-GAD.
- Considerar priorizar otra indicación del mismo paquete: la **diabetes mellitus tipo 1** (posición 10, puntaje 99.37%, nivel L2). Cuenta con el ensayo de Fase 2 [NCT02803892](https://clinicaltrials.gov/study/NCT02803892) y con el ECA [PMID 33124663](https://pubmed.ncbi.nlm.nih.gov/33124663/) (rapamicina más vildagliptina en diabetes tipo 1 de larga evolución), lo que la convierte en una línea de investigación mucho más sólida.

*Los resultados son solo para referencia de investigación y no constituyen consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

