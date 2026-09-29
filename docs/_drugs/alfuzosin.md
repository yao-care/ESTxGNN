---
layout: default
title: Alfuzosin
parent: Solo predicción del modelo (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
---

# Alfuzosin
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

# Alfuzosina: De Hiperplasia Prostática Benigna a Hipertricosis Universal Congénita Tipo Ambras

## Resumen en Una Frase

Alfuzosina es un antagonista de los receptores alfa-1 adrenérgicos, utilizado para facilitar la micción en hombres con hiperplasia prostática benigna.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita tipo Ambras**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción. Es una señal puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperplasia prostática benigna (según el uso clínico registrado en la base farmacológica; los textos de indicación de las autorizaciones españolas vienen vacíos) |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99,999% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 14 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Alfuzosina actúa bloqueando los receptores alfa-1 adrenérgicos (subtipos 1A, 1B y 1D). Al relajar el músculo liso de la próstata y del cuello vesical, mejora el flujo urinario en la hiperplasia prostática benigna. No se dispone de una descripción detallada del mecanismo de acción; solo se conocen estas dianas.

**En este caso la predicción no tiene respaldo mecanístico.** No existe una vía conocida que conecte el bloqueo alfa-1 con el desarrollo del folículo piloso. La hipertricosis de tipo Ambras es un trastorno congénito raro de origen genético. El puntaje alto probablemente refleja la cercanía en el grafo de conocimiento con otros nodos relacionados con la hipertricosis, y debe considerarse un posible artefacto.

Lo mismo ocurre con las otras nueve predicciones del modelo, todas de nivel L5 y sin ensayos ni literatura:

- **Trastornos del pelo:** hipertricosis, anomalía genética aislada del tallo piloso, tricomegalia familiar aislada, hipotricosis simple del cuero cabelludo e hipotricosis congénita con milia.
- **Malformaciones:** síndrome con componente dental o periodontal y síndrome con malformación de Dandy-Walker.
- **Otras:** urticaria alérgica y síndrome de circulación fetal persistente.

La única con cierta plausibilidad biológica es el **síndrome de circulación fetal persistente**. La hipótesis es que la vasodilatación podría reducir la resistencia vascular pulmonar, y un bloqueante alfa antiguo, la tolazolina, se usó en ese contexto. Sin embargo, es otro fármaco y no hay datos de alfuzosina. Además, no existen datos de seguridad ni de dosificación en neonatos, y hay un riesgo real de hipotensión sistémica. Sigue siendo solo una hipótesis.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 14 autorizaciones. Los textos de indicación aprobada no figuran en los datos recibidos, por lo que se omite esa columna.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 67855 | Alfuzosina Ratiopharm 10 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | Teva Pharma S.L.U. |
| 67605 | Alfuzosina Stada 10 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | Laboratorio Stada S.L. |
| 60767 | Benestan Retard 5 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | Sanofi Aventis S.A. |
| 69418 | Alfuzosina Teva-Ratiopharm 10 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | Teva Pharma S.L.U. |
| 67764 | Alfuzosina Sandoz 10 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | Sandoz Farmacéutica S.A. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Las advertencias y contraindicaciones de la ficha técnica de la AEMPS aún no se han incorporado. Las tres entradas del apartado de interacciones corresponden a las dianas farmacológicas de alfuzosina (ADRA1A, ADRA1B y ADRA1D), no a interacciones con otros fármacos.

Para la única hipótesis con cierta plausibilidad (circulación fetal persistente), un bloqueante alfa-1 conlleva riesgo de hipotensión sistémica en neonatos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las diez predicciones son de nivel L5: no hay ensayos clínicos, literatura ni mecanismo plausible. Los puntajes altos parecen deberse a vecindad en el grafo entre nodos relacionados con el pelo, más que a evidencia independiente.

**Para avanzar se necesita:**
- Un vínculo mecanístico plausible entre el bloqueo alfa-1 y la nueva indicación, antes de cualquier estudio.
- Búsqueda sistemática en literatura y registros de ensayos para confirmar la ausencia de evidencia.
- Descargar y analizar la ficha técnica de la AEMPS (advertencias y contraindicaciones), que es un bloqueo para el cribado de seguridad.
- Datos del mecanismo de acción desde DrugBank.
- Si se quiere explorar la circulación fetal persistente, datos de seguridad y dosificación neonatal, y una revisión de si el uso de bloqueantes alfa es aplicable a alfuzosina.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

