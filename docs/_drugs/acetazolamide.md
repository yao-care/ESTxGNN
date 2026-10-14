---
layout: default
title: Acetazolamide
parent: Solo predicción del modelo (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
---

# Acetazolamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Acetazolamida: De Epilepsia de Ausencia a Hipertermia Maligna Inducida por el Ejercicio

## Resumen en Una Frase

Acetazolamida es un inhibidor de la anhidrasa carbónica, utilizado originalmente en epilepsia de ausencia, insuficiencia cardíaca congestiva, glaucoma y mal de altura.
El modelo TxGNN predice que podría ser efectivo para **hipertermia maligna inducida por el ejercicio**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia de ausencia (el texto de indicación de la autorización española está vacío; se toma la primera indicación original del grafo de conocimiento) |
| Nueva Indicación Predicha | Hipertermia maligna inducida por el ejercicio |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la acetazolamida inhibe la anhidrasa carbónica (los datos farmacológicos muestran afinidad por las isoformas CA1, CA4, CA7, CA12, CA13 y CA14). Esto reduce la formación de líquido intraocular, ejerce un efecto diurético renal y, en el cerebro, contribuye a su efecto antiepiléptico.

El vínculo con la nueva indicación es plausible pero no verificado: la inhibición de la anhidrasa carbónica modifica el equilibrio ácido-base y podría influir en el manejo de iones en el músculo. No existe ninguna evidencia clínica que lo respalde, y la similitud con las indicaciones originales no ha sido evaluada.

Debe interpretarse con cautela: la puntuación alta de TxGNN es una predicción basada en el grafo y no equivale a evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 24408 | EDEMOX 250 mg COMPRIMIDOS (Chiesi España S.A.U.) | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto)**: insuficiencia hepática y enfermedad hepática, enfermedad renal, acidosis tubular renal, enfermedad hematológica, enfermedad de la vesícula biliar, gota, diabetes mellitus tipo 1 y tipo 2, cetoacidosis diabética, insuficiencia respiratoria, y enfermedad de Addison e insuficiencia suprarrenal (incluidas formas congénitas y familiares).
- **Interacciones farmacológicas**: la consulta se completó y devolvió 6 resultados, todos ellos de tipo farmacológico (dianas de unión) y no interacciones con otros fármacos: anhidrasas carbónicas 1, 4, 7, 12, 13 y 14.
- **Señales de seguridad en la literatura recuperada para otras indicaciones predichas**: un caso de edema pulmonar no cardiogénico tras acetazolamida intravenosa y casos de íleo adinámico inducido por acetazolamida. En cirrosis, el fármaco puede precipitar encefalopatía hepática al aumentar el amoníaco.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertermia maligna inducida por el ejercicio tiene una puntuación alta en TxGNN, pero carece por completo de ensayos clínicos y literatura (nivel L5). Además, no se ha podido completar el cribado de seguridad por falta de los datos del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción.
- Realizar una revisión sistemática de la literatura sobre anhidrasa carbónica y trastornos de hipertermia o canalopatías musculares.
- Evaluar estudios preclínicos que respalden un vínculo mecanístico.
- Valorar la relevancia de las contraindicaciones del grafo en la población diana.

---

### Nota sobre otras predicciones de la lista

Ninguna de las otras nueve indicaciones predichas tiene evidencia clínica sólida; todas reciben recomendación **Hold**:

| Indicación predicha | Evidencia | Observación |
|------|------|------|
| Miocardiopatía hipertrófica | L4 | Solo literatura sobre diuresis en insuficiencia cardíaca; la depleción de volumen podría empeorar la obstrucción del flujo |
| Cardiomiopatía | L4 | Evidencia indirecta; incluye una señal de seguridad (edema pulmonar no cardiogénico) |
| Obstrucción intestinal | L4 | La literatura describe íleo adinámico inducido por acetazolamida, lo que contradice la predicción |
| Cardiomiopatía cirrótica | L5 | Riesgo de encefalopatía hepática en cirrosis |
| Pseudoobstrucción intestinal no clasificada | L5 | Posible contraindicación por riesgo de dismotilidad |
| Miopatía congénita con exceso de filamentos finos, miopatía distal tipo Tateyama, glucogenosis por deficiencia de maltasa ácida tardía, miocardiopatía hipertrófica por entrenamiento intensivo | L5 | Sin evidencia ni mecanismo definido |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

