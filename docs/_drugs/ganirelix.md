---
layout: default
title: Ganirelix
parent: Solo predicción del modelo (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Ganirelix
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

# Ganirelix: De Inhibición de Picos Prematuros de LH en Reproducción Asistida (FIV) a Hipertricosis

## Resumen en Una Frase

Ganirelix es un antagonista del receptor de GnRH, comercializado en España para ciclos de fecundación in vitro (FIV), donde suprime la hormona luteinizante (LH) y la hormona foliculoestimulante (FSH).
El modelo TxGNN predice que podría ser efectivo para **hipertricosis**, pero **no existe ningún ensayo clínico ni publicación** que respalde esta predicción, y no se identifica un vínculo biológico plausible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ciclos de FIV (supresión de picos prematuros de LH). Los textos de indicación de las autorizaciones españolas están vacíos; este dato procede del análisis de la predicción |
| Nueva Indicación Predicha | Hipertricosis |
| Puntaje de Predicción TxGNN | 99,98 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Ganirelix es un antagonista del receptor de GnRH: bloquea la señal hipotalámica en la hipófisis, reduce la secreción de LH y FSH y, con ello, los esteroides sexuales de origen gonadal. El campo de mecanismo de acción de DrugBank no está disponible en el Evidence Pack, por lo que esta descripción se basa en la clase farmacológica conocida.

**La predicción no tiene un respaldo biológico claro.** La hipertricosis no suele depender del eje hipófiso-gonadal, y el puntaje tan alto (0,9998) refleja únicamente la cercanía en el grafo de conocimiento, no un efecto demostrado. No hay ensayos, literatura ni un vínculo mecanístico identificado.

Las demás predicciones del modelo tampoco ofrecen respaldo clínico. La única biológicamente coherente es **pubertad precoz central** (puntaje 99,75 %, posición 9): el fármaco suprime directamente el eje. Aun así, los agonistas de GnRH de acción prolongada son el tratamiento estándar, ganirelix es de acción corta y tampoco hay evidencia clínica. Se considera una hipótesis para revisión farmacológica o preclínica, no una recomendación clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 78205 | FYREMADEL 0,25 MG / 0,5 ML solución inyectable en jeringa precargada EFG | Solución inyectable |
| 1221658001 | GANIRELIX GEDEON RICHTER 0,25 MG/0,5 ML solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada |
| 86368 | ASTARTE 0,25 MG/0,5 ML solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada |
| 00130001 | ORGALUTRAN 0,25 MG/0,5 ML solución inyectable | Solución inyectable en jeringa precargada |
| 00130002 | ORGALUTRAN 0,25 MG/0,5 ML solución inyectable | Solución inyectable en jeringa precargada |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y sin vínculo mecanístico plausible entre el antagonismo de GnRH y la hipertricosis. Los datos de seguridad tampoco están disponibles, por lo que no se puede avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias y contraindicaciones), que es un vacío bloqueante.
- Completar el mecanismo de acción desde DrugBank.
- Justificar biológicamente el vínculo con hipertricosis; de lo contrario, descartar la predicción.
- Reorientar la revisión hacia pubertad precoz central como pregunta de investigación, con revisión farmacológica o preclínica previa.
- Tratar con cautela el número de publicaciones de otras predicciones del modelo (p. ej., el síndrome de malformación con componente periodontal): son literatura genérica sobre periodontitis que no menciona ganirelix y no constituye evidencia.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

