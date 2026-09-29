---
layout: default
title: Prilocaine
parent: Solo predicción del modelo (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
---

# Prilocaine
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

# Prilocaína: De Anestesia Local a Conjuntivitis Papilar

## Resumen en Una Frase

La prilocaína es un anestésico local de tipo amida (bloqueador de canales de sodio), comercializado en España como solución inyectable. El modelo TxGNN predice que podría ser efectiva para **conjuntivitis papilar**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción: es solo una inferencia del grafo de conocimiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el registro de AEMPS (uso como anestésico local) |
| Nueva Indicación Predicha | Conjuntivitis papilar |
| Puntaje de Predicción TxGNN | 99.78% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, la prilocaína es un anestésico local de tipo amida que bloquea los canales de sodio dependientes de voltaje en las fibras nociceptivas, y su eficacia como anestésico local está bien establecida.

La relación con la conjuntivitis papilar es débil. Esta enfermedad tiene un origen alérgico o mecánico (por ejemplo, lentes de contacto), y los datos disponibles no muestran un vínculo terapéutico plausible con el bloqueo de canales de sodio. El puntaje alto (0.998) probablemente refleja la topología del grafo de conocimiento y no una relación biológica demostrada.

Hasta que se aporte evidencia clínica o mecanística, esta predicción debe tratarse como una hipótesis sin respaldo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 70932 | TAKIPRIL HIPERBARICA 20 MG/ML SOLUCION INYECTABLE (B Braun Medical S.A.) | Solución inyectable | No especificada en el registro |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para conjuntivitis papilar es solo del modelo (nivel L5): no tiene ensayos, literatura ni un vínculo mecanístico plausible con un bloqueador de canales de sodio.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y del prospecto de AEMPS (advertencias y contraindicaciones)
- Evidencia preclínica o clínica que conecte la prilocaína con la patología de la conjuntivitis papilar
- Evaluación de la compatibilidad de vía de administración (la autorización actual es inyectable, no oftálmica)

**Nota sobre otras predicciones del mismo paquete:** la señal más fuerte no es la de la predicción principal, sino la de **neuralgia** (puntaje 99.34%, nivel L3, recomendación "Research Question"). Se apoya en varias publicaciones de 1989 a 1999 sobre la mezcla lidocaína/prilocaína (EMLA) en neuralgia posherpética y en un ensayo de Fase 2 abierto (NCT00916942, n=20). Esa evidencia es pequeña y no confirmada como ensayos aleatorizados, así que conviene evaluarla en un informe aparte. La predicción de **eccema atópico** debe leerse como una alerta de seguridad (metahemoglobinemia, convulsiones y púrpura en piel con barrera alterada) y no como una señal de reposicionamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

