---
layout: default
title: Mebendazole
parent: Solo predicción del modelo (L5)
nav_order: 338
evidence_level: L5
indication_count: 1
---

# Mebendazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Mebendazol: De Uso Antiparasitario a Acné

## Resumen en Una Frase

Mebendazol es un benzimidazol comercializado en España como LOMPER (suspensión oral y comprimidos). Los datos de autorización recibidos no incluyen el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para **acné**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de autorización (el texto de indicación está vacío) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99.20% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción ni sobre las indicaciones originales registradas. Por eso el vínculo del grafo de conocimiento no puede contrastarse con un mecanismo documentado. El puntaje de TxGNN es alto (0.992), pero un puntaje de modelo no es evidencia clínica.

Se pueden plantear dos hipótesis, ninguna respaldada por los datos recibidos:

1. Mebendazol es un benzimidazol que inhibe la polimerización de la tubulina. Además, se ha descrito que puede modular la vía de señalización Hedgehog, implicada en el desarrollo de las glándulas sebáceas.
2. Podría tener efectos antiinflamatorios relevantes para las lesiones inflamatorias del acné.

Hay una limitación práctica importante: el mebendazol oral tiene baja biodisponibilidad sistémica, por lo que alcanzar dianas en la piel sería incierto. Una formulación tópica requeriría un estudio independiente.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 53775 | LOMPER 20 mg/ml SUSPENSIÓN ORAL | Suspensión oral | No consta en los datos recibidos |
| 51200 | LOMPER 100 mg COMPRIMIDOS | Comprimido | No consta en los datos recibidos |

Ambas autorizaciones pertenecen a Esteve Pharmaceuticals S.A.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La ausencia de interacciones farmacológicas registradas probablemente refleja datos faltantes y no demuestra que no existan. Por eso la seguridad para este uso aún no puede evaluarse.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, faltan el mecanismo de acción y la información de seguridad del prospecto, así que no hay base para avanzar.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un dato bloqueante para el cribado de seguridad.
- Obtener el mecanismo de acción desde DrugBank para evaluar el vínculo mecanístico con el acné.
- Obtener el texto de las indicaciones aprobadas de las dos autorizaciones.
- Realizar una búsqueda dirigida de ensayos clínicos y literatura sobre mebendazol en acné.
- Evaluar la viabilidad de llegar a la piel (biodisponibilidad oral baja; posible formulación tópica).
- Completar los datos de interacciones farmacológicas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

