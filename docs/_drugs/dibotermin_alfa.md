---
layout: default
title: Dibotermin Alfa
parent: Solo predicción del modelo (L5)
nav_order: 246
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "dibotermin alfa"
predicted_indications: ["esotropia", "HER2 positive breast carcinoma", "normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "breast tumor luminal A or B", "progesterone-receptor negative breast cancer", "non-syndromic esophageal malformation", "multifocal choroiditis", "atypical coarctation of aorta"]
description: "Dibotermin Alfa: nueva indicación predicha, Esotropía (esotropia) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Dibotermin Alfa
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Dibotermin Alfa: Esotropía (esotropia)
{: .text-alpha }

## Resumen en Una Frase

Dibotermina alfa (proteína morfogenética ósea 2 humana recombinante, BMP-2) se utiliza originalmente en trastornos degenerativos del disco intervertebral y en fracturas de tibia, como agente osteoinductor.
El modelo TxGNN predice que podría ser efectivo para **esotropía**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Esotropía (esotropia) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Dibotermin Alfa es (traducción no oficial): «Agonista del receptor de proteína morfogenética ósea tipo 1A; agonista del receptor de activina tipo 2B; agonista del receptor de proteína morfogenética ósea tipo 2; agonista del receptor de proteína morfogenética ósea tipo 1B». Texto original en inglés: "Bone morphogenetic protein receptor type-1A agonist; Activin receptor type-2B agonist; Bone morphogenetic protein receptor type-2 agonist; Bone morphogenetic protein receptor type-1B agonist" ([ChEMBL CHEMBL2109171 (dibotermin alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2109171), CC BY-SA 3.0; consultado el 2026-11-19). Según el conocimiento general, dibotermina alfa es BMP-2 recombinante humana, un factor de crecimiento que induce la formación de hueso y cartílago cuando se aplica localmente sobre una matriz de implantación.

Para la esotropía **no se ha establecido un vínculo mecanístico**. La esotropía es una desviación ocular convergente relacionada con los músculos extraoculares y el control neural, mientras que dibotermina alfa actúa sobre el tejido óseo. El puntaje elevado del modelo (0.9997) es solo una predicción computacional, sin ensayos ni literatura de apoyo.

Conviene tener en cuenta que el modelo también generó otras predicciones (varios subtipos de cáncer de mama, malformación esofágica no sindrómica, coroiditis multifocal y coartación atípica de aorta). Todas se encuentran en nivel L5 y con recomendación Hold. En el caso del cáncer de mama, además, la señalización de BMP-2 podría ser promotora de tumores, lo que supone una preocupación de seguridad que debería abordarse primero.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esotropía.

Nota: para otra indicación predicha (tumor de mama luminal A o B) se recuperó una publicación preclínica (PMID [27441597](https://pubmed.ncbi.nlm.nih.gov/27441597/), 2016, *European Surgical Research*) sobre patrones de expresión génica en osteoblastos humanos en respuesta a BMP2. Es un estudio in vitro sin relación clínica directa con cáncer de mama ni con esotropía.

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 02226001 | INDUCTOS 1,5 MG/ML POLVO, DISOLVENTE Y MATRIZ PARA MATRIZ DE IMPLANTACIÓN | IMPLANTE | Medtronic Biopharma B.V. | Comercializada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Los datos compilados no incluyen advertencias ni contraindicaciones del prospecto, y no se encontraron interacciones farmacológicas registradas. Como consideración general, la posible promoción tumoral asociada a la señalización de BMP-2 es relevante para cualquier indicación oncológica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para esotropía se basa únicamente en el modelo (L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible entre un agente osteoinductor y una desviación ocular.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), indispensable antes de cualquier evaluación de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Realizar estudios preclínicos o de mecanismo que justifiquen un papel de BMP-2 en la esotropía
- Evaluar la compatibilidad de la vía de administración (implante en matriz) con la nueva indicación
- Si se considera cáncer de mama, evaluar primero el riesgo de promoción tumoral

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL2109171 (dibotermin alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2109171) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

