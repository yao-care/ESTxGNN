---
layout: default
title: Pantoprazole
parent: Solo predicción del modelo (L5)
nav_order: 407
evidence_level: L5
indication_count: 6
---

# Pantoprazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Pantoprazol: De Inhibidor de la Bomba de Protones (indicación original no registrada) a Úlcera Péptica Activa

## Resumen en Una Frase

Pantoprazol es un inhibidor de la bomba de protones comercializado en España en comprimidos gastrorresistentes y polvo para solución inyectable. Los registros de AEMPS del Evidence Pack no incluyen el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para **úlcera péptica activa**, con **3 ensayos clínicos** y **19 publicaciones** que respaldan esta dirección.
Por tratarse de una indicación ácido-dependiente clásica, es probable que sea una indicación ya autorizada y no un reposicionamiento genuino.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de AEMPS (texto de indicación vacío en todas las autorizaciones) |
| Nueva Indicación Predicha | Úlcera péptica activa (active peptic ulcer disease) |
| Puntaje de Predicción TxGNN | 99.69% |
| Nivel de Evidencia | L2 (1 ECA de Fase 3 completado en los ensayos listados; el paquete de datos asigna L1 al contar además ECA publicados en la literatura) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

El paquete de datos no incluye el mecanismo de acción de DrugBank. Según la literatura recuperada (PMID 19938880), pantoprazol es un inhibidor de la bomba de protones que se une de forma irreversible y específica a la H+/K+ ATPasa de la célula parietal gástrica. Esto reduce la secreción de ácido gástrico.

La úlcera péptica es una lesión de la mucosa en cuya aparición y cicatrización interviene el ácido gástrico. Suprimir el ácido favorece la curación de la úlcera y reduce las recurrencias. Por eso el vínculo entre el mecanismo y la nueva indicación es directo y está bien establecido.

**Advertencia:** pantoprazol está comercializado y la úlcera péptica es una indicación central de esta clase de fármacos. Lo más probable es que el campo de indicaciones originales esté vacío por falta de datos y que esta sea una indicación ya autorizada. Antes de presentarla como reposicionamiento, hay que verificarla contra la ficha técnica aprobada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Fase 3 | Completado | 323 | ECA multicéntrico, doble ciego y con control activo: erradicación de H. pylori con triple terapia de 7 días, ilaprazol frente a pantoprazol, en pacientes con úlcera gástrica o duodenal. Evidencia directa; el título está truncado y conviene confirmar comparador y criterio principal. |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/D | Completado | 316 | Estudio prospectivo de factores de riesgo para decidir quién necesita una segunda endoscopia tras hemostasia y perfusión de IBP a dosis altas en úlcera péptica sangrante. No evalúa la eficacia de pantoprazol. |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Fase 4 | Completado | 320 | Efecto de estatinas e IBP sobre la acción antiagregante de clopidogrel en pacientes con ICP. Aborda una interacción farmacológica, no el tratamiento de la úlcera. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | ECA | Digestion | Compara la perfusión intermitente y la continua de pantoprazol para prevenir el resangrado de la úlcera péptica tras terapia endoscópica. |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | ECA | Aliment Pharmacol Ther | Compara tres triples terapias con pantoprazol para la erradicación de H. pylori y la cicatrización de la úlcera gástrica. |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | ECA (según el título) | J Gastroenterol Hepatol | Perfusión de pantoprazol como tratamiento adyuvante al endoscópico en la úlcera péptica sangrante. |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | ECA | Gut and Liver | Tegoprazán frente a un comparador activo en úlceras artificiales tras resección endoscópica. Es evidencia indirecta, de la clase de fármacos. |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Revisión sistemática / metaanálisis en red | Am J Gastroenterol | Compara P-CAB con IBP en esofagitis grado C/D. Es evidencia indirecta, de la clase de fármacos. |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Estudio clínico (diseño no verificado) | Hepatogastroenterology | Compara lansoprazol y pantoprazol en úlcera duodenal activa y erradicación de H. pylori. |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | Estudio clínico (tipo no verificado) | Aliment Pharmacol Ther | Pantoprazol, amoxicilina y azitromicina o claritromicina para erradicar H. pylori en úlcera duodenal. |
| [10228801](https://pubmed.ncbi.nlm.nih.gov/10228801/) | 1999 | Estudio clínico (tipo no verificado) | Hepatogastroenterology | Eficacia y tolerabilidad de una triple terapia de una semana con pantoprazol, amoxicilina y metronidazol en úlcera duodenal con H. pylori. |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclínico (modelo animal) | Inflammopharmacology | Pantoprazol combinado con células madre mesenquimales en úlcera gástrica experimental en ratas: estrés oxidativo, inflamación y apoptosis. |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Revisión | Clin Drug Investig | Revisión del mecanismo de pantoprazol como inhibidor de la bomba de protones y de su perfil de interacciones. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 17903-12-09-1995 | PANTECTA 40 mg COMPRIMIDOS GASTRORRESISTENTES (Takeda Hellas S.A.) | Comprimido gastrorresistente |
| 61001 | PANTECTA 40 mg COMPRIMIDOS GASTRORRESISTENTES (Takeda Gmbh) | Comprimido gastrorresistente |
| 77931 | PANTOPRAZOL DURBAN 40 MG COMPRIMIDOS GASTRORRESISTENTES EFG (Laboratorios Francisco Durban S.A.) | Comprimido gastrorresistente |
| 69698 | PANTOPRAZOL NORMON 40 mg POLVO PARA SOLUCION INYECTABLE EFG (Laboratorios Normon S.A.) | Polvo para solución inyectable |
| 72528 | PANTOPRAZOL BLUEFISH 40 mg COMPRIMIDOS GASTRORRESISTENTES EFG (Bluefish Pharmaceuticals Ab) | Comprimido gastrorresistente |

Se muestran 5 de las 20 autorizaciones. Los registros no incluyen el texto de la indicación aprobada, por lo que se omite esa columna.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como referencia, el ensayo NCT00930670 estudia la posible interferencia de los IBP con el efecto antiagregante de clopidogrel. Conviene revisar esta interacción al evaluar pacientes con doble antiagregación.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un mecanismo directo y bien establecido, un ensayo de Fase 3 completado y varios ECA publicados en úlcera péptica y duodenal. La evidencia es sólida, pero es probable que la indicación ya esté autorizada, por lo que no debe presentarse como reposicionamiento sin verificarlo.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de AEMPS para confirmar si la úlcera péptica es una indicación ya aprobada. Este dato también aporta las advertencias y contraindicaciones, que hoy faltan.
- Obtener el mecanismo de acción de DrugBank para completar el análisis mecanístico.
- Confirmar el comparador y el criterio principal del ensayo NCT02084420, cuyo título está truncado.
- Completar los datos de seguridad e interacciones, que no constan en el paquete de datos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

