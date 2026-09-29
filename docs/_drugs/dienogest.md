---
layout: default
title: Dienogest
parent: Evidencia moderada (L3-L4)
nav_order: 175
evidence_level: L4
indication_count: 10
---

# Dienogest
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Dienogest: De Endometriosis a Amenorrea

## Resumen en Una Frase

Dienogest es un progestágeno que se utiliza en el tratamiento de la endometriosis (indicación tomada de la literatura, ya que las fichas de AEMPS del paquete no incluyen texto de indicación). El modelo TxGNN predice que podría ser efectivo para **amenorrea**, pero **ninguno de los 4 ensayos clínicos** ni de las **6 publicaciones** asociadas estudia la amenorrea como enfermedad a tratar. La amenorrea es un efecto esperado del fármaco y no un objetivo terapéutico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99,71 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, dienogest es un progestágeno que suprime el endometrio y reduce los niveles de gonadotropinas y estradiol. Su eficacia en endometriosis está descrita en la literatura, y la amenorrea es una consecuencia frecuente de este efecto hormonal.

La predicción del modelo probablemente refleja esta asociación fármaco-fenotipo (el fármaco provoca amenorrea), no una indicación tratable. Un progestágeno que induce amenorrea no es, por ello, un tratamiento de la amenorrea.

Por tanto, esta predicción **no tiene respaldo mecanístico como nueva indicación**. No hay evidencia directa de que dienogest sirva para tratar la amenorrea.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | Completado | 895 | Cohorte observacional prospectiva sobre calidad de vida y seguridad a largo plazo de dienogest en mujeres asiáticas con endometriosis |
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | Completado | 968 | Estudio observacional en práctica clínica real de dienogest en endometriosis |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Activo, sin reclutar | 138 | Compara estradiol transdérmico + dienogest frente a drospirenona en endometriosis (satisfacción de las pacientes) |
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Fase 3 | Reclutando | 290 | Ensayo abierto y aleatorizado de no inferioridad: Indinol Forto frente a Visanne 2 mg en endometriosis |

Todos los ensayos son de relevancia baja (grado C): estudian endometriosis, no amenorrea. El único de Fase 3 sigue en reclutamiento y su condición objetivo no es la amenorrea.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Revisión sistemática | BMC Pharmacol Toxicol | Resume los eventos adversos de dienogest y su prevalencia durante el tratamiento de endometriosis y adenomiosis |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Revisión | Rev Endocr Metab Disord | Base endocrina de los tratamientos hormonales de la endometriosis (dependencia de estrógenos y resistencia a la progesterona) |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Otro | Eur J Contracept Reprod Health Care | Propiedades farmacológicas de dienogest 2 mg y su uso en endometriosis; menciona la inducción de amenorrea como objetivo hormonal general |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Cohorte | Reprod Sci | Cohorte retrospectiva de 514 mujeres: eficacia, seguridad y recurrencia del endometrioma con dienogest más allá de 12 meses |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Reporte de caso | Medicine | Tumor de células de la granulosa ovárico en una paciente con síndrome de ovario poliquístico (relevancia indirecta) |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Revisión | J Pediatr Adolesc Gynecol | Visualización avanzada de anomalías müllerianas para diagnóstico y planificación quirúrgica (relevancia indirecta) |

Ninguna publicación evalúa dienogest como tratamiento de la amenorrea.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 84765 | Dienogest Aristo 2 mg comprimidos EFG | Comprimido |
| 85463 | Adienocare 2 mg comprimidos EFG | Comprimido |
| 84820 | Endovelle 2 mg comprimidos EFG | Comprimido |
| 84015 | Dimetrio 2 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 89468 | Dienogest Adalvo 2 mg comprimidos EFG | Comprimido |

Se muestran 5 de las 7 autorizaciones. Los registros no incluyen texto de indicación aprobada.

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La amenorrea es un efecto esperado de dienogest, no un objetivo terapéutico. La puntuación alta de TxGNN (99,71 %) refleja probablemente esa asociación y no una indicación tratable. Ningún ensayo ni publicación respalda su uso para esta condición.
- Las otras nueve predicciones del modelo (insuficiencia ovárica primaria, enfermedad fibroquística de mama, entre otras) tienen evidencia L4-L5 y tampoco justifican avanzar. Solo la enfermedad fibroquística de mama se marca como pregunta de investigación.

**Para avanzar se necesita:**
- Confirmar si la predicción tiene un objetivo clínico real (por ejemplo, control de sangrado) o si es solo un efecto farmacológico esperado.
- Obtener el prospecto de AEMPS con advertencias y contraindicaciones, que hoy falta y bloquea el cribado de seguridad.
- Obtener los datos de mecanismo de acción desde DrugBank.
- Obtener el texto de indicación aprobada de las autorizaciones españolas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

