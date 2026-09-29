---
layout: default
title: Reslizumab
parent: Solo predicción del modelo (L5)
nav_order: 464
evidence_level: L5
indication_count: 2
---

# Reslizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Reslizumab: De Anticuerpo Anti-IL-5 a Trombocitopenia por Destrucción Inmune

## Resumen en Una Frase

Reslizumab es un anticuerpo monoclonal anti-IL-5 que reduce los eosinófilos. En el Evidence Pack no consta su indicación original ni el texto de indicación de su autorización en España.
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia por destrucción inmune**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Trombocitopenia por destrucción inmune |
| Puntaje de Predicción TxGNN | 99.53% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, reslizumab es un anticuerpo monoclonal anti-IL-5 que reduce los eosinófilos. Su eficacia se asocia a enfermedades mediadas por eosinófilos, y mecanísticamente su aplicabilidad a la nueva indicación es, por ahora, solo una hipótesis.

Hoy no se ha documentado ningún vínculo mecanístico ni clínico entre la vía IL-5/eosinófilos y la destrucción plaquetaria inmune. La trombocitopenia inmune se explica sobre todo por autoanticuerpos y desregulación de linfocitos T, y no se conoce un papel establecido de la IL-5 en ella.

El puntaje alto de TxGNN (99.53%) proviene únicamente de una predicción basada en grafos de conocimiento. Debe tratarse como una señal para generar hipótesis y no como prueba de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

*Nota:* para otra indicación predicha (trastorno primario de liberación plaquetaria, puntaje 99.25%, nivel L4) solo existe una revisión de 2010 sobre el síndrome hipereosinofílico y mepolizumab, otro anticuerpo anti-IL-5 ([PMID 20565230](https://pubmed.ncbi.nlm.nih.gov/20565230/)). Ofrece contexto general sobre el bloqueo de IL-5, pero no aborda la función plaquetaria.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 1161125001 | CINQAERO 10 MG/ML | Concentrado para solución para perfusión | Teva B.V. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene respaldo de ensayos clínicos ni de literatura (nivel L5) y no hay un vínculo mecanístico plausible entre el bloqueo de IL-5 y la trombocitopenia inmune. El puntaje alto del modelo no basta por sí solo para avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS para completar la revisión de seguridad, lo que actualmente bloquea el cribado de seguridad.
- Completar los datos de mecanismo de acción e indicación original desde DrugBank.
- Buscar evidencia preclínica o clínica que conecte la vía IL-5/eosinófilos con la destrucción plaquetaria inmune.
- Evaluar la compatibilidad de vías de administración, hoy pendiente (reslizumab se presenta como perfusión intravenosa).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

