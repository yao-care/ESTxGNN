---
layout: default
title: Capecitabine
parent: Evidencia alta (L1-L2)
nav_order: 138
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Capecitabine: nueva indicación predicha, Adenocarcinoma tubular gástrico (nivel de evidencia L1). Indicación original: Cáncer gástrico (según el grafo de conocimiento"
monitor_inn: "Capecitabine"
predicted_indications: ["gastric adenocarcinoma and proximal polyposis of the stomach", "signet ring cell gastric adenocarcinoma", "gastric tubular adenocarcinoma", "gastric cardia adenocarcinoma"]
---

# Capecitabine
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Capecitabina: De Cáncer Gástrico a Adenocarcinoma Tubular Gástrico

## Resumen en Una Frase

Capecitabina es un profármaco oral de la fluoropirimidina (se convierte en 5-FU), utilizado originalmente en el tratamiento del cáncer gástrico y de las metástasis de tumores malignos de colon.
El modelo TxGNN predice que podría ser eficaz para **adenocarcinoma tubular gástrico** (la predicción con mayor evidencia, entre las 10 candidatas evaluadas, todas ellas subtipos o localizaciones del cáncer gástrico), con **0 ensayos clínicos** y **19 publicaciones** que respaldan esta dirección, incluidos varios ensayos de Fase 3 con regímenes que contienen capecitabina.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer gástrico (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Adenocarcinoma tubular gástrico |
| Puntaje de Predicción TxGNN | 99,94% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

**Nota:** esta es una predicción de la categoría de "reposicionamiento" en sentido débil: el adenocarcinoma tubular es un subtipo histológico del cáncer gástrico, ya cubierto por la indicación original. Se trata más de una confirmación de uso que de un uso realmente nuevo.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, capecitabina es un profármaco de fluoropirimidina que se convierte preferentemente en 5-fluorouracilo (5-FU), cuyo metabolito activo inhibe la timidilato sintasa (TYMS), enzima clave en la síntesis de ADN. La base de datos farmacológica consultada confirma la interacción con TYMS y su uso clínico en cáncer colorrectal y de mama metastásicos.

El adenocarcinoma tubular es un subtipo histológico frecuente del adenocarcinoma gástrico, indicación en la que capecitabina ya está establecida. Los ensayos de Fase 3 recuperados emplean regímenes con capecitabina (por ejemplo, CLASSIC con capecitabina más oxaliplatino adyuvante tras gastrectomía D2, y GLOW con zolbetuximab más CAPOX). Por tanto, la plausibilidad mecanística es alta, pero la evidencia corresponde al adenocarcinoma gástrico en general y no a la histología tubular específicamente.

Otras predicciones del modelo con puntuaciones similares (≈99,9%) tienen un respaldo muy dispar: el carcinoma de cardias gástrico (L2) y el cuerpo gástrico (L1) tienen apoyo clínico; el carcinoma de células en anillo de sello, el de tipo glándula salival y el asociado a virus de Epstein-Barr se sitúan en L3; y las predicciones de poliposis proximal con adenocarcinoma gástrico (GAPPS), cáncer gástrico microinvasivo y tumor gástrico de células granulares maligno solo tienen respaldo del modelo (L5), con una justificación clínica débil.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para adenocarcinoma tubular gástrico.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | ECA Fase 3 | Lancet | CLASSIC: quimioterapia adyuvante con capecitabina + oxaliplatino tras gastrectomía D2 frente a cirugía sola en cáncer gástrico estadio II-IIIB |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | ECA Fase 3 | Lancet Oncol | RESOLVE: S-1 + oxaliplatino perioperatorio frente a capecitabina + oxaliplatino adyuvante tras gastrectomía D2 |
| [39952264](https://pubmed.ncbi.nlm.nih.gov/39952264/) | 2025 | Informe final de ECA Fase 3 | Lancet Oncol | RESOLVE: análisis actualizado de supervivencia global |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | ECA Fase 3 | Nature Medicine | GLOW: zolbetuximab + CAPOX en adenocarcinoma gástrico/de la unión gastroesofágica CLDN18.2 positivo |
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | ECA Fase 2/3 | Lancet | FLOT4: FLOT frente a ECF/ECX (incluye capecitabina) perioperatorio en adenocarcinoma gástrico resecable |
| [27776843](https://pubmed.ncbi.nlm.nih.gov/27776843/) | 2016 | ECA Fase 2 (parte del FLOT4) | Lancet Oncol | Regresión histopatológica con FLOT frente a ECF/ECX neoadyuvante |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | ECA Fase 3 | Lancet | CheckMate 649: nivolumab + quimioterapia frente a quimioterapia sola en primera línea |
| [37875143](https://pubmed.ncbi.nlm.nih.gov/37875143/) | 2023 | ECA Fase 3 | Lancet Oncol | KEYNOTE-859: pembrolizumab + quimioterapia en cáncer gástrico HER2 negativo |
| [38806195](https://pubmed.ncbi.nlm.nih.gov/38806195/) | 2024 | ECA Fase 3 | BMJ | RATIONALE-305: tislelizumab + quimioterapia en primera línea |
| [20728210](https://pubmed.ncbi.nlm.nih.gov/20728210/) | 2010 | ECA Fase 3 | Lancet | ToGA: trastuzumab + quimioterapia en cáncer gástrico HER2 positivo |

*Se muestran 10 de las 19 publicaciones recuperadas. Varios de estos ensayos evalúan fármacos añadidos (inmunoterapia, anticuerpos) a un esqueleto de quimioterapia que puede incluir capecitabina, por lo que no aíslan su efecto.*

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 00163001 | XELODA 150 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 12763001 | ECANSYA 150 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 112761001 | Capecitabina Teva 150 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 76108 | Capecitabina Kern Pharma 150 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 79673 | ZAPECINE 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |

*Hay 20 autorizaciones vigentes en total (todas de medicamento con un único principio activo, ninguna cancelada).*

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (clase fluoropirimidina, profármaco de 5-FU) |
| Riesgo de Mielosupresión | Medio a alto: el grafo de conocimiento registra neutropenia, trombocitopenia, anemia y agranulocitosis como condiciones asociadas de contraindicación o precaución |
| Clasificación de Emetogenicidad | Baja a moderada (clasificación general de la clase; consultar el prospecto) |
| Items de Monitoreo | Hemograma con diferencial, función hepática (incluida bilirrubina), función renal, electrolitos |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según el grafo de conocimiento, no el texto del prospecto):** deficiencia de dihidropirimidina deshidrogenasa (DPD), enfermedad hepática, hiperbilirrubinemia (incluidos síndrome de Gilbert e hiperbilirrubinemia hereditaria), insuficiencia renal, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, anemia (incluida la macrocítica), enfermedad coronaria, parada cardíaca súbita, enfermedad de conducción cardíaca, enterocolitis necrosante, estomatitis y enfermedades infecciosas.
- **Interacciones farmacológicas:** la consulta se completó y solo devolvió la interacción farmacológica con el objetivo timidilato sintasa (TYMS), sin nivel de gravedad asignado. No se registraron interacciones con otros fármacos.

Las advertencias y contraindicaciones oficiales del prospecto de la AEMPS no están disponibles en los datos compilados; consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Varios ECA de Fase 3 con regímenes que contienen capecitabina respaldan su uso en adenocarcinoma gástrico, del que el subtipo tubular forma parte, y el fármaco ya está comercializado en España. Sin embargo, no hay ensayos registrados ni datos específicos de histología tubular, y la seguridad del prospecto no está disponible, por lo que se recomienda avanzar con salvaguardas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones, indicaciones aprobadas), ya que su ausencia es un vacío bloqueante para el cribado de seguridad.
- Datos detallados del mecanismo de acción (MOA) desde DrugBank.
- Confirmar si existen datos por subtipo histológico (tubular) dentro de los ensayos de Fase 3 identificados.
- Cribado de deficiencia de DPD y plan de monitoreo hematológico, hepático y renal.
- Valorar por separado las predicciones con mejor respaldo clínico (cuerpo gástrico, L1; cardias, L2) y mantener en espera las de solo predicción del modelo (L5).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

