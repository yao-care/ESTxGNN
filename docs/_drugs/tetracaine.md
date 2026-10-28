---
layout: default
title: Tetracaine
parent: Solo predicción del modelo (L5)
nav_order: 785
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Tetracaine"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "bronchitis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "hydroa vacciniforme, familial", "amyopathic dermatomyositis", "cauda equina syndrome", "irritable bowel syndrome"]
description: "Tetracaine: nueva indicación predicha, Acrodermatitis crónica atrófica (acrodermatitis chronica atrophicans) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Tetracaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Tetracaine: Acrodermatitis crónica atrófica (acrodermatitis chronica atrophicans)
{: .text-alpha }

## Resumen en Una Frase

La tetracaína es un anestésico local de tipo éster, originalmente asociado al tratamiento de la dermatitis y comercializado en España en formulaciones tópicas.
El modelo TxGNN predice que podría ser efectiva para **acrodermatitis crónica atrófica**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta predicción: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Acrodermatitis crónica atrófica (acrodermatitis chronica atrophicans) |
| Puntaje de Predicción TxGNN | 0.9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 2 de 3) |
| Número de Autorizaciones | 3 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, la tetracaína es un anestésico local de tipo éster que actúa bloqueando los canales de sodio, con efecto sintomático (anestesia tópica o espinal), y su uso en dermatitis se relaciona con el alivio local de síntomas.

Para la acrodermatitis crónica atrófica, sin embargo, **no se identifica un vínculo mecanístico plausible**. Esta enfermedad es una infección cutánea tardía por *Borrelia*, y la tetracaína no tiene actividad antimicrobiana relevante. El puntaje elevado (0.9993) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Por ello, la predicción debe considerarse exploratoria y de baja credibilidad clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para acrodermatitis crónica atrófica.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para acrodermatitis crónica atrófica.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 80830 | Tetracaína Lainco 7,5 mg/g gel | Gel | No disponible |
| 15371 | Anestesia Tópica B. Braun 10 mg/ml solución | Solución cutánea | No disponible |
| 14534 | Lubristesic 7,5 mg/g pomada | Pomada | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): epilepsia, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, enfermedad cardíaca y cardiovascular, paro cardíaco súbito, trastornos de la conducción cardíaca, insuficiencia respiratoria, miastenia gravis y enfermedades de la unión neuromuscular, deficiencia de butirilcolinesterasa, hipertiroidismo (enfermedad de Graves, tirotoxicosis) y enfermedades oculares inflamatorias o infecciosas (uveítis, enfermedades del iris y del cuerpo ciliar, conjuntivitis).
- **Interacciones farmacológicas**: se identificaron 32 interacciones en total; las principales son:
  - **Mayores**: ácido nitroso y bupivacaína liposomal.
  - **Moderadas**: sulfasalazina, sulfametoxazol, otros anestésicos locales (lidocaína, benzocaína, cocaína, cincocaína, proparacaína, oxibuprocaína) y benzodiazepinas (alprazolam, clordiazepóxido, clobazam, clonazepam, ácido clorazépico, diazepam, estazolam).
  - **Menores**: hialuronidasa.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura, y no existe un mecanismo plausible: la tetracaína carece de actividad antimicrobiana frente a *Borrelia*. No se recomienda avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción.
- Evidencia preclínica o clínica que justifique un efecto sobre la acrodermatitis crónica atrófica.
- Evaluar la compatibilidad de vías de administración (pendiente).

**Nota sobre otras predicciones:** entre las demás indicaciones predichas, ninguna justifica avanzar. Los datos para acné queloide (L4) se refieren a analgesia durante procedimientos con láser, no al tratamiento de la enfermedad. La literatura sobre síndrome de cauda equina describe a la tetracaína como **causa** de neurotoxicidad, por lo que esa predicción refleja un efecto adverso y no un uso terapéutico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

