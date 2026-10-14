---
layout: default
title: Chloroprocaine
parent: Solo predicción del modelo (L5)
nav_order: 172
evidence_level: L5
indication_count: 1
---

# Chloroprocaine
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

# Cloroprocaína: De Anestesia Local a Síndrome de la Cola de Caballo (Predicción No Terapéutica)

## Resumen en Una Frase

Cloroprocaína es un anestésico local de tipo éster, comercializado en España en solución inyectable.
El modelo TxGNN predice una asociación con **síndrome de la cola de caballo** (puntaje alto), pero la literatura la describe como una posible **complicación** de la anestesia neuroaxial y no como un tratamiento.
No hay **ensayos clínicos** registrados y las **4 publicaciones** disponibles no respaldan un uso terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones de AEMPS (texto de indicación vacío) |
| Nueva Indicación Predicha | Síndrome de la cola de caballo |
| Puntaje de Predicción TxGNN | 99,01 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

**Esta predicción no es razonable desde el punto de vista terapéutico.** Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la cloroprocaína es un anestésico local de tipo éster que bloquea los canales de sodio dependientes de voltaje, lo que impide la conducción del impulso nervioso.

La literatura revisada asocia la cloroprocaína con el síndrome de la cola de caballo como un **posible evento adverso** de la anestesia espinal o epidural. Este se atribuye a neurotoxicidad por concentraciones locales elevadas o mala distribución del anestésico, y no a un efecto beneficioso.

El puntaje elevado (0,99) probablemente refleja una asociación en el grafo de conocimiento entre anestésicos locales y esta enfermedad **como causa**, no una relación terapéutica. No se identificó un vínculo mecanístico que sustente su uso para tratar este síndrome.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22236346](https://pubmed.ncbi.nlm.nih.gov/22236346/) | 2012 | ECA | Acta Anaesthesiol Scand | Comparación aleatorizada de cloroprocaína y lidocaína para anestesia espinal selectiva en prostatectomía transuretral ambulatoria; es un estudio de anestesia, no de tratamiento del síndrome |
| [23320599](https://pubmed.ncbi.nlm.nih.gov/23320599/) | 2013 | Revisión | Acta Anaesthesiol Scand | Uso de 2-cloroprocaína en anestesia espinal; se mencionan secuelas neurológicas descritas tras inyección intratecal de dosis altas con conservantes |
| [11368250](https://pubmed.ncbi.nlm.nih.gov/11368250/) | 2001 | Revisión | Drug Safety | Complicaciones de la anestesia regional (fallo, lesión neural y toxicidad del anestésico local) e importancia de su prevención |
| [9338907](https://pubmed.ncbi.nlm.nih.gov/9338907/) | 1997 | Reporte de caso | Regional Anesthesia | Dos casos de síndrome de la cola de caballo tras anestesia espinal-epidural; se señala que anestésicos como la cloroprocaína se han implicado en su etiología |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 84918 | AMPRES 20 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |
| 76137 | AMPRES 10 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones potenciales según el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo, no texto de prospecto): enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, miastenia gravis (incluida la de inicio en adulto), enfermedad de la unión neuromuscular, deficiencia de butirilcolinesterasa, enfermedad cardiovascular y cardiopatía.
- **Interacciones Farmacológicas** (12 registradas):
  - **Mayor**: ácido nitroso.
  - **Moderadas**: sulfasalazina, lidocaína (tópica y oftálmica), benzocaína (tópica), cocaína (nasal y tópica), tetracaína (oftálmica y tópica), oxibuprocaína (oftálmica) y cinchocaína (tópica).
  - **Menor**: hialuronidasa.
- Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos, y la literatura sugiere que el síndrome de la cola de caballo es una complicación asociada a la cloroprocaína, no una indicación terapéutica. Proseguir sería inapropiado y potencialmente perjudicial.

**Para avanzar se necesita:**
- Descartar formalmente la predicción como artefacto del grafo de conocimiento (asociación causal frente a terapéutica).
- Obtener las advertencias, contraindicaciones e indicaciones aprobadas del prospecto de AEMPS (pendiente, bloquea el cribado de seguridad).
- Obtener datos del mecanismo de acción desde DrugBank.
- Evaluar otras indicaciones predichas con mejor plausibilidad terapéutica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

