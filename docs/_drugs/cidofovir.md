---
layout: default
title: Cidofovir
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 4
---

# Cidofovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Cidofovir: De Infección por Citomegalovirus (CMV) a Colangitis Esclerosante

## Resumen en Una Frase

Cidofovir es un análogo nucleotídico antiviral utilizado en el tratamiento de infecciones por citomegalovirus (CMV).
El modelo TxGNN predice que podría ser efectivo para **Colangitis Esclerosante**,
pero **no existe actualmente ningún ensayo clínico ni publicación** que respalde esta dirección: la predicción se basa exclusivamente en el puntaje del modelo.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible en los datos (Cidofovir no está comercializado en España; el vínculo con CMV se infiere del contexto mecanístico reportado) |
| Nueva Indicacion Predicha | Colangitis Esclerosante (sclerosing cholangitis) |
| Puntaje de Prediccion TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion oficial de Cidofovir (dato marcado como brecha de alta prioridad). Según la información disponible en el propio evidence pack, Cidofovir es un análogo nucleotídico con actividad inhibidora de la ADN polimerasa del citomegalovirus (CMV), utilizado en el tratamiento de infecciones por este virus.

El razonamiento detrás de la predicción es indirecto: la infección por CMV en pacientes inmunodeprimidos puede provocar colangiopatías similares a la colangitis esclerosante (por ejemplo, la "AIDS cholangiopathy"). Esto establece una posible relación biológica teórica entre el mecanismo antiviral de Cidofovir y la nueva indicación predicha.

Sin embargo, esta relación es puramente teórica: no existe ningún ensayo clínico ni publicación que demuestre un efecto terapéutico directo de Cidofovir sobre la colangitis esclerosante. La predicción está impulsada únicamente por el puntaje del modelo TxGNN, sin respaldo de evidencia real.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Cabe señalar que la información oficial del prospecto/TFDA para Cidofovir aún no ha sido incorporada a este análisis (brecha de datos bloqueante), por lo que no puede completarse una evaluación de seguridad de nivel S1 con los datos actuales.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La predicción cuenta con un puntaje TxGNN muy alto (99.94%), pero no tiene ningún respaldo de ensayos clínicos ni literatura (evidencia L5), y el fármaco no está comercializado en España. Además, falta información regulatoria bloqueante (advertencias/contraindicaciones oficiales), por lo que no puede avanzar a una evaluación de seguridad.

**Para avanzar se necesita:**
- Obtener el prospecto oficial y datos de advertencias/contraindicaciones (brecha bloqueante DG001)
- Obtener datos detallados del mecanismo de acción (MOA) desde DrugBank (brecha DG002)
- Estudios preclínicos o de mecanismo que evalúen la relación entre CMV, colangiopatía asociada a CMV y colangitis esclerosante
- Nota adicional: de los 4 candidatos de reposicionamiento evaluados para Cidofovir (colangitis esclerosante, artritis reumatoide, y dos síndromes congénitos raros), ninguno superó el nivel L4 de evidencia y todos recibieron recomendación "Hold". El candidato con más literatura asociada (artritis reumatoide, L4) se basa mayormente en estudios sobre leflunomida, no sobre Cidofovir, por lo que su relevancia real es limitada.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

