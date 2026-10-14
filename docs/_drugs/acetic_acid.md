---
layout: default
title: Acetic Acid
parent: Solo predicción del modelo (L5)
nav_order: 18
evidence_level: L5
indication_count: 9
---

# Acetic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Ácido acético: De otitis externa a trastorno posbacteriano

## Resumen en Una Frase

El ácido acético es un antiséptico y acidificante de uso tópico, originalmente asociado al tratamiento de la otitis externa y de enfermedades del oído externo.
El modelo TxGNN predice que podría ser efectivo para el **trastorno posbacteriano**, pero no hay **ningún ensayo clínico** ni **ninguna publicación** que respalde esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Otitis externa / enfermedad del oído externo (según el grafo de conocimiento; las autorizaciones españolas no incluyen texto de indicación) |
| Nueva Indicación Predicha | Trastorno posbacteriano |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el ácido acético es un antiséptico y acidificante tópico con actividad antibacteriana. Su eficacia en infecciones superficiales del oído externo se explica por la reducción del pH local, que dificulta el crecimiento microbiano.

La relación con el trastorno posbacteriano es débil. Este tipo de cuadros son secuelas inflamatorias o inmunomediadas posteriores a una infección, no infecciones activas. Por ello, la actividad antibacteriana tópica no ofrece un vínculo mecanístico establecido. El puntaje alto de TxGNN refleja conectividad en el grafo de conocimiento, no evidencia biológica o clínica.

Otras predicciones del modelo (vasculitis posinfecciosa, síndrome posinfeccioso, cardiomiopatía chagásica, estenosis uretral infecciosa, síndrome hemolítico urémico asociado a infección, osteoporosis inducida por fármacos) tampoco cuentan con ensayos y tienen mecanismos poco plausibles. La única predicción con alguna base plausible es **tinea corporis** (nivel L4, "pregunta de investigación"): el ácido acético reduce el pH cutáneo y tiene actividad antifúngica in vitro. Hay informes históricos (1946-1958) sobre ácido acético diluido en tinea capitis y epidermofitosis del pie, además de modelos in vitro de onicomicosis. Se trata de evidencia indirecta, antigua y sin control, y no se refiere específicamente a tinea corporis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para el trastorno posbacteriano (indicación principal) actualmente no hay literatura relacionada disponible.

Como referencia, la predicción alternativa de mayor interés (tinea corporis) tiene la siguiente literatura indirecta:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20996178](https://pubmed.ncbi.nlm.nih.gov/20996178/) | 1946 | Informe clínico histórico | JAMA | Tratamiento de tinea capitis con yodo especial y ácido acético diluido |
| [20983383](https://pubmed.ncbi.nlm.nih.gov/20983383/) | 1946 | Informe clínico histórico | Arch Dermatol Syphilol | Tratamiento de tinea capitis con yodo especial y ácido acético diluido |
| [20256868](https://pubmed.ncbi.nlm.nih.gov/20256868/) | 1947 | Serie histórica de casos | Urol Cutan Rev | Resultados en una serie mayor de pacientes con tinea capitis |
| [13616002](https://pubmed.ncbi.nlm.nih.gov/13616002/) | 1958 | Informe clínico histórico | Vestn Dermatol Venerol | Epidermofitosis del pie tratada con concentraciones crecientes de ácido acético |
| [31049344](https://pubmed.ncbi.nlm.nih.gov/31049344/) | 2019 | Serie de casos | Skin Appendage Disord | Peeling químico como alternativa a antifúngicos orales en onicomicosis |
| [26857689](https://pubmed.ncbi.nlm.nih.gov/26857689/) | 2016 | Estudio in vitro | Mycoses | Evaluación de productos antifúngicos tópicos en un modelo in vitro de onicomicosis |
| [37256034](https://pubmed.ncbi.nlm.nih.gov/37256034/) | 2023 | Serie de casos / etiología | Arch Plast Surg | Quemaduras causadas por remedios populares coreanos; señal de riesgo con concentraciones no controladas |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 12467 | COR PIK CALLICIDA COLODION | Colodión | No disponible |
| 56618 | QUOCIN 120 mg/ 60 mg/ ml COLODION | Colodión | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del prospecto): porfiria hereditaria, enfermedad del metabolismo de las porfirinas, porfiria, infección por herpes simple y herpes zóster geniculado.
- **Otras señales**: un informe de 2023 documenta quemaduras por remedios populares con concentraciones no controladas, lo que indica riesgo de lesión cutánea con uso inadecuado.
- **Interacciones farmacológicas**: no se encontraron interacciones registradas.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para trastorno posbacteriano es solo un resultado del modelo (L5), sin ensayos ni literatura, y sin vínculo mecanístico plausible entre un antiséptico tópico y una secuela inmunomediada o inflamatoria.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias y contraindicaciones) para completar el análisis de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank.
- Definir la indicación aprobada en las autorizaciones españolas, que actualmente no tienen texto de indicación.
- Si se desea explorar la alternativa más plausible (tinea corporis, L4), diseñar una comparación controlada moderna frente a antifúngicos tópicos estándar, con concentraciones definidas y control de seguridad cutánea.
- Evaluar la compatibilidad de vías de administración (la presentación comercializada es colodión tópico) y la similitud con la indicación original.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

