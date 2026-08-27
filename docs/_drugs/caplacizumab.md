---
layout: default
title: Caplacizumab
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Caplacizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Caplacizumab: De Indicación No Especificada en los Datos a Púrpura Trombocitopénica Trombótica (PTT)

## Resumen en Una Frase

Caplacizumab es un nanocuerpo anti-factor de von Willebrand (vWF) cuya indicación original no consta en este paquete de evidencia (dato ausente en `drug.original_indications` y en el registro regulatorio). El modelo TxGNN señala la **Púrpura Trombocitopénica Trombótica adquirida (aTTP)** como indicación de mayor solidez entre 10 candidatas generadas, respaldada por **14 ensayos clínicos** y **20 publicaciones**, incluyendo múltiples ensayos de Fase 3 completados. La propia evidencia recogida sugiere que esta podría ser ya la indicación central aprobada del fármaco y no un uso realmente nuevo — ver nota al final de esta sección.

> **Nota importante:** El paquete de evidencia lista 10 "indicaciones predichas", pero solo la de PTT (rango 5) tiene evidencia real; las otras 9 tienen nivel L5 (solo predicción del modelo, sin ensayos ni literatura) y recomendación "Hold" — varias de ellas señaladas en su propio razonamiento mecanístico como probablemente falsos positivos. Este informe se centra en la única señal con sustento clínico real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el paquete de datos (fármaco no comercializado en España; sin registro de indicación original) |
| Nueva Indicación Predicha | Púrpura Trombocitopénica Trombótica adquirida (aTTP) |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

No hay datos estructurados sobre el mecanismo de acción en la ficha del fármaco (brecha de datos DG002, prioridad alta, pendiente de consulta en DrugBank). Sin embargo, la propia evidencia clínica recogida en este paquete describe el mecanismo con claridad: caplacizumab es un fragmento de inmunoglobulina bivalente humanizado (nanocuerpo) dirigido contra el dominio A1 del factor de von Willebrand (vWF), que bloquea la interacción entre los multímeros de vWF y el receptor GPIb de las plaquetas.

En la PTT adquirida, un déficit autoinmune de la proteasa ADAMTS13 permite que se acumulen multímeros ultragrandes de vWF, que se adhieren de forma descontrolada a las plaquetas y generan microtrombos. Al bloquear precisamente esa unión vWF-GPIb, caplacizumab actúa sobre el mecanismo patogénico central de la enfermedad, lo que explica la solidez mecanística de esta señal frente a las otras 9 candidatas del paquete (varias de las cuales implican vías de sangrado no relacionadas, como defectos de GPIIb/IIIa o de scramblase de fosfolípidos).

**Aviso relevante:** varios ensayos citados (p. ej. HERCULES, TITAN, Post-HERCULES) corresponden a los estudios pivotales que sustentaron la aprobación real de caplacizumab (Cablivi) para aTTP en otras jurisdicciones. Esto sugiere que la "predicción" de TxGNN puede estar señalando una indicación ya establecida del fármaco, y que la ausencia de `original_indications` en este paquete es probablemente una brecha de datos de origen (curación incompleta) más que un descubrimiento genuino de reposicionamiento. Se recomienda verificar el estatus regulatorio real antes de tratar esta señal como candidato de reposicionamiento de novo.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02553317](https://clinicaltrials.gov/study/NCT02553317) | Fase 3 | Completado | 145 | Ensayo doble ciego, aleatorizado, controlado con placebo (HERCULES); evalúa normalización más rápida del recuento plaquetario como medida de prevención de microtrombosis. |
| [NCT05468320](https://clinicaltrials.gov/study/NCT05468320) | Fase 3 | Completado | 51 | Estudio abierto de un solo brazo; eficacia y seguridad de caplacizumab + inmunosupresión sin recambio plasmático de primera línea. |
| [NCT04074187](https://clinicaltrials.gov/study/NCT04074187) | Fase 2/3 | Completado | 21 | Estudio multicéntrico abierto en pacientes japoneses; evalúa prevención de recurrencia de aTTP, mortalidad y eventos tromboembólicos mayores. |
| [NCT02878603](https://clinicaltrials.gov/study/NCT02878603) | Fase 3 | Completado | 104 | Seguimiento prospectivo (Post-HERCULES) para evaluar seguridad y eficacia a largo plazo, incluido uso repetido de caplacizumab. |
| [NCT01151423](https://clinicaltrials.gov/study/NCT01151423) | Fase 2 | Completado | 75 | Ensayo aleatorizado, controlado con placebo, simple ciego (TITAN); nanocuerpo anti-vWF como tratamiento adyuvante al recambio plasmático. |
| [NCT04720261](https://clinicaltrials.gov/study/NCT04720261) | Fase 2 | Terminado | 58 | Régimen personalizado de caplacizumab guiado por monitorización de actividad de ADAMTS13. |
| [NCT05876221](https://clinicaltrials.gov/study/NCT05876221) | N/A | Completado | 223 | Estudio observacional sobre dinámica de recuento plaquetario bajo caplacizumab; desacopla el recuento plaquetario de la actividad de ADAMTS13. |
| [NCT06291025](https://clinicaltrials.gov/study/NCT06291025) | N/A | Reclutando | 131 | Estudio de no inferioridad, un solo brazo; inmunosupresión + caplacizumab + infusión de plasma sin recambio plasmático terapéutico. |
| [NCT04985318](https://clinicaltrials.gov/study/NCT04985318) | N/A | Reclutando | 350 | Estudio observacional prospectivo alemán (REACT-2020); confirma eficacia en mundo real e identifica factores predictivos. |
| [NCT05263193](https://clinicaltrials.gov/study/NCT05263193) | N/A | Completado | 4 | Recolección retrospectiva de datos pediátricos multinacionales sobre efectividad y seguridad de caplacizumab. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/) | 2019 | ECA | N Engl J Med | Publicación pivotal (HERCULES); caplacizumab inhibe la interacción vWF-plaquetas en aTTP. |
| [26863353](https://pubmed.ncbi.nlm.nih.gov/26863353/) | 2016 | ECA | N Engl J Med | Publicación pivotal (TITAN); reducción de microtrombosis asociada a plasma exchange e inmunosupresión. |
| [32914526](https://pubmed.ncbi.nlm.nih.gov/32914526/) | 2020 | Guía | J Thromb Haemost | Guías ISTH de tratamiento de PTT. |
| [32914582](https://pubmed.ncbi.nlm.nih.gov/32914582/) | 2020 | Guía | J Thromb Haemost | Guías ISTH de diagnóstico de PTT. |
| [40533296](https://pubmed.ncbi.nlm.nih.gov/40533296/) | 2025 | Guía | J Thromb Haemost | Actualización 2025 de las guías ISTH 2020 para manejo de PTT. |
| [36053773](https://pubmed.ncbi.nlm.nih.gov/36053773/) | 2023 | Revisión sistemática/metaanálisis | Blood Adv | Añadir caplacizumab al tratamiento estándar en PTT: revisión sistemática y metaanálisis. |
| [37045600](https://pubmed.ncbi.nlm.nih.gov/37045600/) | 2023 | Revisión sistemática/metaanálisis | Expert Rev Hematol | Eficacia y seguridad de caplacizumab en el tratamiento de PTT. |
| [40235949](https://pubmed.ncbi.nlm.nih.gov/40235949/) | 2025 | Cohorte retrospectiva internacional | EClinicalMedicine | Proyecto Capla 1000+: uso de caplacizumab en aTTP inmunomediada a gran escala. |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Revisión | Blood | Revisión general de fisiopatología, diagnóstico y tratamiento de la PTT. |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Revisión | J Clin Med | Fisiopatología, diagnóstico y manejo de la PTT. |

## Información de Mercado en España

Caplacizumab no está actualmente comercializado en España (0 autorizaciones registradas en los datos disponibles).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. (Brecha de datos DG001, severidad *Blocking*: el prospecto/ficha técnica de la AEMPS aún no ha sido incorporado a este paquete, lo que impide la evaluación de seguridad inicial S1.)

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La señal de PTT cuenta con nivel de evidencia L1 (múltiples ensayos de Fase 2/3 completados, incluidos los pivotales HERCULES y TITAN) y mecanismo de acción coherente con la fisiopatología de la enfermedad. No obstante, persisten brechas críticas —posible confusión entre indicación "nueva" y ya aprobada, ausencia de ficha técnica AEMPS/TFDA (bloqueante) y ausencia total de comercialización en España— que impiden avanzar sin salvaguardas.

**Para avanzar se necesita:**
- Confirmar si la PTT adquirida es ya una indicación aprobada del fármaco en otras jurisdicciones (resolver la brecha de `original_indications`), para reclasificar correctamente esta señal como reposicionamiento genuino o como brecha de datos regulatorios.
- Obtener el prospecto/ficha técnica de la AEMPS (DG001, bloqueante) para completar la evaluación de seguridad S1.
- Completar los datos estructurados de mecanismo de acción vía DrugBank (DG002).
- Evaluar la vía de entrada al mercado español, dado que el fármaco no está actualmente comercializado (0 autorizaciones).
- Descartar formalmente las 9 señales adicionales de nivel L5 antes de asignarles recursos de investigación, dado que carecen de evidencia clínica o bibliográfica de soporte.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

