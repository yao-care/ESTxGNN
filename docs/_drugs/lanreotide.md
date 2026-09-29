---
layout: default
title: Lanreotide
parent: Solo predicción del modelo (L5)
nav_order: 303
evidence_level: L5
indication_count: 5
---

# Lanreotide
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

# Lanreotida: De Acromegalia a Hipertricosis

## Resumen en Una Frase

Lanreotida es un análogo de la somatostatina que, según la referencia farmacológica disponible, se usa en la acromegalia y en los síntomas de los tumores neuroendocrinos.
El modelo TxGNN predice que podría ser efectivo para **Hipertricosis**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ningún texto de indicación aprobada figura en las autorizaciones de la AEMPS. La referencia farmacológica indica acromegalia y síntomas de tumores neuroendocrinos. |
| Nueva Indicación Predicha | Hipertricosis |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de entrada. Según la información farmacológica, lanreotida es un péptido análogo de la somatostatina que actúa sobre los receptores **SSTR2, SSTR3 y SSTR5**. Su eficacia en acromegalia y tumores neuroendocrinos está establecida.

Mecanísticamente, la única vía plausible es indirecta. Al actuar sobre SSTR2 y SSTR5, lanreotida suprime la señalización de GH/IGF-1, e IGF-1 influye en el ciclo del folículo piloso. Sin embargo, **no existe evidencia directa** que vincule esta vía con la hipertricosis.

El puntaje de 99.97% por sí solo no es evidencia clínica. Probablemente refleja cercanía en el grafo de conocimiento, no un mecanismo demostrado. Las otras cuatro predicciones principales (síndromes malformativos, hipertricosis congénita de tipo Ambras, anomalías genéticas del tallo piloso) tampoco cuentan con ensayos ni literatura relevante. Las 20 publicaciones recuperadas para el síndrome malformativo con componente periodontal tratan de periodontitis en general, no de lanreotida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 64838 | SOMATULINA AUTOGEL 90 mg, solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada |
| 86176 | MYRELEZ 60 mg solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada |
| 90113 | LANREOTIDA SUN 90 mg solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada |
| 90111 | LANREOTIDA SUN 120 mg solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada |
| 60914 | SOMATULINA 30 mg polvo y disolvente para suspensión inyectable de liberación prolongada | Polvo y disolvente para suspensión inyectable de liberación prolongada |

Se muestran 5 de las 10 autorizaciones. Los registros no incluyen el texto de la indicación aprobada.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos, literatura ni mecanismo directo que la sustenten. Además, no se han revisado las advertencias ni contraindicaciones de la ficha técnica, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar la ficha técnica de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar el mecanismo de acción desde DrugBank.
- Buscar estudios preclínicos o series de casos que relacionen análogos de somatostatina o la vía GH/IGF-1 con la hipertricosis.
- Evaluar la compatibilidad de la vía de administración (inyectable) con una indicación dermatológica.
- Reevaluar la decisión solo si aparece evidencia mecanística o clínica directa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

