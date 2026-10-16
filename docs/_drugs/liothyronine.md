---
layout: default
title: Liothyronine
parent: Solo predicción del modelo (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Liothyronine: nueva indicación predicha, Hipodisplasia/aplasia renal (nivel de evidencia L5). Indicación original: No disponible en la ficha de AEMPS (el texto de indicación está vacío…"
---

# Liothyronine
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

# Liotironina: De Hipotiroidismo a Hipodisplasia/Aplasia Renal

## Resumen en Una Frase

La liotironina (triyodotironina, T3) es una hormona tiroidea sintética, utilizada originalmente para tratar el hipotiroidismo y otras enfermedades de la tiroides, como el bocio.
El modelo TxGNN predice que podría ser efectiva para **hipodisplasia/aplasia renal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la ficha de AEMPS (el texto de indicación está vacío). En el grafo de conocimiento figuran hipotiroidismo, mixedema, bocio y cáncer de tiroides, entre otras |
| Nueva Indicación Predicha | Hipodisplasia/aplasia renal |
| Puntaje de Predicción TxGNN | 99,95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la liotironina es la forma activa de la hormona tiroidea (T3): su eficacia en el hipotiroidismo y en enfermedades tiroideas está bien establecida, y actúa sustituyendo la hormona deficiente y suprimiendo la TSH.

Sin embargo, **no se identifica un vínculo mecanístico plausible** con la nueva indicación. La hipodisplasia o aplasia renal es una malformación congénita del desarrollo, de carácter estructural, y es improbable que una hormona administrada después del nacimiento pueda revertirla. El puntaje elevado parece reflejar la cercanía en el grafo de conocimiento (fenotipos de anomalías congénitas compartidos) y no una justificación terapéutica.

Conviene señalar que otras predicciones del mismo análisis siguen patrones similares. Entre ellas figuran la agenesia renal bilateral, la secuencia de Potter, el complejo de Carney, el mixoma y el angiomixoma, todas sin evidencia clínica. El bocio nodular ya forma parte de las indicaciones originales, por lo que no constituye un verdadero reposicionamiento. La acrodisostosis, con hormonas resistentes, es mecanísticamente concebible pero no está demostrada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hipodisplasia/aplasia renal.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 45503 | TRIYODOTIRONINA LEO | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, hipopituitarismo y déficits de hormona de crecimiento o hipogonadismo hipogonadotrópico, osteoporosis (incluida la posmenopáusica), diabetes mellitus y cetoacidosis diabética, enfermedad coronaria e infarto de miocardio, y enfermedades del timo.
- **Interacciones farmacológicas**: se identificaron 100 interacciones; las 20 mostradas son todas de nivel moderado. Destacan:
  - Antidiabéticos: acarbosa, metformina, pioglitazona, alogliptina, linagliptina, canagliflozina, dapagliflozina, empagliflozina, clorpropamida, albiglutida y dulaglutida.
  - Inhibidores de la bomba de protones: omeprazol, rabeprazol y dexlansoprazol.
  - Simpaticomiméticos: epinefrina, isometepteno y dietilpropión.
  - Sales de calcio y magnesio: fosfato de calcio, acetato de calcio y óxido de magnesio.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos ni literatura, y no existe un mecanismo plausible para corregir una malformación renal congénita con hormona tiroidea. Además, el perfil de seguridad (cardiovascular, óseo y metabólico) no justifica un uso especulativo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y análisis del vínculo mecanístico con la nueva indicación
- Texto de indicaciones, advertencias y contraindicaciones del prospecto de AEMPS
- Estudios preclínicos o de mecanismo que justifiquen un efecto sobre el desarrollo renal
- Reevaluar candidatos con mayor sustento biológico antes de invertir más recursos en esta predicción
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

