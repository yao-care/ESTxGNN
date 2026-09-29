---
layout: default
title: Fexofenadine
parent: Solo predicción del modelo (L5)
nav_order: 231
evidence_level: L5
indication_count: 1
---

# Fexofenadine
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

# Fexofenadina: De Alergias Estacionales a Conjuntivitis por Rosácea

## Resumen en Una Frase

Fexofenadina es un antihistamínico que actúa sobre el receptor H1 y se usa para tratar los síntomas de las alergias estacionales y otras afecciones dependientes de la histamina.
El modelo TxGNN predice que podría ser efectivo para la **conjuntivitis por rosácea**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síntomas de alergias estacionales (según datos de farmacología; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Conjuntivitis por rosácea |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información de farmacología disponible, fexofenadina tiene como diana el receptor H1 de histamina (gen HRH1). Por conocimiento farmacológico general, y no por los datos aportados, es un antagonista H1 de selectividad periférica. Su utilidad en alergias estacionales es conocida.

Mecanísticamente, una contribución de la histamina o de los mastocitos a la inflamación de la superficie ocular en la rosácea ocular es plausible. Sin embargo, no está establecida como factor principal y este vínculo no se ha verificado con los datos disponibles.

La conjuntivitis asociada a rosácea suele deberse a disfunción de las glándulas de Meibomio, a *Demodex* y a vías inflamatorias. Por eso un antihistamínico no es una opción evidente. El único respaldo es el puntaje de predicción de TxGNN, que por sí solo no constituye evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 61911 | Fexofenadina Opella 180 mg comprimidos recubiertos con película | Comprimido recubierto con película | Opella Healthcare Spain S.L. |
| 61910 | Telfast 120 mg comprimidos recubiertos con película | Comprimido recubierto con película | Opella Healthcare Spain S.L. |
| 79718 | Fexofenadina Cipla 180 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Cipla Europe N.V. |
| 79726 | Fexofenadina Cipla 120 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Cipla Europe N.V. |
| 89656 | Riniwel 120 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Aurovitas Spain, S.A.U. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un puntaje alto del modelo (99.85%), sin ensayos clínicos ni literatura (nivel L5). El vínculo mecanístico con la conjuntivitis por rosácea es especulativo, y la compatibilidad de vías de administración sigue pendiente.

**Para avanzar se necesita:**
- Obtener del prospecto de la AEMPS las advertencias y contraindicaciones, hoy bloqueantes para el cribado de seguridad
- Completar los datos del mecanismo de acción (por ejemplo, consultando la API de DrugBank)
- Revisar la literatura preclínica y clínica sobre el papel de la histamina y los mastocitos en la rosácea ocular
- Evaluar la compatibilidad de la vía de administración: las autorizaciones actuales son solo comprimidos orales, y una indicación ocular podría requerir otra formulación
- Definir la similitud con la indicación original y, si hay respaldo mecanístico, considerar estudios preclínicos o exploratorios antes de un ensayo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

