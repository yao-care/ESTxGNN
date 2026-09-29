---
layout: default
title: Budesonide
parent: Evidencia moderada (L3-L4)
nav_order: 86
evidence_level: L4
indication_count: 10
---

# Budesonide
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

# Budesonida: De Asma y Enfermedades Inflamatorias a Eccema Atópico

## Resumen en Una Frase

La budesonida es un corticoide sintético que se usa por inhalación en asma y EPOC, y por vía oral o rectal en enfermedad de Crohn, colitis ulcerosa y esofagitis eosinofílica.
El modelo TxGNN predice que podría ser efectivo para **eccema atópico**, con una puntuación muy alta (99,96 %).
Los datos recuperados incluyen **2 ensayos clínicos** y **20 publicaciones**, pero ninguno demuestra eficacia clínica de la budesonida en eccema. La única evidencia específica es un estudio preclínico de formulación (2024).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS (los textos de indicación están vacíos). Según farmacología (GtoPdb): asma, EPOC, enfermedad de Crohn, colitis ulcerosa, esofagitis eosinofílica |
| Nueva Indicación Predicha | Eccema atópico |
| Puntaje de Predicción TxGNN | 99,96 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados del mecanismo de acción en DrugBank. Los datos farmacológicos indican que la budesonida actúa sobre tres receptores: el receptor de glucocorticoides (NR3C1), el de mineralocorticoides (NR3C2) y el de progesterona (PGR). Como agonista del receptor de glucocorticoides, suprime las vías inflamatorias, incluida la inflamación de tipo 2.

Su uso original ya se centra en enfermedades inflamatorias de mucosas (vías respiratorias e intestino). El eccema atópico es una enfermedad inflamatoria cutánea de tipo 2, y los corticoides tópicos ya son tratamiento establecido, por lo que el mecanismo es plausible.

Sin embargo, esta plausibilidad es de clase farmacológica (corticoides en general), no específica de la budesonida. La puntuación TxGNN es alta, pero no discrimina entre candidatos. La única evidencia específica en dermatología es un estudio preclínico de nanopartículas en hidrogel (2024).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | N/A | Completado | 54 | Caracterización de endotipos de asma pediátrica grave (inmunología, metabolómica, microbiota). No es un ensayo de budesonida en eccema; la relación con la atopia es indirecta |
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Fase 1/2 | Completado | 58 | Inmunoterapia alérgica para prevenir morbilidad asmática en niños atópicos con sibilancias. El objetivo es asma, no eccema, y la budesonida no es claramente la intervención |

Ambos ensayos se clasificaron con relevancia baja (grado C).

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Estudio preclínico de formulación | Gels | Nanopartículas de Eudragit L 100 con budesonida en hidrogeles para terapia local de dermatitis atópica, con liberación sensible al pH |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | ECA (veterinario) | J Vet Pharmacol Ther | Acondicionador de budesonida al 0,025 % en perros con dermatitis atópica (29 perros, cruzado, con placebo): mejora de lesiones y prurito |
| [16428071](https://pubmed.ncbi.nlm.nih.gov/16428071/) | 2006 | Estudio in vitro | Int Immunopharmacol | La budesonida, pero no el tacrolimus, altera funciones inmunes de queratinocitos humanos normales |
| [19875223](https://pubmed.ncbi.nlm.nih.gov/19875223/) | 2010 | Estudio clínico | Allergol Immunopathol | Respuesta a budesonida en lactantes y preescolares con sibilancias recurrentes, atópicos y no atópicos. Es asma, no eccema |
| [31705907](https://pubmed.ncbi.nlm.nih.gov/31705907/) | 2020 | Revisión | J Allergy Clin Immunol | Terapias emergentes en esofagitis eosinofílica. Fuera del objetivo |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Revisión | Neuroimmunomodulation | Corticoides intranasales y supresión adrenal en rinitis alérgica (a menudo coexiste con dermatitis atópica) |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | Estudio clínico | Dermatology | Eje IGF, recambio óseo y de colágeno en niños con dermatitis atópica tratados con corticoides tópicos (no específico de budesonida) |
| [30053491](https://pubmed.ncbi.nlm.nih.gov/30053491/) | 2018 | Estudio observacional | J Am Acad Dermatol | Dermatitis de contacto alérgica a productos de cuidado personal y medicamentos tópicos en adultos con dermatitis atópica |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Estudio observacional | Contact Dermatitis | Pruebas de parche con budesonida en Italia (serie SIDAPA 2018-2019): tendencia decreciente de alergia a budesonida |
| [37927648](https://pubmed.ncbi.nlm.nih.gov/37927648/) | 2023 | Reporte de caso | Cureus | Angioedema y urticaria inducidos por esteroides en un paciente de 81 años con antecedente de dermatitis atópica |

Se recuperaron 20 publicaciones; se muestran las 10 más relevantes. La mayoría no aborda la eficacia de la budesonida en eccema. La evidencia más directa es preclínica o veterinaria.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Laboratorio |
|---------|------|------|-----------|
| 61728 | ENTOCORD 3 mg | Cápsula dura de liberación modificada | Tillotts Pharma GmbH |
| 83987 | Budesonida Aldo-Unión 100 microgramos/pulsación | Suspensión para inhalación en envase a presión | Laboratorio Aldo Unión S.L. |
| 88386 | Intestifalk 4 mg | Supositorio | Dr. Falk Pharma GmbH |
| 67103 | Novopulm Novolizer 400 microgramos | Polvo para inhalación | Viatris Healthcare Limited |
| 1171254003 | Jorveza 1 mg | Comprimido bucodispersable | Dr. Falk Pharma GmbH |

Se muestran 5 de las 20 autorizaciones. Entre las formas farmacéuticas registradas (inhalación, oral, rectal, nasal) no figura ninguna de aplicación cutánea.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

La literatura recuperada, aunque no procede del prospecto, señala puntos a vigilar con corticoides en atopia:
- Supresión del eje hipotálamo-hipófiso-adrenal con corticoides intranasales.
- Posible efecto sobre el crecimiento en niños con corticoides tópicos por absorción percutánea.
- Sensibilización de contacto: la budesonida es marcador de hipersensibilidad a corticoides en la serie básica europea.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque la puntuación TxGNN es muy alta y el mecanismo glucocorticoide es plausible, no hay ningún ensayo clínico de budesonida en eccema. La única evidencia específica es un estudio preclínico de formulación (L4), y la puntuación del modelo no discrimina entre candidatos. Además, la entrada "dermatitis, atópica" (puesto 3) es sinónimo de "eccema atópico" y debería fusionarse con esta.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que es una brecha bloqueante para el cribado de seguridad.
- Obtener el mecanismo de acción de DrugBank.
- Evaluar la compatibilidad de vía: las formas comercializadas en España no son cutáneas, y se requeriría una formulación tópica.
- Buscar ensayos clínicos de budesonida específicos en dermatitis atópica, frente a corticoides tópicos ya establecidos.
- Fusionar los registros duplicados de eccema atópico y dermatitis atópica.
- Si se busca una dirección con más respaldo dentro de esta lista, la predicción de **bronquitis** (puesto 2, L2, Proceed with Guardrails) tiene ensayos de fase 2/4 en bronquitis eosinofílica. Requiere confirmar la población y la intervención de cada ensayo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

