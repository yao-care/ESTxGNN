---
layout: default
title: Fluocinonide
parent: Solo predicción del modelo (L5)
nav_order: 342
evidence_level: L5
indication_count: 7
---

# Fluocinonide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Fluocinonida: De Dermatosis Inflamatorias y Pruriginosas a Alopecia Mucinosa

## Resumen en Una Frase

Fluocinonida es un corticosteroide tópico de alta potencia, utilizado originalmente para tratar afecciones inflamatorias y pruriginosas de la piel, como la dermatitis atópica, la dermatitis de contacto y la dermatitis seborreica.
El modelo TxGNN predice que podría ser efectivo para **alopecia mucinosa**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se apoya únicamente en el puntaje del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dermatosis inflamatorias y pruriginosas de la piel (la ficha de la autorización no incluye texto de indicación; se toma de las indicaciones del grafo de conocimiento: dermatitis atópica, de contacto, seborreica, etc.) |
| Nueva Indicación Predicha | Alopecia mucinosa |
| Puntaje de Predicción TxGNN | 99,61 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, la fluocinonida es un corticosteroide tópico de alta potencia que actúa sobre el receptor de glucocorticoides (NR3C1) y ejerce efectos antiinflamatorios e inmunosupresores. Su eficacia en dermatosis inflamatorias está establecida.

La alopecia mucinosa (mucinosis folicular) es un trastorno inflamatorio del folículo piloso. Por ello, existe un vínculo mecanístico plausible: reducir la inflamación folicular local mediante un corticosteroide tópico. Aun así, este vínculo se basa solo en la predicción de TxGNN y en un razonamiento general; no hay estudios que lo hayan comprobado con fluocinonida.

Otras predicciones del modelo (efluvio telógeno, alopecia areata, foliculitis decalvante y varios síndromes genéticos raros) muestran puntajes similares. Algunas tienen una relación mecanística débil, como el efluvio telógeno (generalmente no inflamatorio) o los síndromes genéticos del desarrollo capilar. Esto sugiere cautela al interpretar el puntaje por sí solo. La alopecia areata, de base autoinmune, es la que presenta un vínculo biológico más plausible, aunque con evidencia solo indirecta.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para alopecia mucinosa.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para alopecia mucinosa.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 54036 | NOVOTER 0,5 MG/G CREMA (Teofarma S.R.L.) | Crema | No se dispone del texto de indicación |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (no provienen del prospecto): hiperglucemia, diabetes mellitus, cetoacidosis diabética, síndrome de Cushing e hiperfunción de la glándula suprarrenal, así como diversas deficiencias hipofisarias (hipopituitarismo, déficit de hormona del crecimiento, hipogonadismo hipogonadotrópico, síndrome de Kallmann, síndrome de Sheehan) y enfermedad del timo.
- **Interacciones farmacológicas**: solo se identificó la interacción farmacológica con el receptor de glucocorticoides (NR3C1), que es su diana terapéutica; no hay interacciones con otros fármacos documentadas.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, ya que no se dispone de ellas en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para alopecia mucinosa tiene un puntaje alto (99,61 %), pero no cuenta con ensayos clínicos ni literatura (nivel L5). El vínculo mecanístico es plausible, pero no está verificado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales), pues su ausencia impide completar el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisión de la literatura sobre corticosteroides tópicos en mucinosis folicular (series de casos, informes publicados).
- Evaluar la compatibilidad de la vía de administración (crema tópica) con la localización de las lesiones, por ejemplo, el cuero cabelludo.
- Si se desea priorizar otra indicación, la alopecia areata (nivel L4, evidencia solo indirecta) podría ser una pregunta de investigación más fundamentada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

