---
layout: default
title: Cabotegravir
parent: Solo predicción del modelo (L5)
nav_order: 131
evidence_level: L5
indication_count: 5
---

# Cabotegravir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Cabotegravir: De Indicación Original No Especificada a Artritis Reumatoide

## Resumen en Una Frase

Cabotegravir es un fármaco antirretroviral comercializado en España (Apretude y Vocabria), cuyo texto de indicación aprobada no figura en los datos compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción: se trata de una predicción exclusivamente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la licencia (el fármaco es un inhibidor de la integrasa del VIH-1) |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 99.45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, cabotegravir es un inhibidor de la transferencia de cadena de la integrasa (INSTI) del VIH-1. Su diana es la integrasa viral, que no tiene homólogo humano implicado en la inflamación articular autoinmune.

Por tanto, **no existe un vínculo mecanístico establecido** entre cabotegravir y la artritis reumatoide. El puntaje alto (0.9945) proviene del grafo de conocimiento y no está respaldado por ningún ensayo ni publicación. La similitud con la indicación original está pendiente de evaluar, así como la compatibilidad de vías de administración.

Otras predicciones del modelo (colangitis esclerosante, bronquitis, síndrome de displasia rizomélica con microftalmia colobomatosa y retinopatía diabética no proliferativa grave) tampoco cuentan con evidencia clínica ni mecanismo plausible, y se mantienen en nivel L5 con recomendación Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1231760002 | APRETUDE 600 MG suspensión inyectable de liberación prolongada | Suspensión inyectable de liberación prolongada | No especificada en los datos |
| 1201481001 | VOCABRIA 30 MG comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |
| 1231760001 | APRETUDE 30 MG comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |
| 1201481003 | VOCABRIA 600 mg suspensión inyectable de liberación prolongada | Suspensión inyectable de liberación prolongada | No especificada en los datos |

Todas las autorizaciones están vigentes, son de monofármaco y pertenecen a Viiv Healthcare B.V.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (7 interacciones de nivel moderado, según DDInter): carbonato de calcio, hidróxido de aluminio, carbonato de magnesio, hidróxido de magnesio, óxido de magnesio, bicarbonato de sodio y citrato de sodio. Todas corresponden a antiácidos o agentes con cationes polivalentes; conviene revisar en el prospecto la pauta de separación de tomas.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es puramente computacional (L5), sin ensayos clínicos ni literatura, y sin vínculo mecanístico plausible entre un inhibidor de la integrasa del VIH y la artritis reumatoide.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), lo que actualmente impide el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Realizar una búsqueda sistemática de literatura y ensayos preclínicos que justifiquen un posible mecanismo en artritis reumatoide
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

