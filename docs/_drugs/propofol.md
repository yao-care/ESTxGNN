---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 5
---

# Propofol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Propofol: De Anestesia General a Migraña

## Resumen en Una Frase

Propofol es un agente anestésico intravenoso utilizado ampliamente para la inducción y mantenimiento de la anestesia general y para sedación en procedimientos médicos. El modelo TxGNN predice que podría ser efectivo para **Migraña**, con **5 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anestesia general / Sedación (uso estándar como anestésico intravenoso) |
| Nueva Indicación Predicha | Migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 99.69% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Taiwan | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de propofol en las fuentes consultadas. Según la información conocida a partir de la evidencia disponible, propofol es un anestésico general intravenoso de acción rápida cuya eficacia en la inducción y mantenimiento de la anestesia ha sido ampliamente comprobada.

Existe una hipótesis mecanicista concreta que vincula ambas indicaciones: la publicación de Dhir et al. (PMID 22390898) muestra que el hemisuccinato de propofol suprime la depresión cortical propagada (*cortical spreading depression*, CSD), fenómeno que se considera el correlato neuronal del aura migrañosa y un posible desencadenante del dolor en la migraña. Esto proporciona una base farmacológica plausible para el uso de propofol en dosis subanestésicas como tratamiento abortivo de la migraña, más allá de la mera coincidencia estadística del modelo.

Adicionalmente, la relación entre ambas indicaciones ya tiene respaldo clínico observacional: desde el año 2000 (Krusz et al., PMID 10759925) se documenta el uso de propofol intravenoso para migraña refractaria, y esta línea de evidencia se ha extendido tanto a poblaciones adultas como pediátricas en el contexto de servicios de urgencias.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | Fase NA | Desconocido | 130 | Compara mantenimiento de anestesia con sevoflurano vs. propofol y aparición de cefalea postoperatoria; propofol se postula con efecto protector en pacientes migrañosos |
| [NCT02443220](https://clinicaltrials.gov/study/NCT02443220) | Fase NA | Completado | 315 | Estudio de electroacupuntura para analgesia en cirugía de bypass coronario sin circulación extracorpórea (relación indirecta con manejo del dolor) |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | Fase NA | Completado | 40 | Infusión de propofol en dosis baja como tratamiento abortivo de migraña en pacientes pediátricos; evalúa eficacia y límites de dosificación segura |
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Fase 2/3 | Completado | 74 | Propofol en dosis baja como terapia abortiva de migraña pediátrica en urgencias; revisión retrospectiva previa sugiere seguridad y posible mayor eficacia que el tratamiento estándar |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | Fase NA | Terminado | 12 | Propofol en dosis baja para migraña refractaria severa en urgencias; explora opciones de segunda línea cuando el tratamiento estándar falla |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | ECA | Arch Acad Emerg Med | Ensayo doble ciego que compara propofol+granisetrón vs. propofol+metoclopramida en manejo de migraña aguda |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | ECA | J Emerg Med | Ensayo controlado aleatorizado prospectivo de propofol en dosis baja para migraña pediátrica |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | ECA piloto | Emerg Med Australas | Compara propofol IV a dosis de sedación procedimental vs. terapia estándar en manejo inicial de migraña en urgencias |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | ECA | Arch Acad Emerg Med | Evalúa eficacia de sumatriptán+propofol vs. sumatriptán solo en migraña aguda |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Revisión sistemática | Acad Emerg Med | Revisión sistemática de seguridad y eficacia de propofol como terapia de migraña aguda en urgencias |
| [26790849](https://pubmed.ncbi.nlm.nih.gov/26790849/) | 2016 | Revisión sistemática | Headache | Revisión cualitativa de terapias de tratamiento agudo para migraña pediátrica |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | Revisión sistemática / meta-análisis en red | Headache | Compara efectividad de agentes parenterales para reducir recaídas tras migraña aguda severa |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Revisión sistemática | Cephalalgia | Guía de la Sociedad Canadiense de Cefalea con recomendaciones para tratamiento del dolor migrañoso en urgencias |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guía clínica | Headache | Actualización 2025 de la guía de la American Headache Society sobre farmacoterapias parenterales para migraña aguda en urgencias |
| [32638172](https://pubmed.ncbi.nlm.nih.gov/32638172/) | 2020 | Revisión | Curr Pain Headache Rep | Revisión del tratamiento intravenoso de migraña en niños y adolescentes |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Actualmente no hay datos de advertencias, contraindicaciones ni interacciones farmacológicas (DDI) disponibles en las fuentes consultadas; la obtención del inserto/prospecto de TFDA está identificada como un vacío de datos de severidad **bloqueante** (impide el ingreso a la evaluación de seguridad inicial S1).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia clínica y de literatura para migraña es razonablemente sólida (Nivel L2, con múltiples ECAs y una base mecanicista plausible vía supresión de la depresión cortical propagada), pero existe un vacío de datos **bloqueante**: no se dispone del prospecto/inserto de TFDA con advertencias y contraindicaciones, lo que impide completar la evaluación de seguridad inicial (S1). Además, propofol no está actualmente comercializado en Taiwan (0 autorizaciones), lo que añade incertidumbre regulatoria.

**Para avanzar se necesita:**
- Obtener el inserto/prospecto oficial de TFDA (o de la agencia reguladora de origen) con advertencias, contraindicaciones e interacciones
- Obtener datos de mecanismo de acción (MOA) desde DrugBank para completar el análisis de relación mecanística
- Evaluar la compatibilidad de vía de administración (propofol IV) frente a los requisitos de uso en dosis subanestésica para migraña en contexto de urgencias
- Definir estrategia de acceso al mercado dado que el fármaco actualmente no está comercializado en Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

