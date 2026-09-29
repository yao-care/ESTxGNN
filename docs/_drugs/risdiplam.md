---
layout: default
title: Risdiplam
parent: Solo predicción del modelo (L5)
nav_order: 470
evidence_level: L5
indication_count: 1
---

# Risdiplam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Risdiplam: De Atrofia Muscular Espinal a Acné

## Resumen en Una Frase

Risdiplam es un modulador del empalme del pre-ARNm de SMN2, utilizado para la atrofia muscular espinal (AME).
El modelo TxGNN predice que podría ser efectivo para **acné**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es únicamente una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Atrofia muscular espinal (según la descripción del mecanismo; el texto de indicación de las autorizaciones españolas está vacío) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99.45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, risdiplam es un modulador del empalme del pre-ARNm de SMN2 aprobado para la atrofia muscular espinal. No hay una relación mecanística establecida con el acné.

El acné depende de la producción de sebo, la hiperqueratinización folicular, la colonización por *Cutibacterium acnes* y la inflamación. Ninguna de estas vías se conoce como dependiente del empalme de SMN2, y la AME (una enfermedad neuromuscular) y el acné (una enfermedad dermatológica) no comparten una base fisiopatológica evidente.

El puntaje alto de TxGNN (0.995) proviene solo del grafo de conocimiento y no está respaldado por datos clínicos ni bibliográficos. Se han descrito cambios de empalme fuera de diana (por ejemplo, inclusión de exones en genes como FOXM1 y MADD), y en estudios preclínicos aparecieron toxicidades cutáneas y retinianas. Esto son señales de seguridad, no evidencia de beneficio en acné.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1211531002 | EVRYSDI 5 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 1211531001 | EVRYSDI 0,75 mg/ml polvo para solución oral | Polvo para solución oral |

Ambas autorizaciones pertenecen a Roche Registration GmbH.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre la modulación del empalme de SMN2 y el acné. Además, las señales preclínicas de toxicidad cutánea y retiniana no favorecen el uso en una enfermedad de curso benigno.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias y contraindicaciones), que es un vacío bloqueante para el cribado de seguridad
- Completar los datos de mecanismo de acción desde DrugBank
- Identificar estudios preclínicos o de mecanismo que vinculen la vía de SMN2 o los efectos de empalme con la biología del acné
- Evaluar la compatibilidad de vía de administración (actualmente solo formas orales; una indicación dermatológica requeriría justificación)
- Reevaluar solo si aparece evidencia independiente al modelo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

