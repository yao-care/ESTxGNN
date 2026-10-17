---
layout: default
title: Roxadustat
parent: Solo predicción del modelo (L5)
nav_order: 715
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Roxadustat: nueva indicación predicha, Síndrome del ojo seco (nivel de evidencia L5). Indicación original: Anemia refractaria (según el grafo de conocimiento"
monitor_inn: "ROXADUSTAT"
predicted_indications: ["dry eye syndrome", "bone Paget disease", "dentinogenesis imperfecta", "squamous cell carcinoma"]
---

# Roxadustat
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Roxadustat: De Anemia Refractaria a Síndrome del Ojo Seco

## Resumen en Una Frase

Roxadustat es un inhibidor de la prolil hidroxilasa del factor inducible por hipoxia (HIF-PH), utilizado originalmente para el tratamiento de la anemia refractaria (en Europa, la anemia asociada a la enfermedad renal crónica).
El modelo TxGNN predice que podría ser efectivo para **síndrome del ojo seco**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anemia refractaria (según el grafo de conocimiento; el texto de indicación autorizado no está disponible en los datos compilados) |
| Nueva Indicación Predicha | Síndrome del ojo seco |
| Puntaje de Predicción TxGNN | 99.51% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Roxadustat inhibe las prolil hidroxilasas del HIF (EGLN1-3), lo que estabiliza HIF-1α/2α e incrementa la eritropoyetina endógena. Los datos compilados no incluyen una descripción detallada del mecanismo de acción original, por lo que este razonamiento se basa en el conocimiento general de la clase farmacológica.

La relación con el ojo seco es especulativa. La activación de HIF podría modular la inflamación de la superficie ocular, la respuesta al estrés hipóxico y la reparación epitelial. Sin embargo, no existe evidencia clínica ni bibliográfica que lo confirme, y el sentido del efecto (beneficioso o perjudicial) es incierto.

El puntaje TxGNN (0.995) es una predicción computacional y no sustituye a la evidencia experimental. La similitud mecanística con la indicación original (anemia) aún está pendiente de análisis.

### Otras predicciones del modelo (para contexto)

| Rango | Indicación Predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|------|
| 2 | Enfermedad de Paget ósea | 99.12% | L5 | HIF influye en el remodelado óseo, pero el sentido del efecto es incierto |
| 3 | Dentinogénesis imperfecta | 99.06% | L5 | Sin vía mecanística clara; probable artefacto de proximidad en la red |
| 4 | Carcinoma de células escamosas | 99.02% | L5 | La estabilización de HIF podría favorecer el crecimiento tumoral: preocupación de seguridad |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1211574001 | EVRENZO 20 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 1211574002 | EVRENZO 50 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 1211574003 | EVRENZO 70 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 1211574004 | EVRENZO 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 1211574005 | EVRENZO 150 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

Todas las autorizaciones están vigentes, corresponden a monofármaco y su titular es Astellas Pharma Europe B.V.

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificó una entrada de interacción de tipo farmacológico, que corresponde a la diana de roxadustat (la prolil hidroxilasa EGLN2, familia egl-9 del factor inducible por hipoxia) y no a una interacción con otro fármaco. No se dispone de nivel de gravedad.
- **Preocupación específica de la predicción de carcinoma escamoso**: la estabilización de HIF podría, en teoría, favorecer la progresión tumoral, por lo que cualquier uso en contextos oncológicos requeriría una evaluación preclínica cuidadosa.

Consultar el prospecto para información sobre advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para síndrome del ojo seco tiene un puntaje alto en TxGNN, pero carece por completo de ensayos clínicos y literatura (nivel L5), y el vínculo mecanístico es especulativo.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), actualmente un vacío bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Realizar una revisión sistemática de la literatura sobre HIF-PH y superficie ocular
- Estudios preclínicos en modelos de ojo seco que establezcan el sentido del efecto
- Evaluar la compatibilidad de la vía de administración (la forma oral actual no es la habitual para una indicación ocular; probablemente se requeriría una formulación tópica oftálmica)
- Evaluar la seguridad oncológica derivada de la estabilización de HIF
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

