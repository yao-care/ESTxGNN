---
layout: default
title: Vinpocetine
parent: Evidencia moderada (L3-L4)
nav_order: 563
evidence_level: L4
indication_count: 7
---

# Vinpocetine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

# Vinpocetina: De Trastornos Cerebrovasculares a Enfermedad de la Arteria Coronaria

## Resumen en Una Frase

La vinpocetina es un fármaco comercializado en España en comprimidos, que según la farmacología de referencia se utiliza en trastornos cerebrovasculares y en el deterioro de memoria asociado a la edad.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad de la arteria coronaria**,
pero actualmente **no hay ensayos clínicos registrados** y solo **3 publicaciones** indirectas (una revisión, un estudio preclínico y un estudio hemodinámico pequeño de 1988) respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en las autorizaciones de AEMPS; la farmacología de referencia indica trastornos cerebrovasculares y deterioro de memoria asociado a la edad |
| Nueva Indicación Predicha | Enfermedad de la arteria coronaria |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro suministrado. Los datos farmacológicos disponibles indican que la vinpocetina actúa sobre las fosfodiesterasas PDE1A y PDE1C humanas. Según el conocimiento general de farmacología (no procede del registro), también se describe como vasodilatador cerebral, con bloqueo de canales de sodio dependientes de voltaje y actividad antiinflamatoria (vía IKK).

Mecanísticamente, aumentar los niveles de cAMP/cGMP podría mejorar el tono vascular y el flujo sanguíneo en enfermedad aterosclerótica. Por eso es plausible que un fármaco usado en enfermedad cerebrovascular se explore en enfermedad coronaria, ya que ambas comparten un sustrato vascular aterosclerótico.

Este vínculo es solo una hipótesis. La literatura de apoyo es indirecta y no hay datos de resultados coronarios ni ensayos registrados. El puntaje alto de TxGNN refleja proximidad en el grafo de conocimiento, no evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17631470](https://pubmed.ncbi.nlm.nih.gov/17631470/) | 2007 | Revisión | Orvosi Hetilap | Revisa el papel de la vinpocetina en enfermedades cerebrovasculares a partir de estudios en humanos; destaca el beneficio de aumentar el flujo sanguíneo cerebral en hipoperfusión crónica |
| [15377497](https://pubmed.ncbi.nlm.nih.gov/15377497/) | 2005 | Preclínico | Am J Physiol Lung Cell Mol Physiol | Inhibidores de PDE de cAMP potencian el efecto de análogos de prostaciclina en el remodelado vascular pulmonar hipóxico; relevancia indirecta para la vinpocetina |
| [3188457](https://pubmed.ncbi.nlm.nih.gov/3188457/) | 1988 | Estudio clínico pequeño (diseño no especificado) | Vrachebnoe Delo | Efecto de Kavinton (vinpocetina) sobre la hemodinámica y el metabolismo de la adenosina en pacientes con aterosclerosis; sin resumen disponible |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 61827 | VINPOCETINA COVEX 5 mg COMPRIMIDOS | Comprimido | Covex S.A. |
| 85430 | VINPOCETINA COVEX 10 MG COMPRIMIDOS | Comprimido | Covex S.A. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para enfermedad coronaria solo existe evidencia indirecta (una revisión cerebrovascular, un estudio preclínico de PDE y un estudio hemodinámico de 1988), sin ensayos registrados. El nivel es L4 y no justifica avanzar por ahora.

Dentro de las predicciones del modelo, la **isquemia miocárdica** (puntaje 99.90%) cuenta con más respaldo: estudios en animales de 2019 y 2026 que muestran cardioprotección. Es la línea más prometedora para una pregunta de investigación futura.

**Para avanzar se necesita:**
- Prospecto de AEMPS con advertencias, contraindicaciones e indicación aprobada (actualmente sin datos)
- Datos detallados del mecanismo de acción (MOA) desde DrugBank
- Estudios clínicos con desenlaces coronarios y evaluación de seguridad cardíaca específica
- Revisión del contenido de los estudios clínicos antiguos, cuyo diseño y desenlaces no pueden verificarse solo con los títulos

*Este informe es solo para referencia de investigación y no constituye consejo médico. Todo candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

