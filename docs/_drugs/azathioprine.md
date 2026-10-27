---
layout: default
title: Azathioprine
parent: Solo predicción del modelo (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Azathioprine: nueva indicación predicha, Síndrome de microftalmia colobomatosa-displasia rizomélica (nivel de evidencia L5). Indicación original: Artritis reumatoide (según las relaciones de indicaci…"
monitor_inn: "Azathioprine"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "osteoarthritis susceptibility", "WHIM syndrome", "granulomatous disease, chronic, autosomal recessive, 5", "osteoarthritis", "granulomatous disease with defect in neutrophil chemotaxis", "acromesomelic dysplasia, Hunter-Thompson type"]
---

# Azathioprine
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

## Azatioprina: De Artritis Reumatoide a Síndrome de Microftalmia Colobomatosa-Displasia Rizomélica
{: .text-alpha }

## Resumen en Una Frase

La azatioprina es un inmunosupresor antimetabolito de purinas, cuya indicación original en los datos compilados es la artritis reumatoide.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de microftalmia colobomatosa-displasia rizomélica**, una malformación del desarrollo muy poco frecuente.
Actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, por lo que se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide (según las relaciones de indicación del grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome de microftalmia colobomatosa-displasia rizomélica |
| Puntaje de Predicción TxGNN | 99.99% (posición 61 en el ranking del modelo) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la azatioprina es un inmunosupresor que actúa como antimetabolito de purinas, y su eficacia en enfermedades inmunomediadas como la artritis reumatoide está establecida.

En este caso, **no se identifica un vínculo mecanístico plausible**. El síndrome predicho es una malformación del desarrollo (ocular y esquelética) sin un componente inflamatorio o inmunomediado que la inmunosupresión pueda modificar. Una inmunosupresión basada en el metabolismo de purinas difícilmente corregiría un defecto estructural congénito.

El puntaje del modelo (99.99%) refleja una asociación calculada en el grafo de conocimiento, no evidencia clínica ni biológica. La similitud con la indicación original tampoco ha podido establecerse, por lo que esta predicción debe considerarse una señal estadística sin respaldo, no una hipótesis terapéutica sólida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 51003 | IMUREL 50 mg polvo para solución inyectable | Polvo para solución inyectable | No disponible en los datos compilados |
| 78164 | IMMUFALK 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 50043 | IMUREL 50 mg comprimidos recubiertos con película | Comprimido | No disponible en los datos compilados |
| 78165 | IMMUFALK 75 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

Las cuatro autorizaciones son de principio activo único y están vigentes. Ninguna está cancelada.

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto): pancreatitis, trombocitopenia, anemia (incluida la macrocítica), infecciones (fúngicas, dermatofitosis e infecciones en general), función renal alterada, linfomas (incluidos el linfoma primario del sistema nervioso central, el linfosarcoma y el linfoma hepatoesplénico de células T), trombosis de la vena hepática y síndrome de Budd-Chiari.
- **Interacciones farmacológicas**: se registraron 100 interacciones; entre las principales:
  - **Moderadas**: mesalazina, balsalazida, olsalazina y sulfasalazina.
  - **Leves**: acetato, gluconato y sulfato de zinc.
  - Otras interacciones, como anfotericina B, ácido acetilsalicílico, metformina u omeprazol, figuran sin nivel de gravedad definido.
- **Consideración adicional**: la azatioprina es mielosupresora e inmunosupresora. En enfermedades que ya cursan con citopenias o alteraciones inmunitarias, esto podría agravar el riesgo infeccioso.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni literatura que la respalden (nivel L5) y no existe un mecanismo plausible que vincule la inmunosupresión con una malformación congénita del desarrollo. Un puntaje alto del modelo no basta para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la azatioprina y una hipótesis biológica que conecte con esta enfermedad.
- Estudios preclínicos o mecanísticos que muestren un componente inmunomediado en este síndrome.
- Textos de indicaciones, advertencias y contraindicaciones del prospecto de la AEMPS.

**Nota de contexto:** dentro de las predicciones del mismo modelo, la **enfermedad inflamatoria intestinal** y la **colitis ulcerosa** sí cuentan con múltiples ensayos de Fase 3 y 4 y revisiones Cochrane (nivel L1, "Proceed with Guardrails"). Sin embargo, corresponden a un uso clínico ya establecido, por lo que serían un reposicionamiento de etiqueta más que un hallazgo nuevo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

