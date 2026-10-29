---
layout: default
title: Emicizumab
parent: Solo predicción del modelo (L5)
nav_order: 286
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-29
monitor_inn: "EMICIZUMAB"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "thrombotic thrombocytopenic purpura", "fetal and neonatal alloimmune thrombocytopenia", "flood factor deficiency"]
description: "Emicizumab: nueva indicación predicha, Pseudo-von Willebrand disease (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Emicizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Emicizumab: Pseudo-von Willebrand disease
{: .text-alpha }

## Resumen en Una Frase

Emicizumab es un anticuerpo biespecífico originalmente utilizado para el tratamiento de la hemofilia (incluida la forma sintomática en mujeres portadoras).
El modelo TxGNN predice que podría ser efectivo para el **déficit adquirido de factores de coagulación**, con un respaldo clínico concreto en **hemofilia A adquirida**: **20 publicaciones** (incluidos 3 estudios prospectivos de fase 2/3), sin ensayos clínicos registrados en los datos compilados.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Pseudo-von Willebrand disease |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 5 de 5) |
| Número de Autorizaciones | 5 (vigentes: 5) |
| Decisión Recomendada | Proceed with Guardrails |

**Nota sobre la selección:** la primera predicción del modelo (rank 1) es la pseudoenfermedad de von Willebrand (0.9999), pero carece de toda evidencia y su vínculo mecanístico es débil (L5, Hold). Este informe se centra en la predicción con mayor sustento: el déficit adquirido de factores de coagulación. Las demás predicciones se resumen al final.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información conocida, emicizumab es un anticuerpo biespecífico que une el factor IX activado (FIXa) y el factor X (FX), imitando la función del factor VIII activado (FVIIIa). Se une a FIXa con una constante de afinidad (KD) de 1,52 µM y a FXa con una KD de 0,98 µM.

En la hemofilia A congénita falta el FVIII; en la hemofilia A adquirida, autoanticuerpos neutralizan el FVIII endógeno. Como emicizumab no depende del FVIII y no es neutralizado por estos inhibidores, existe una justificación mecanística directa. De hecho, ya está aprobado para hemofilia A congénita con o sin inhibidores, y en Japón se ha estudiado en fase 3 para la hemofilia A adquirida.

Conviene precisar el alcance: la evidencia respalda la **hemofilia A adquirida** específicamente, no todos los déficits adquiridos de factores de coagulación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en los datos compilados. Los estudios prospectivos aparecen en la sección de literatura. Los datos de farmacología mencionan el ensayo de fase 3 NCT02622321, pero corresponde a hemofilia A congénita con inhibidores, no a la nueva indicación.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Estudio prospectivo fase III, multicéntrico, abierto | J Thromb Haemost | Primer estudio prospectivo de profilaxis con emicizumab en hemofilia A adquirida (Japón) |
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Fase 2, abierto, un solo brazo (GTH-AHA-EMI) | Lancet Haematol | Emicizumab previene hemorragias y permite posponer la inmunosupresión durante las primeras 12 semanas |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Estudio prospectivo, análisis final (AGEHA) | Thromb Haemost | Profilaxis con emicizumab con o sin inmunosupresión, incluidos pacientes no aptos para inmunosupresión |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | Cohorte | Blood Adv | Seguimiento a 2 años: beneficio sostenido en supervivencia al posponer la inmunosupresión |
| [38936699](https://pubmed.ncbi.nlm.nih.gov/38936699/) | 2024 | Cohorte comparativa | J Thromb Haemost | Emicizumab frente a terapia inmunosupresora en hemofilia A adquirida |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | Cohorte retrospectiva multicéntrica | Blood Adv | 62 pacientes de EE. UU. tratados fuera de indicación con emicizumab |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | Recomendaciones de consenso | Hamostaseologie | Recomendaciones del grupo GTH-AHA sobre el uso de emicizumab |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Revisión narrativa | J Thromb Haemost | Manejo de la hemofilia A adquirida en la era de emicizumab |
| [37276345](https://pubmed.ncbi.nlm.nih.gov/37276345/) | 2023 | Serie de casos | Haemophilia | Experiencia con emicizumab en hemofilia A adquirida |
| [41436689](https://pubmed.ncbi.nlm.nih.gov/41436689/) | 2025 | Reporte de caso | CEN Case Rep | Inicio de hemodiálisis con susoctocog alfa y emicizumab en hemofilia A adquirida |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181271001 | HEMLIBRA 30 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |
| 1181271002IP | HEMLIBRA 150 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |
| 1181271002IP1 | HEMLIBRA 150 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |
| 1181271002 | HEMLIBRA 150 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |
| 1181271002IP2 | HEMLIBRA 150 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |

Las cinco autorizaciones están vigentes (titular: Roche Registration GmbH).

## Consideraciones de Seguridad

- **Interacciones farmacológicas** (5 registradas):
  - **Complejo coagulante anti-inhibidor (aPCC): Mayor.** Es la interacción más relevante; se asocia a riesgo de microangiopatía trombótica y eventos trombóticos.
  - Factor antihemofílico recombinante humano: Moderada.
  - Factor VIIa recombinante humano: Moderada.
  - Factor X y factor IX de coagulación: interacciones farmacológicas con sus dianas (sin clasificación de gravedad).
- **Riesgo trombótico**: señalado en el análisis de la predicción, especialmente con agentes de bypass concomitantes y en pacientes ancianos con comorbilidades.
- **Limitaciones de laboratorio**: los ensayos de coagulación estándar pueden verse afectados por emicizumab.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay estudios prospectivos de fase 2/3 (GTH-AHA-EMI, estudio japonés de fase III y AGEHA) con un mecanismo directamente aplicable, pero son de un solo brazo, sin comparación aleatorizada y sin ensayos registrados en los datos compilados.

**Para avanzar se necesita:**
- Datos de mecanismo de acción y del prospecto de la AEMPS (advertencias y contraindicaciones), actualmente no disponibles.
- Evidencia comparativa o aleatorizada, y ensayos clínicos registrados.
- Plan de gestión del riesgo trombótico (evitar o vigilar estrechamente el uso con aPCC y agentes de bypass).
- Estrategia de monitorización de la erradicación del inhibidor y del laboratorio de coagulación.
- Delimitar la indicación a hemofilia A adquirida.

## Otras Predicciones del Modelo (todas con recomendación Hold salvo indicación)

| Enfermedad | Puntaje TxGNN | Nivel | Observación |
|------|------|------|------|
| Pseudoenfermedad de von Willebrand | 0.9999 | L5 | El mecanismo no corrige la ganancia de función de GP1BA; vínculo débil |
| Trastorno primario de liberación plaquetaria | 0.9999 | L5 | No corrige la secreción plaquetaria; beneficio solo especulativo |
| Trombastenia de Glanzmann | 0.9998 | L4 (Research Question) | Única referencia es una revisión de rFVIIa, evidencia indirecta |
| Síndrome de Scott | 0.9992 | L5 | Posible limitación por menor superficie procoagulante |
| Defecto del receptor de colágeno | 0.9986 | L5 | Mecanismo no relacionado |
| Trombocitopenia constitucional con hemorragia | 0.9985 | L5 | Mecanismo no relacionado |
| Púrpura trombótica trombocitopénica | 0.9961 | L5 | Posiblemente dañino por riesgo trombótico; probable falso positivo |
| Trombocitopenia aloinmune fetal y neonatal | 0.9952 | L5 | Mecanismo inmunitario no abordado |
| "Flood factor deficiency" | 0.9940 | L5 | Nombre ambiguo; requiere aclaración |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

