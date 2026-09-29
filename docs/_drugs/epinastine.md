---
layout: default
title: Epinastine
parent: Solo predicción del modelo (L5)
nav_order: 204
evidence_level: L5
indication_count: 2
---

# Epinastine
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

# Epinastina: De Conjuntivitis Alérgica a Conjuntivitis por Rosácea

## Resumen en Una Frase

La epinastina es un antihistamínico H1 que se usa en colirio para tratar el picor asociado a la conjuntivitis alérgica.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis por rosácea**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Conjuntivitis alérgica (según el uso clínico descrito en la fuente de farmacología; el texto de indicación de la autorización de la AEMPS está vacío) |
| Nueva Indicación Predicha | Conjuntivitis por rosácea |
| Puntaje de Predicción TxGNN | 99,57% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, la epinastina es un antagonista del receptor H1 de la histamina (diana HRH1 en la base de datos de farmacología). Además tiene actividad estabilizadora de mastocitos, y su eficacia en la conjuntivitis alérgica está comprobada. Mecanísticamente podría ser aplicable a la conjuntivitis por rosácea.

La conjuntivitis alérgica y la afectación ocular de la rosácea comparten inflamación de la superficie ocular. Por eso es plausible que un fármaco que reduce la liberación de mediadores de los mastocitos y bloquea la histamina tenga algún efecto. La vía de administración actual, un colirio, también es coherente con una enfermedad de la superficie ocular.

Este vínculo es solo una hipótesis. No hay ensayos ni publicaciones que lo apoyen, y el mecanismo no se ha verificado contra DrugBank. La similitud con la indicación original tampoco se ha evaluado formalmente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 65574 | RELESTAT 0,5 mg/ml COLIRIO EN SOLUCIÓN (Abbvie Spain, S.L.U.) | Colirio en solución | No especificada en los datos recibidos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99,57%), pero es la única base: no hay ensayos clínicos ni literatura sobre conjuntivitis por rosácea (nivel L5). Tampoco están disponibles las advertencias y contraindicaciones del prospecto de la AEMPS, así que no se puede avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación autorizada)
- Obtener el mecanismo de acción desde DrugBank y verificar el vínculo con la inflamación ocular en rosácea
- Buscar estudios preclínicos o clínicos sobre epinastina en rosácea ocular
- Evaluar formalmente la similitud con la indicación original y la compatibilidad de vía (colirio)

**Nota:** la segunda predicción del modelo, **urticaria alérgica** (puntaje 99,28%), tiene más respaldo: 2 estudios observacionales poscomercialización (n = 2001 y n = 3793), revisiones y estudios farmacodinámicos de habón y eritema, con nivel L3 y recomendación "Proceed with Guardrails". Sin embargo, el uso poscomercialización sugiere que ya podría ser una indicación aprobada en otros mercados, por lo que no sería un reposicionamiento genuino. Conviene revisarla como un informe separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

