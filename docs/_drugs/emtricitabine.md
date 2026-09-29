---
layout: default
title: Emtricitabine
parent: Solo predicción del modelo (L5)
nav_order: 200
evidence_level: L5
indication_count: 3
---

# Emtricitabine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Emtricitabina: De Infección por VIH-1 a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Emtricitabina es un inhibidor nucleósido de la transcriptasa inversa (ITIN) que se utiliza en humanos contra el VIH-1. Esta indicación es de conocimiento general del fármaco, porque el registro de la AEMPS del Evidence Pack no incluye el texto de indicación.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina (FIV)**, con **4 ensayos clínicos** (todos en VIH humano, evidencia indirecta) y **1 publicación** (un estudio en gatos infectados con FIV) que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 (conocimiento general; el registro AEMPS del pack no contiene texto de indicación) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L4 (solo un estudio preclínico en animales) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, emtricitabina es un análogo nucleósido que se incorpora al ADN proviral y termina la elongación de la cadena, con eficacia comprobada en VIH-1. Mecanísticamente podría ser aplicable al FIV.

El FIV es un lentivirus de gatos, cuya transcriptasa inversa es homóloga a la del VIH-1. Provoca una disfunción inmunitaria progresiva, similar a la del VIH en humanos. Esta similitud explica que el modelo relacione el fármaco con la enfermedad felina.

Hay dos limitaciones importantes. Los ensayos clínicos citados se realizaron en personas con VIH-1 y no prueban el fármaco en gatos. Además, la farmacocinética, la toxicidad y la eficacia entre especies no están establecidas. Se trata de una indicación veterinaria, distinta de un uso humano.

---

## Evidencia de Ensayos Clínicos

Los cuatro ensayos son de VIH-1 en humanos. La emtricitabina aparece solo como posible componente del esquema base o comparador, por lo que la relevancia para el FIV es baja (grado C).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Fase 3 | Completado | 844 | Dolutegravir + abacavir/lamivudina frente a Atripla (efavirenz/emtricitabina/tenofovir) en adultos con VIH-1 sin tratamiento previo; no inferioridad a 48 y 96 semanas |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Fase 3 | Completado | 828 | Dolutegravir frente a raltegravir con ITIN duales (ABC/3TC o TDF/FTC) en VIH-1 sin tratamiento previo; no inferioridad a 48 y 96 semanas |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Fase 2 | Completado | 208 | Selección de dosis diaria de dolutegravir con abacavir/lamivudina o tenofovir/emtricitabina en VIH-1 |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Fase 4 | Completado | 145 | Darunavir potenciado + lamivudina frente a darunavir + emtricitabina/tenofovir o lamivudina/tenofovir en VIH-1 sin tratamiento previo |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Estudio animal (gatos con FIV) | Viruses | Evalúa la farmacocinética y los resultados clínicos de una terapia antirretroviral combinada (dolutegravir 2,5 mg/kg, tenofovir 20 mg/kg, emtricitabina 40 mg/kg) en gatos infectados con FIV. El resumen disponible está truncado, por lo que no se han verificado los resultados de eficacia |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 03261001 | EMTRIVA 200 MG CÁPSULAS | Cápsula dura |
| 03261003 | EMTRIVA 10 MG/ML SOLUCIÓN ORAL | Solución oral |

Ambas autorizaciones pertenecen a Gilead Sciences Ireland Unlimited Company.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única evidencia directa es un estudio preclínico en gatos (L4) con resultados de eficacia aún no verificados. Los ensayos clínicos son de VIH humano y solo aportan evidencia indirecta. Además, la indicación es veterinaria y quedaría fuera del uso humano autorizado en España.

**Para avanzar se necesita:**
- Revisar el texto completo de PMID 37112803 para confirmar los resultados de eficacia y seguridad de la combinación con emtricitabina en gatos
- Datos de farmacocinética, toxicidad y dosis de emtricitabina en gatos
- Datos del mecanismo de acción desde DrugBank
- Información de advertencias y contraindicaciones del prospecto de la AEMPS
- Como referencia, la segunda predicción (infección por virus de inmunodeficiencia simia) cuenta con más estudios preclínicos en macacos con emtricitabina/tenofovir, aunque también es un modelo de investigación y no una indicación clínica humana
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

