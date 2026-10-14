---
layout: default
title: Prilocaine
parent: Solo predicción del modelo (L5)
nav_order: 662
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

# Prilocaína: De Eyaculación Precoz a Papilar Conjuntivitis (Conjuntivitis Papilar)

## Resumen en Una Frase

Prilocaína es un anestésico local de tipo amida, cuyas indicaciones originales en el grafo de conocimiento son la eyaculación precoz y la dispareunia psicológica.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis papilar**, pero no hay **ningún ensayo clínico** ni **ninguna publicación** que respalde esta dirección, por lo que se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Eyaculación precoz; dispareunia psicológica (según el grafo de conocimiento; el texto de indicación de la autorización de AEMPS no está disponible) |
| Nueva Indicación Predicha | Conjuntivitis papilar |
| Puntaje de Predicción TxGNN | 99.78% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la prilocaína es un anestésico local que bloquea los canales de sodio dependientes de voltaje, y su eficacia como anestésico (solo o en la mezcla eutéctica con lidocaína, EMLA) está bien establecida.

La relación con la conjuntivitis papilar es débil y especulativa. Se trata de una enfermedad inflamatoria/alérgica de la conjuntiva, y no existe una justificación farmacológica clara que vincule el bloqueo de canales de sodio con su tratamiento. El puntaje alto de TxGNN refleja probablemente similitud en la red del grafo y no evidencia clínica.

Por ello, esta predicción debe considerarse solo una hipótesis de partida. Hay otras predicciones del modelo con más respaldo (ver nota más abajo).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 70932 | TAKIPRIL HIPERBÁRICA 20 MG/ML SOLUCIÓN INYECTABLE (B Braun Medical S.A.) | Solución inyectable | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (no provienen del prospecto): hipertensión, epilepsia, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, diabetes mellitus y cetoacidosis diabética, enfermedad coronaria e infarto de miocardio, hemoglobinopatía, parada cardíaca súbita, enfermedad del sistema de conducción cardíaco y bloqueo auriculoventricular, insuficiencia respiratoria, glaucoma de ángulo cerrado, miastenia gravis y enfermedades de la unión neuromuscular, deficiencia de butirilcolinesterasa, enfermedad cardiovascular, hipertiroidismo, enfermedad de Graves y tirotoxicosis.
- **Interacciones farmacológicas** (22 registradas; se listan las principales): interacciones de nivel **mayor** con metoclopramida, sulfasalazina, nitrito de amilo, rasburicasa, ácido nitroso, cloroquina, primaquina, quinina, tafenoquina, lidocaína (sistémica y tópica), benzocaína tópica, óxido nítrico, dapsona (sistémica y tópica), cinocaína tópica, nitrato de plata tópico y sulfadiazina argéntica tópica. Con nivel **moderado**: morfina liposomal. Con nivel **menor**: hialuronidasa. Muchas de estas combinaciones se asocian al riesgo de metahemoglobinemia.
- **Señales de seguridad en la literatura**: hay casos de metahemoglobinemia y convulsiones tras aplicar EMLA en un niño con dermatitis atópica, mayor absorción sistémica en piel con barrera alterada, y casos de alergia de contacto a la prilocaína.

Las advertencias y contraindicaciones del prospecto de AEMPS no están disponibles en los datos compilados; consultar el prospecto para confirmarlas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha (conjuntivitis papilar) solo tiene respaldo del modelo (L5), sin ensayos ni publicaciones y sin un mecanismo plausible. Además, el perfil de seguridad (riesgo de metahemoglobinemia y de toxicidad sistémica) exige cautela.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar estudios preclínicos o una revisión de literatura que justifique un vínculo entre la prilocaína y la conjuntivitis papilar.
- Evaluar la compatibilidad de la vía de administración (oftálmica frente a la inyectable autorizada).

**Nota sobre otras predicciones:** entre las candidatas de mayor rango, la **neuralgia** (puntaje 99.34%, nivel L3) es la que cuenta con más respaldo: un ensayo de Fase 2 abierto (n=20) con crema de lidocaína/prilocaína y estudios antiguos en neuralgia posherpética. La evidencia es pequeña y confundida por el componente de lidocaína, por lo que podría explorarse como pregunta de investigación. El resto de las predicciones no tiene evidencia terapéutica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

