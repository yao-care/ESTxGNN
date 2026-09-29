---
layout: default
title: Atorvastatin
parent: Evidencia alta (L1-L2)
nav_order: 54
evidence_level: L1
indication_count: 6
---

# Atorvastatin
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **6** 
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

# Atorvastatina: De Hipercolesterolemia (uso clínico general) a Hipercolesterolemia Familiar

## Resumen en Una Frase

La atorvastatina es un hipolipemiante (inhibidor de la HMG-CoA reductasa) que se usa para tratar la hipercolesterolemia y la dislipidemia mixta y para la prevención cardiovascular primaria.
El modelo TxGNN predice que podría ser efectiva para **hipercolesterolemia familiar**,
con **35 ensayos clínicos** y **19 publicaciones** relacionados con esta dirección. Muchos evalúan la atorvastatina como tratamiento de base o comparador, no como intervención aislada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los textos de AEMPS del paquete de datos. La fuente farmacológica describe el uso clínico como hipercolesterolemia y dislipidemia mixta |
| Nueva Indicación Predicha | Hipercolesterolemia familiar |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

La atorvastatina inhibe la enzima HMG-CoA reductasa (gen *HMGCR*), paso limitante de la síntesis de colesterol en el hígado. Al reducir el colesterol intracelular, aumentan los receptores hepáticos de LDL y baja el colesterol LDL (LDL-C). El paquete de datos no incluye un campo de mecanismo de acción completo. Esta descripción proviene de la diana registrada en la fuente farmacológica y de la justificación mecanística de la predicción.

La hipercolesterolemia familiar es un trastorno genético con LDL-C muy elevado y enfermedad cardiovascular prematura. Comparte con la indicación general del fármaco la misma vía biológica: el colesterol LDL. Por eso el modelo la puntúa tan alto.

Hay que tener en cuenta que las estatinas ya son tratamiento estándar en las guías para esta enfermedad. Se trata de un uso establecido más que de un reposicionamiento genuino. El campo de indicaciones originales vacío parece una laguna de la fuente de datos y conviene corregirlo antes de publicar.

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes, con atorvastatina como intervención o brazo de base en población con hipercolesterolemia familiar (FH).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Fase 3 | Completado | 272 | Estudio abierto de 3 años de atorvastatina en niños y adolescentes con FH heterocigota: crecimiento, desarrollo y reducción del colesterol |
| [NCT00134485](https://clinicaltrials.gov/study/NCT00134485) | Fase 3 | Completado | 400 | Aleatorizado, doble ciego: torcetrapib/atorvastatina frente a atorvastatina sola en FH heterocigota durante 6 meses |
| [NCT00136981](https://clinicaltrials.gov/study/NCT00136981) | Fase 3 | Completado | 800 | Torcetrapib/atorvastatina frente a atorvastatina a dosis máxima tolerada, con ecografía carotídea a 24 meses en FH heterocigota |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completado | 50 | Ezetimiba añadida a atorvastatina o simvastatina en FH homocigota |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Fase 3 | Completado | 44 | Extensión abierta de 24 meses: seguridad a largo plazo de ezetimiba con atorvastatina o simvastatina en FH homocigota |
| [NCT03867318](https://clinicaltrials.gov/study/NCT03867318) | Fase 3 | Completado | 621 | Ezetimiba 10 mg añadida a atorvastatina en FH heterocigota, enfermedad coronaria o múltiples factores de riesgo |
| [NCT03882996](https://clinicaltrials.gov/study/NCT03882996) | Fase 3 | Completado | 432 | Seguridad y tolerabilidad a 12 meses de ezetimiba con atorvastatina (10-80 mg) |
| [NCT00739999](https://clinicaltrials.gov/study/NCT00739999) | Fase 1 | Completado | 39 | Farmacocinética, farmacodinamia y seguridad de atorvastatina a 8 semanas en niños y adolescentes con FH heterocigota |
| [NCT00134511](https://clinicaltrials.gov/study/NCT00134511) | Fase 3 | Completado | 30 | Torcetrapib/atorvastatina en FH homocigota, abierto, con titulación forzada |
| [NCT00145431](https://clinicaltrials.gov/study/NCT00145431) | Fase 3 | Terminado | 41 | Torcetrapib/atorvastatina frente a atorvastatina sola y fenofibrato en disbetalipoproteinemia familiar; terminado anticipadamente |

**Notas:**
- El programa de torcetrapib se canceló el 2 de diciembre de 2006 por hallazgos de seguridad. Esto no invalida el brazo de atorvastatina, pero limita lo que se puede concluir de esos estudios.
- En la mayoría de los estudios de combinación la atorvastatina es tratamiento de base. Su efecto propio no se puede aislar con estos datos.
- Otros ensayos del paquete (alirocumab, colesevelam, ácido bempedoico) usan estatinas como terapia de fondo, pero no evalúan la atorvastatina directamente.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | Estudio clínico (sin clasificar) | J Clin Lipidol | Estudio de 3 años de atorvastatina en niños y adolescentes con FH heterocigota; evalúa eficacia y seguridad más allá de 1 año |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Estudio comparativo (sin clasificar) | Nutr Metab Cardiovasc Dis | Compara atorvastatina y simvastatina en el logro de objetivos de LDL-C en FH heterocigota, con efectos sobre fibrinógeno y coagulación |
| [12883464](https://pubmed.ncbi.nlm.nih.gov/12883464/) | 2003 | Estudio clínico | Med Sci Monit | Evalúa si la atorvastatina reduce la microalbuminuria en pacientes con FH y tolerancia normal a la glucosa |
| [22957727](https://pubmed.ncbi.nlm.nih.gov/22957727/) | 2013 | Estudio clínico (sin clasificar) | Echocardiography | Efecto de la atorvastatina sobre el flujo sanguíneo miocárdico y periférico en FH sin aterosclerosis coronaria |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Estudio observacional (sin clasificar) | J Am Coll Cardiol | Cuantifica las consecuencias de las estatinas sobre la enfermedad coronaria y la mortalidad global en FH heterocigota |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Revisión | Curr Atheroscler Rep | Nuevas terapias para reducir el LDL-C en hipercolesterolemia familiar homocigota |
| [26988948](https://pubmed.ncbi.nlm.nih.gov/26988948/) | 2016 | Revisión | J Am Coll Cardiol | Mejora del seguimiento y la atención de pacientes con FH |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Revisión | Ann Pharmacother | Eficacia y seguridad de la atorvastatina en dislipidemias e hipercolesterolemia primaria |
| [10582478](https://pubmed.ncbi.nlm.nih.gov/10582478/) | 1999 | Revisión (sin clasificar) | Rev Med Brux | Estatina sintética de segunda generación: inhibe la HMG-CoA reductasa, aumenta los receptores de LDL y su semivida prolongada mantiene la inhibición |
| [40254247](https://pubmed.ncbi.nlm.nih.gov/40254247/) | 2025 | Preclínico (sin clasificar) | Toxicology | Miotoxicidad por estatinas en células musculares derivadas de iPSC de pacientes con FH, comparando estatinas lipofílicas e hidrofílicas |

No hay ECA con clasificación explícita en la literatura provista. La evidencia bibliográfica es sobre todo observacional, de revisión o mecanística.

## Información de Mercado en España

Hay 20 autorizaciones en total; se muestran 5. El paquete de datos no incluye el texto de indicación aprobada de ninguna de ellas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 76261 | Atorvastatina Vir 20 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Industria Química y Farmacéutica Vir S.A. |
| 73778 | Atorvastatina Combix 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorios Combix S.L.U. |
| 89944 | Atorvastatina Davurgama 60 mg comprimidos recubiertos con película | Comprimido recubierto con película | Teva Pharma S.L.U. |
| 77296 | Atorvastatina Davur 30 mg comprimidos recubiertos con película | Comprimido recubierto con película | Teva Pharma S.L.U. |
| 86214 | Atorvastatina Bluefish 80 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Bluefish Pharmaceuticals AB (publ) |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta de interacciones solo devolvió la diana farmacológica (HMG-CoA reductasa), no interacciones con otros fármacos. Los ensayos de fase 1 del paquete estudian interacciones farmacocinéticas con antirretrovirales, y el análisis de la predicción señala interacciones clínicamente relevantes con inhibidores de proteasa y regímenes potenciados (CYP3A4).
- **Miotoxicidad**: un estudio preclínico reciente ([40254247](https://pubmed.ncbi.nlm.nih.gov/40254247/)) describe síntomas musculares asociados a estatinas en pacientes con FH.

Consultar el prospecto para las advertencias y contraindicaciones completas.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Varios ensayos de fase 3 completados en FH (heterocigota y homocigota) incluyen la atorvastatina como tratamiento de base o comparador, y hay estudios pediátricos de atorvastatina de hasta 3 años. La evidencia respalda el uso, pero se trata de una indicación ya establecida y no de un reposicionamiento nuevo.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS para obtener indicaciones, advertencias y contraindicaciones.
- Corregir el campo de indicaciones originales y el mecanismo de acción, que están vacíos en la fuente de datos.
- Confirmar el estado de la FH en la ficha técnica.
- Advertir que la FH homocigota responde poco a las estatinas y suele requerir terapia añadida.
- Aislar el efecto propio de la atorvastatina en los ensayos de combinación, cuyos títulos aparecen truncados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

