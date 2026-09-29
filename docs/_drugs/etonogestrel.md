---
layout: default
title: Etonogestrel
parent: Evidencia moderada (L3-L4)
nav_order: 219
evidence_level: L4
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

# Etonogestrel: De Indicación Original No Registrada a Amenorrea

## Resumen en Una Frase

Etonogestrel es un progestágeno utilizado en el implante anticonceptivo Implanon NXT, comercializado en España. El texto de indicación aprobada no figura en los datos disponibles.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, con **1 ensayo clínico** (indirecto) y **2 publicaciones** recuperadas, de las cuales solo una guarda relación con el fármaco. La señal probablemente refleja un efecto conocido del implante sobre el patrón de sangrado y no una indicación terapéutica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99,84% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, etonogestrel es un progestágeno que suprime la ovulación y provoca atrofia endometrial. Su uso establecido es la anticoncepción mediante implante subdérmico.

La amenorrea es un efecto bien documentado del implante, pero es un efecto sobre el patrón de sangrado, no un objetivo terapéutico. Por ello, el alto puntaje de TxGNN probablemente refleja una asociación fármaco-fenotipo (efecto adverso o cambio del patrón de sangrado) y no una señal de tratamiento. Esta predicción debe interpretarse con cautela.

Las otras cuatro predicciones (enfermedad fibroquística de mama, adenosis apocrina, adenosis de conducto romo y displasia mamaria benigna) tienen puntajes entre 99,2% y 99,6%, pero carecen de ensayos y literatura. Se consideran preguntas de investigación o hipótesis por vecindad en el grafo, sin respaldo clínico.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Fase 3 | Completado | 498 | Estudio de un solo brazo, abierto, sobre eficacia anticonceptiva y seguridad del implante de etonogestrel (MK-8415) en el cuarto y quinto año de uso, en mujeres de 35 años o menos. No es un ensayo de tratamiento de la amenorrea; a lo sumo aporta datos de patrón de sangrado (evidencia indirecta). |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | ECA | Contraception | Estudio aleatorizado multicéntrico en China (200 mujeres) que compara el implante de una varilla (Implanon) con el de seis cápsulas (Norplant) en eficacia anticonceptiva, tolerabilidad y patrón de sangrado. No hubo embarazos. Evidencia indirecta. |

Nota: se recuperó otra publicación (PMID 33430924, protocolo de un ECA sobre BIO101 en COVID-19), que no guarda relación con etonogestrel ni con esta indicación y se excluye.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62628 | IMPLANON NXT 68 mg IMPLANTE (Organon Salud S.L.) | Implante | No disponible en los datos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se dispone de datos de interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción más fuerte (amenorrea) parece reflejar un efecto conocido del implante sobre el sangrado y no un beneficio terapéutico, y las demás predicciones carecen de cualquier evidencia clínica. El único ensayo es indirecto y no evalúa amenorrea como objetivo de tratamiento.

**Para avanzar se necesita:**
- Obtener del prospecto de la AEMPS las advertencias, contraindicaciones y la indicación aprobada (bloqueante para el cribado de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir si la amenorrea se busca como beneficio terapéutico (por ejemplo, en sangrado uterino anómalo) y, en ese caso, buscar estudios que la evalúen como desenlace primario.
- Revisar la seguridad de la exposición sistémica a progestágenos en tejido mamario antes de explorar las indicaciones de patología mamaria benigna.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

