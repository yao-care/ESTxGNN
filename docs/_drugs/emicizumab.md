---
layout: default
title: Emicizumab
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab: De Hemofilia A Congénita a Deficiencia Adquirida de Factor de Coagulación (Hemofilia A Adquirida)

> **Nota metodológica:** Este Evidence Pack es de tipo *multi-indicación* (`TW-DB13923-multi`): TxGNN generó **10 hipótesis** de reposicionamiento para emicizumab. Sin embargo, la puntuación TxGNN **no se correlaciona con la evidencia real** — las 4 hipótesis con score más alto (rank 1-2, 4) carecen por completo de ensayos clínicos o literatura de respaldo (Nivel L5), mientras que la hipótesis en 5º lugar (*acquired coagulation factor deficiency*) cuenta con 2 ensayos clínicos y 20 publicaciones, incluyendo varios ensayos Fase III. Por esta razón, este informe destaca **esa indicación** como candidato principal y resume las 9 restantes en una sección aparte al final.

---

## Resumen en Una Frase

Emicizumab es un anticuerpo biespecífico ya conocido en la literatura como tratamiento para la **hemofilia A congénita** (con o sin inhibidores del Factor VIII), donde actúa imitando la función cofactor del Factor VIII activado. El modelo TxGNN, junto con evidencia clínica real ya existente, señala que emicizumab podría ser eficaz para la **deficiencia adquirida de factor de coagulación** (correlato clínico: hemofilia A adquirida), con **1 ensayo clínico de registro** y **20 publicaciones**, incluyendo dos ensayos Fase III abiertos y guías de consenso, respaldando actualmente esta dirección. Las restantes 9 hipótesis predichas por TxGNN no cuentan con ningún ensayo clínico ni literatura de apoyo y deben mantenerse en espera.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia A (congénita, con o sin inhibidores) — inferida del contexto de la literatura incluida en este pack, ya que no hay registro de licencias en España |
| Nueva Indicación Predicha | Deficiencia Adquirida de Factor de Coagulación (correlato clínico: Hemofilia A Adquirida) — indicación destacada de entre 10 hipótesis TxGNN, seleccionada por fortaleza de evidencia real |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción de emicizumab en la base DrugBank de este pack (marcado como *Data Gap* bloqueante, ítem DG002). No obstante, la literatura y el análisis de reposicionamiento incluidos en este mismo Evidence Pack describen consistentemente a emicizumab como un **anticuerpo biespecífico que imita la función cofactor del Factor VIII activado (FVIIIa)**, puenteando el Factor IXa y el Factor X para reconstituir el complejo "tenasa" y restaurar la generación de trombina — es decir, actúa sobre la vía de la **hemostasia secundaria**, independientemente de la presencia de anticuerpos inhibidores contra el Factor VIII endógeno.

La deficiencia adquirida de factor de coagulación (en la práctica clínica, hemofilia A adquirida) se produce cuando autoanticuerpos neutralizan el Factor VIII propio del paciente. Dado que emicizumab **no depende del Factor VIII nativo** para ejercer su función — actúa como un sustituto molecular externo — el mecanismo es directamente aplicable a este escenario: puentea la vía de coagulación aun cuando el Factor VIII endógeno esté inhibido por autoanticuerpos. Esta lógica mecanística ya ha sido validada clínicamente: múltiples ensayos Fase III abiertos (GTH-AHA-EMI, AGEHA) han demostrado que emicizumab previene sangrados en hemofilia A adquirida y permite posponer la inmunosupresión sistémica, tratamiento estándar históricamente asociado a alta morbimortalidad por infecciones.

Es importante señalar que este mecanismo **no es generalizable** a todo el resto de trastornos hemorrágicos evaluados por TxGNN en este pack: enfermedades de hemostasia primaria (defectos plaquetarios, de receptores de colágeno, tromboastenia de Glanzmann) no involucran la vía FIXa-FX sobre la que actúa emicizumab, y en el caso de la púrpura trombótica trombocitopénica, el mecanismo procoagulante de emicizumab representa un **riesgo de seguridad**, no una oportunidad terapéutica (ver sección "Otras Indicaciones Predichas").

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) | N/A | Reclutando | 3000 | ATHN Transcends: estudio de cohorte de historia natural en trastornos hematológicos no neoplásicos. No es un ensayo intervencionista de emicizumab, pero cubre la población de hemofilia A adquirida y puede aportar datos de seguridad/efectividad del mundo real (relevancia grado B). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Ensayo Fase III abierto (GTH-AHA-EMI) | The Lancet Haematology | Emicizumab protegió del sangrado y permitió diferir el inicio de inmunosupresión durante las primeras 12 semanas en pacientes con hemofilia A adquirida |
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Ensayo Fase III abierto, prospectivo, multicéntrico | Journal of Thrombosis and Haemostasis | Primer estudio prospectivo Fase III de profilaxis con emicizumab en hemofilia A adquirida; hasta entonces no existían estudios controlados en esta población |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Análisis final Fase III (Estudio AGEHA) | Thrombosis and Haemostasis | Perfil beneficio-riesgo favorable de emicizumab en profilaxis, incluyendo pacientes no elegibles para inmunosupresión y seguimiento a largo plazo |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | Consenso/Guía (Grupo de Trabajo GTH-AHA) | Hämostaseologie | Recomendaciones de consenso: el estudio GTH-AHA-EMI demostró que emicizumab previene sangrados y permite posponer la inmunosupresión |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | Cohorte multicéntrica del mundo real (EE.UU.) | Blood Advances | 62 pacientes tratados off-label con emicizumab (mediana de 10 semanas) en 12 centros de hemofilia de EE.UU. |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | Cohorte de seguimiento/supervivencia | Blood Advances | Datos a 2 años del estudio GTH-AHA-EMI: beneficio de supervivencia sostenido con emicizumab y aplazamiento de inmunosupresión |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Revisión narrativa | Journal of Thrombosis and Haemostasis | Revisión del manejo de hemofilia A adquirida en la era de emicizumab; uso creciente tras su aprobación en hemofilia A congénita |
| [38562115](https://pubmed.ncbi.nlm.nih.gov/38562115/) | 2024 | Revisión | Haemophilia | Avances en manejo de hemofilia A adquirida y trastornos hemostáticos relacionados; los pacientes ahora se benefician de profilaxis con emicizumab |
| [36795341](https://pubmed.ncbi.nlm.nih.gov/36795341/) | 2023 | Revisión/Comentario | Blood Transfusion | Pros y contras del nuevo enfoque de emicizumab para prevención y tratamiento del sangrado en hemofilia A adquirida |
| [39401737](https://pubmed.ncbi.nlm.nih.gov/39401737/) | 2025 | Estudio de caso | Journal of Thrombosis and Haemostasis | Evaluación detallada de anticuerpos anti-emicizumab en un caso de hemofilia A adquirida; eficacia hemostática prometedora, con desarrollo de anticuerpos anti-fármaco en una minoría de pacientes |

*(Se identificaron 10 publicaciones adicionales sobre este tema en el pack, mayormente revisiones generales sobre hemofilia A adquirida sin foco específico en emicizumab; se omiten aquí por redundancia.)*

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

⚠️ **Aviso importante:** la evaluación de seguridad de emicizumab está actualmente **bloqueada** (ítem DG001, severidad *Blocking*): aunque se localizó el prospecto TFDA, sus advertencias y contraindicaciones aún no han sido extraídas ni integradas en este pack. No debe avanzarse a la etapa de evaluación de seguridad (S1) sin completar este paso. Cabe destacar, además, que la literatura sobre reposicionamiento de emicizumab documentada en este mismo pack (indicación "thrombotic thrombocytopenic purpura", ver más abajo) señala un riesgo teórico de eventos trombóticos asociado a su actividad procoagulante, que deberá verificarse formalmente contra el prospecto una vez disponible.

---

## Otras Indicaciones Predichas (Evidencia Insuficiente)

Las siguientes 9 hipótesis fueron generadas por TxGNN con puntuaciones muy altas (>99%), pero **ninguna cuenta con ensayos clínicos ni literatura de respaldo** (salvo la excepción parcial indicada), por lo que se recomienda **Hold** (mantener en espera) para la mayoría:

| Rank | Indicación Predicha | Score TxGNN | Nivel Evidencia | Decisión | Comentario |
|------|------|------|------|------|------|
| 1 | Enfermedad de pseudo-von Willebrand | 99.99% | L5 | Hold | Defecto de hemostasia primaria (receptor GPIb); sin relación mecanística directa con emicizumab |
| 2 | Trastorno primario de liberación plaquetaria | 99.99% | L5 | Hold | Defecto de gránulos plaquetarios; sin relación mecanística ni evidencia |
| 3 | Tromboastenia de Glanzmann | 99.98% | L4 | Research Question | Defecto de receptor GPIIb/IIIa; analogía mecanística débil, tratamiento estándar actual son agentes bypass (rFVIIa) |
| 4 | Síndrome de Scott | 99.92% | L5 | Hold | Déficit de exposición de fosfolípidos procoagulantes; podría **limitar** la eficacia de emicizumab en lugar de beneficiarse |
| 6 | Diátesis hemorrágica por defecto del receptor de colágeno (GPVI) | 99.86% | L5 | Hold | Defecto de adhesión plaquetaria; sin relación mecanística ni evidencia |
| 7 | Trastorno hemorrágico por trombocitopenia constitucional | 99.85% | L5 | Hold | Problema de cantidad plaquetaria; emicizumab no actúa sobre recuento plaquetario |
| 8 | Púrpura trombótica trombocitopénica (PTT) | 99.61% | L5 | Hold | ⚠️ Patología de **trombosis excesiva** (déficit de ADAMTS13); la actividad procoagulante de emicizumab sugiere riesgo de seguridad, no oportunidad terapéutica |
| 9 | Trombocitopenia aloinmune fetal y neonatal | 99.52% | L5 | Hold | Mecanismo inmunológico de destrucción plaquetaria; sin relación con la vía de coagulación de emicizumab |
| 10 | Deficiencia de factor de coagulación (nombre posiblemente mal capturado en los datos de origen) | 99.40% | L5 | Research Question | Denominación ambigua; requiere aclarar la enfermedad exacta antes de evaluar |

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
- La indicación de deficiencia adquirida de factor de coagulación (hemofilia A adquirida) cuenta con **evidencia clínica sustancial**: dos ensayos Fase III abiertos (GTH-AHA-EMI, AGEHA) y una recomendación de consenso de un grupo de trabajo especializado, mecanísticamente coherentes con la función conocida de emicizumab.
- Sin embargo, se trata de diseños **abiertos, de un solo brazo** (no aleatorizados controlados), el medicamento **no está registrado ni comercializado en España** para ninguna indicación, y la evaluación de seguridad está **bloqueada** por falta de datos del prospecto (DG001). Por ello no se recomienda un "Go" pleno, sino avanzar con salvaguardas.

**Para avanzar se necesita:**
- Completar la extracción de advertencias y contraindicaciones del prospecto TFDA/AEMPS para desbloquear la evaluación de seguridad S1 (DG001)
- Obtener datos estructurados del mecanismo de acción directamente desde DrugBank (DG002)
- Confirmar el estado de registro/comercialización de emicizumab en España, dado que actualmente no figura ninguna autorización
- Evaluar formalmente el riesgo tromboembólico (relevante especialmente frente a la hipótesis de PTT, donde el uso estaría contraindicado en lugar de indicado)
- Aclarar la denominación de la indicación de rank 10 ("flood factor deficiency"), probablemente un error de captura de datos
- Diseñar un plan de monitorización de seguridad (eventos trombóticos, anticuerpos anti-fármaco) antes de cualquier uso fuera de indicación en hemofilia A adquirida
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

