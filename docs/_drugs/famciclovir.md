---
layout: default
title: Famciclovir
parent: Evidencia moderada (L3-L4)
nav_order: 225
evidence_level: L4
indication_count: 9
---

# Famciclovir
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **9** 
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

# Famciclovir: De Antiviral contra Herpesvirus a Neuralgia Postinfecciosa

## Resumen en Una Frase

Famciclovir es un profármaco antiviral que se convierte en penciclovir y actúa contra los herpesvirus. El modelo TxGNN predice que podría ser útil para la **neuralgia postinfecciosa** (neuralgia posherpética), con un puntaje de 99.75%. Actualmente hay **2 ensayos clínicos** relacionados con la enfermedad, pero ninguno evalúa famciclovir, y **no hay publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Neuralgia postinfecciosa (neuralgia posherpética) |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, famciclovir se convierte en penciclovir, que inhibe la ADN polimerasa del virus varicela-zóster (VZV).

La neuralgia posherpética es la complicación más frecuente del herpes zóster, que es una reactivación del VZV. Reducir la replicación viral durante la fase aguda del zóster podría disminuir el daño nervioso y, en teoría, el riesgo de que el dolor persista. Esa es la única base mecanística de la predicción.

Ninguno de los dos ensayos encontrados prueba famciclovir. No hay evidencia directa de que prevenga o trate la neuralgia posherpética. Por eso el respaldo es solo plausibilidad biológica y la predicción del modelo.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | N/A | Desconocido | 140 | Oxicodona temprana durante la fase aguda del herpes zóster para prevenir la neuralgia posherpética. Famciclovir, como mucho, sería tratamiento antiviral de base. |
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | N/A | Aún sin reclutar | 120 | Bloqueo nervioso con bupivacaína liposomal o ropivacaína y radiofrecuencia pulsada para el dolor agudo del herpes zóster. No es un estudio de famciclovir. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Famciclovir figura con 13 autorizaciones. Se muestran las 5 principales. Los datos recibidos no incluyen el texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 61597 | FAMVIR 125 mg comprimidos recubiertos con película | Comprimido recubierto con película | Phoenix Labs Unlimited Company |
| 71964 | FAMCICLOVIR NORMON 250 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorios Normon S.A. |
| 65027 | FAMVIR 500 mg comprimidos recubiertos con película | Comprimido recubierto con película | Phoenix Labs Unlimited Company |
| 76997 | FAMCICLOVIR TECNIGEN 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Tecnimede España Industria Farmacéutica S.A. |
| 77136 | FAMCICLOVIR STADA 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorio Stada S.L. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en un mecanismo antiviral plausible. Los dos ensayos encontrados no evalúan famciclovir y no hay literatura específica. Además, faltan las advertencias y contraindicaciones del prospecto de la AEMPS, un vacío que bloquea el cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar estudios que evalúen famciclovir (u otros antivirales) para prevenir la neuralgia posherpética.
- Si aparece evidencia, definir un diseño de estudio de prevención en herpes zóster agudo.

**Nota:** de las demás predicciones del paquete, solo la varicela tiene evidencia de fase 3 (L1). Esa evidencia corresponde a enfermedad por VZV que se solapa con el uso ya conocido de famciclovir en herpes zóster, por lo que no constituye un reposicionamiento novedoso.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

