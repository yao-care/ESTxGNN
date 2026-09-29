---
layout: default
title: Betamethasone
parent: Evidencia alta (L1-L2)
nav_order: 71
evidence_level: L2
indication_count: 10
---

# Betamethasone
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Betametasona: De Afecciones Inflamatorias de la Piel a Alopecia Areata

## Resumen en Una Frase

Betametasona es un corticoide sintético que se usa para tratar síntomas inflamatorios de la piel, como dermatitis atópica, seborreica y de contacto, y psoriasis.
El modelo TxGNN predice que podría ser efectivo para **alopecia areata**,
con **8 ensayos clínicos** (varios con betametasona solo como comparador) y **20 publicaciones** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Las autorizaciones no traen texto de indicación. Según los datos farmacológicos: afecciones inflamatorias de la piel (dermatitis, psoriasis, reacciones por picaduras) |
| Nueva Indicación Predicha | Alopecia areata |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según los datos farmacológicos disponibles, betametasona es un agonista del receptor de glucocorticoides (NR3C1) con actividad antiinflamatoria, antipruriginosa y vasoconstrictora. Su eficacia en enfermedades inflamatorias de la piel está comprobada, y mecanísticamente podría ser aplicable a la alopecia areata.

La alopecia areata es una enfermedad autoinmune crónica en la que las células T atacan el folículo piloso y provocan pérdida de cabello sin cicatriz. Un glucocorticoide potente puede frenar ese ataque inmunitario y ayudar a restablecer el privilegio inmune del folículo. Por eso los corticoides son un tratamiento establecido en esta enfermedad, y se usan por vía tópica, intralesional y como minipulsos orales.

Este vínculo se apoya en la farmacología de clase y en los datos clínicos, no en un MOA específico de DrugBank. Las propias pruebas piden cautela por tres razones:
- Los estudios son pequeños (30-60 pacientes).
- En muchos, betametasona es el comparador y no el brazo experimental.
- No hay ensayos de Fase 3.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Fase 2 | Completado | 60 | Azatioprina en pulso semanal vs minipulso oral de betametasona en alopecia areata moderada a grave |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Fase 4 | Completado | 50 | Latanoprost tópico vs corticoide tópico (probablemente betametasona) en alopecia areata localizada |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Fase 4 | Completado | 40 | Minoxidil 5% más corticoide tópico potente vs triamcinolona intralesional en alopecia areata |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | Desconocido | 59 | Cetirizina tópica 1% vs valerato de betametasona 0.1% en alopecia areata localizada |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Fase 1 | Desconocido | 60 | Pentoxifilina 2% y metformina 10% en gel vs valerato de betametasona 0.1% en crema, en alopecia areata en placas |
| [NCT07696585](https://clinicaltrials.gov/study/NCT07696585) | N/A | Aún no reclutando | 60 | Terapia tópica con metformina 30%, simvastatina 2% y valerato de betametasona 0.1% en alopecia areata en placas; sin resultados |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Fase 4 | Reclutando | 250 | Comparación de tratamientos en alopecia cicatricial centrífuga central; relevancia solo indirecta |
| [NCT01111981](https://clinicaltrials.gov/study/NCT01111981) | Fase 4 | Desconocido | 30 | Espuma de clobetasol 0.05% en alopecia cicatricial centrífuga central; otro fármaco y otra enfermedad, relevancia indirecta |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | ECA | J Am Acad Dermatol | Administración transdérmica con microagujas de betametasona compuesta en alopecia areata, como alternativa menos dolorosa a la inyección intralesional |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | ECA | Iran J Pharm Res | Betametasona oral en pulso (3 mg semanales), metotrexato o ambos, contra placebo, en 36 pacientes con alopecia areata grave |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | ECA | Dermatol Ther | Latanoprost frente a minoxidil, betametasona y sus combinaciones en 6 grupos de 18 pacientes |
| [40510104](https://pubmed.ncbi.nlm.nih.gov/40510104/) | 2025 | ECA | Cureus | Ciclosporina oral vs minipulso de betametasona en 60 pacientes con alopecia areata |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | ECA | J Dermatolog Treat | Betametasona vs triamcinolona intralesionales en alopecia areata localizada, con diseño intrapaciente |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Metaanálisis en red | Cochrane Database Syst Rev | Comparación de tratamientos para alopecia areata (inmunosupresores, estimulantes del crecimiento e inmunoterapia de contacto) |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Revisión | Dermatol Pract Concept | Eficacia, recaídas y efectos adversos de la terapia de pulsos de corticoides en alopecia areata |
| [31516138](https://pubmed.ncbi.nlm.nih.gov/31516138/) | 2019 | Estudio clínico comparativo | Indian J Dermatol | Azatioprina semanal vs minipulso oral de betametasona en alopecia areata moderada a grave |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | Estudio comparativo | Cureus | Dipropionato de betametasona tópico vs minoxidil tópico en alopecia areata |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | Estudio clínico | Cureus | Eficacia y seguridad de minipulsos orales de betametasona en alopecia areata moderada a grave |

## Información de Mercado en España

Los registros disponibles no incluyen el texto de indicación aprobada, por lo que esa columna se omite. Se muestran 5 de las 10 autorizaciones.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 82407 | CORTITAPE 2,250 MG APÓSITO ADHESIVO MEDICAMENTOSO | Apósito adhesivo medicamentoso |
| 55041 | DIPRODERM 0,5 mg/g POMADA | Pomada |
| 80594 | BETAMETASONA SONPHAR 0,5 MG/ML GOTAS ORALES EN SOLUCIÓN EFG | Gotas orales en solución |
| 40576 | BETNOVATE 1 mg/g CREMA | Crema |
| 40628 | CELESTONE CRONODOSE SUSPENSIÓN INYECTABLE | Suspensión inyectable |

Las formas disponibles cubren las vías tópica, oral e inyectable. Esto es coherente con los tres modos de uso descritos en la alopecia areata: crema tópica, minipulso oral e inyección intralesional.

## Consideraciones de Seguridad

- **Advertencias del uso propuesto**: las pautas orales en pulso conllevan los riesgos propios de los corticoides sistémicos, y tras suspender el tratamiento son frecuentes las recaídas.

Para el resto de la información de seguridad (advertencias, contraindicaciones e interacciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 2 completado con minipulso oral de betametasona y varios ECA publicados con betametasona en alopecia areata, todos pequeños, lo que da un nivel L2. La plausibilidad mecanística es alta, pero no hay Fase 3 y en muchos estudios betametasona es solo el comparador.

**Para avanzar se necesita:**
- Datos de MOA de DrugBank y el prospecto de AEMPS (advertencias y contraindicaciones) para completar el cribado de seguridad
- Ensayos controlados más grandes, idealmente de Fase 3, con betametasona como brazo experimental
- Un plan de seguimiento de seguridad y de recaídas para las pautas orales en pulso
- Aclarar la vía y la formulación preferentes (tópica, intralesional u oral) para esta indicación

**Otras predicciones del modelo:** las demás indicaciones tienen puntajes TxGNN similares pero una evidencia muy inferior, así que no se recomienda avanzar con ellas por ahora. Ninguna cuenta con ensayos clínicos.
- Mucinosis folicular (alopecia mucinosa), efluvio telógeno y foliculitis decalvante: Hold (L4)
- Los síndromes genéticos raros de alopecia o hipotricosis, la alopecia con deficiencia de anticuerpos y el síndrome nefrótico esteroide-resistente: Hold (L5)
- Síndrome nefrótico idiopático esteroide-sensible: pregunta de investigación (L3). Solo hay un reporte pediátrico de 1981 y prednisolona ya es el agente establecido.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

