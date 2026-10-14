---
layout: default
title: Foscarnet
parent: Solo predicción del modelo (L5)
nav_order: 358
evidence_level: L5
indication_count: 4
---

# Foscarnet
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Foscarnet: De Indicación Original No Disponible a Síndrome de Hematuria Familiar Autosómico Dominante con Tortuosidad Arteriolar Retiniana y Contracturas

## Resumen en Una Frase

Foscarnet es un antiviral de administración intravenosa que está comercializado en España; los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hematuria familiar autosómico dominante con tortuosidad arteriolar retiniana y contracturas**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, y el análisis mecanístico la considera probablemente un artefacto del grafo de conocimiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de las autorizaciones de la AEMPS |
| Nueva Indicación Predicha | Síndrome de hematuria familiar autosómico dominante con tortuosidad arteriolar retiniana y contracturas |
| Puntaje de Predicción TxGNN | 99,56 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según el conocimiento farmacológico general, foscarnet es un análogo del pirofosfato que inhibe la ADN polimerasa viral y la transcriptasa inversa.

La enfermedad predicha es un trastorno genético raro (vasculopatía relacionada con COL4A1) sin etiología viral. El análisis realizado concluye que **no existe un vínculo mecanístico que respalde la predicción**. El puntaje alto de TxGNN parece deberse a nodos de fenotipo retiniano compartidos en el grafo de conocimiento, y no a una justificación farmacológica.

Por tanto, esta predicción debe considerarse una señal computacional sin sustento biológico demostrado, y no una hipótesis de reposicionamiento plausible.

Otras predicciones del modelo tampoco muestran respaldo: enfermedad de vasos pequeños cerebrales tipo 1 (99,54 %), artritis reumatoide (99,52 %) y nefropatía diabética (99,43 %). En esta última existe además una preocupación de seguridad, ya que foscarnet es nefrotóxico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 88760 | Foscarnet Tillomed 24 mg/ml solución para perfusión EFG | Solución para perfusión | No disponible |
| 59712 | Foscavir 24 mg/ml solución para perfusión | Solución para perfusión | No disponible |
| 85153 | Foscarnet Kabi 24 mg/ml solución para perfusión EFG | Solución para perfusión | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto):** síndrome de QT largo (incluida la forma familiar), torsades de pointes, epilepsia, enfermedad renal, déficit de potasio, neutropenia y agranulocitosis (incluidas formas congénitas), hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo (hiperfosfatemia e hipofosfatemia) y anemia.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las de nivel **mayor** figuran anfotericina B (incluido el complejo lipídico), dolasetrón y bupropión. Entre las de nivel moderado se incluyen famotidina, omeprazol, rabeprazol, dexlansoprazol, claritromicina, loperamida, mesalazina, balsalazida y varios corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, beclometasona).
- Consultar el prospecto para información de seguridad adicional, ya que no se dispone de advertencias de etiqueta.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre un antiviral y una vasculopatía genética por defecto de colágeno IV. El puntaje alto parece un artefacto del grafo de conocimiento.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones)
- Completar los datos del mecanismo de acción desde DrugBank
- Justificación biológica independiente que vincule foscarnet con la patología de COL4A1 antes de considerar cualquier estudio
- Si se retomara el caso, evaluar la nefrotoxicidad y las alteraciones electrolíticas, que son riesgos relevantes para esta población
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

