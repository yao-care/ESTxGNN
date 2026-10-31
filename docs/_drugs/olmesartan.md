---
layout: default
title: Olmesartan
parent: Solo predicción del modelo (L5)
nav_order: 586
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Olmesartan: nueva indicación predicha, Angina de Prinzmetal (nivel de evidencia L5). Indicación original: No disponible en los datos de autorización compilados"
monitor_inn: "olmesartan"
predicted_indications: ["Prinzmetal angina", "hypotrichosis simplex of the scalp", "migraine disorder", "alopecia", "pulmonary hypertension", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "kyphoscoliotic heart disease", "open-angle glaucoma"]
---

# Olmesartan
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

## Olmesartán: De Hipertensión Arterial a Angina de Prinzmetal
{: .text-alpha }

## Resumen en Una Frase

Olmesartán es un antagonista del receptor de angiotensina II tipo 1 (ARA-II), comercializado en España como medicamento antihipertensivo. El modelo TxGNN predice que podría ser efectivo para la **angina de Prinzmetal**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción concreta; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización compilados (el texto de indicación está vacío en todas las licencias) |
| Nueva Indicación Predicha | Angina de Prinzmetal |
| Puntaje de Predicción TxGNN | 0,9984 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 10) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, olmesartán pertenece a la clase de los antagonistas del receptor AT1 de la angiotensina II, y su uso en el control de la presión arterial está bien establecido.

Una hipótesis plausible, pero **no verificada**, es que el bloqueo del receptor AT1 podría reducir el tono vasoespástico y la disfunción endotelial, procesos implicados en la angina vasoespástica. Esta idea es especulativa y no está respaldada por ningún dato aportado: no hay ensayos ni literatura sobre olmesartán en angina de Prinzmetal.

La similitud con la indicación original queda pendiente de evaluación. El puntaje alto de TxGNN (0,9984) refleja una predicción del modelo TxGNN (aprendizaje profundo), no una confirmación clínica.

### Otras indicaciones predichas (contexto)

Los datos compilados incluyen otras predicciones; las que tienen algún respaldo son:

| Indicación | Puntaje TxGNN | Nivel | Evidencia disponible |
|------|------|------|------|
| Migraña | 0,9964 | L3 | Estudio pequeño en pacientes hipertensos/prehipertensos (2006), carta/comentario y revisión de clase IECA/ARA-II (2019); sin ensayos registrados |
| Hipertensión pulmonar | 0,9961 | L4 | Estudios preclínicos en roedores; sin datos en humanos |
| Glaucoma de ángulo abierto | 0,9940 | L4 | Solo una revisión indirecta (2009) |

El resto de predicciones (hipotricosis, alopecia, migraña con aura de tronco encefálico, cardiopatía kifoescoliótica, entre otras) carecen de evidencia y son nivel L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para angina de Prinzmetal.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para angina de Prinzmetal.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de medicamento con un único principio activo). Los datos compilados no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 79926 | Olmesartan Viatris 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 87977 | Olmesartan Ratio 40 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 85107 | Olmadur 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 036026110 | Ixia 40 mg comprimidos recubiertos | Comprimido recubierto | No disponible |
| 82425 | Olseron 40 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 94 interacciones en total. Entre las listadas:
  - **Gravedad mayor**: cloruro de potasio y bicarbonato de potasio (riesgo de hiperpotasemia).
  - **Gravedad moderada**: hidrocortisona, eluxadolina, exenatida, diversas formulaciones de insulina (humana, aspart, degludec, detemir, glargina, glulisina, lispro) y polietilenglicol 3350 con electrolitos.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para angina de Prinzmetal tiene un puntaje alto de TxGNN, pero no cuenta con ensayos clínicos ni literatura; es solo una predicción computacional (L5) con un mecanismo especulativo.

**Para avanzar se necesita:**
- Revisión sistemática de literatura sobre ARA-II y angina vasoespástica.
- Datos del mecanismo de acción del fármaco.
- Advertencias y contraindicaciones del prospecto de la AEMPS.
- Texto de indicación aprobada de las autorizaciones españolas.
- Si se desea avanzar con una indicación alternativa, la migraña (L3) es la que tiene más respaldo, aunque limitado a estudios pequeños, y con el posible factor de confusión de la reducción de la presión arterial.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

