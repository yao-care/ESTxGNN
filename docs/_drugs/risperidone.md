---
layout: default
title: Risperidone
parent: Solo predicción del modelo (L5)
nav_order: 471
evidence_level: L5
indication_count: 6
---

# Risperidone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Risperidona: De Esquizofrenia a Parálisis Horizontal de la Mirada Familiar con Escoliosis Progresiva

## Resumen en Una Frase

La risperidona es un antipsicótico atípico, utilizado originalmente para tratar la esquizofrenia, los episodios maníacos del trastorno bipolar y la irritabilidad asociada al autismo.
El modelo TxGNN predice que podría ser efectiva para la **parálisis horizontal de la mirada familiar con escoliosis progresiva**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia, episodios maníacos del trastorno bipolar e irritabilidad en el autismo (según datos farmacológicos; los textos de indicación de las autorizaciones de AEMPS no están disponibles) |
| Nueva Indicación Predicha | Parálisis horizontal de la mirada familiar con escoliosis progresiva |
| Puntaje de Predicción TxGNN | 99,76 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La risperidona actúa como antagonista de varios receptores. Los datos farmacológicos disponibles indican que se une a receptores dopaminérgicos (D2, D3), serotoninérgicos (5-HT1A, 1B, 1D, 1E, 1F, 2A, 2C, 6 y 7), adrenérgicos (α1A, α1B, α1D, α2A) e histaminérgicos (H1). Su efecto antipsicótico se atribuye sobre todo al bloqueo combinado de D2 y 5-HT2A. No se dispone de una descripción detallada del mecanismo de acción en el paquete de evidencia, por lo que este resumen se basa solo en los blancos farmacológicos listados.

**No se identificó un vínculo mecanístico plausible** con la nueva indicación. La parálisis horizontal de la mirada familiar con escoliosis progresiva es un trastorno genético raro del desarrollo del troncoencéfalo (guía axonal), y es poco probable que responda al antagonismo D2/5-HT2A. El puntaje TxGNN (99,76 %) proviene únicamente de la predicción del grafo de conocimiento y no está respaldado por estudios reales.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 68798 | RISPERIDONA STADA 1 mg/ml solución oral EFG | Solución oral |
| 81426 | RISPERIDONA AUROVITAS 1 mg/ml solución oral EFG | Solución oral |
| 71473 | RISPERIDONA VIATRIS 1 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 71095 | RISPERIDONA FLAS KRKA 1 mg comprimidos bucodispersables EFG | Comprimido bucodispersable |
| 70226 | RISPERIDONA CODRAMOL 1 mg/ml solución oral EFG | Solución oral |

El texto de la indicación aprobada no figura en los registros de estas autorizaciones. Se muestran 5 de las 20 autorizaciones totales.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5): no hay ensayos, no hay literatura y no se identificó un vínculo mecanístico plausible. Un puntaje alto de TxGNN no basta para avanzar.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que sigue pendiente y bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción y de la indicación original desde DrugBank y el etiquetado.
- Una justificación biológica que conecte el antagonismo D2/5-HT2A con la fisiopatología de la enfermedad, antes de cualquier reevaluación.

**Nota sobre otras predicciones del mismo paquete:** este medicamento tiene otras candidatas con más respaldo que la evaluada aquí. La más sólida es el **trastorno afectivo mayor** (L1, "Proceed with Guardrails"), con varios ensayos de Fase 3 completados y metaanálisis de aumento con antipsicóticos de segunda generación. Le siguen la **tricotilomanía** y el **síndrome de Phelan-McDermid** (ambas L4, "Research Question"). Se recomienda priorizarlas para un informe propio.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

