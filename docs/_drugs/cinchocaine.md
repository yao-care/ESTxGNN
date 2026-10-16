---
layout: default
title: Cinchocaine
parent: Solo predicción del modelo (L5)
nav_order: 182
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Cinchocaine: nueva indicación predicha, Bronquitis (nivel de evidencia L5). Indicación original: Dermatitis (según el grafo de conocimiento"
---

# Cinchocaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Cinchocaína: De Dermatitis a Bronquitis

## Resumen en Una Frase

La cinchocaína (dibucaína) es un anestésico local de tipo amida, utilizado originalmente en pomada rectal para el tratamiento de la dermatitis y sus síntomas locales.
El modelo TxGNN predice que podría ser efectiva para **bronquitis**, aunque actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dermatitis (según el grafo de conocimiento; el texto de indicación autorizado no figura en los datos compilados) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, la cinchocaína es un anestésico local de tipo amida que bloquea los canales de sodio dependientes de voltaje, lo que reduce la transmisión de señales nerviosas de dolor y picor. En la pomada rectal comercializada se asocia a un uso sintomático (alivio local de dolor, picor e irritación).

Desde el punto de vista teórico, un efecto anestésico tópico o inhalado podría suprimir el reflejo de la tos o la actividad sensorial de las vías respiratorias, lo que explicaría una cierta cercanía con la bronquitis. Sin embargo, esta relación es especulativa: no existen estudios clínicos ni literatura que respalden el uso en bronquitis, y el vínculo descansa exclusivamente en la puntuación del modelo (0.998).

Además, la exposición sistémica o en vías respiratorias a la cinchocaína plantea preocupaciones de toxicidad (por ejemplo, cardiotoxicidad y efectos sobre el sistema nervioso central), por lo que el balance beneficio-riesgo no está establecido.

### Otras indicaciones predichas (para contexto)

Los datos compilados incluyen otras seis predicciones, todas con nivel de evidencia L5, sin ensayos ni literatura, y con recomendación Hold:

| Indicación Predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Acrodermatitis crónica atrófica | 99.76% | Manifestación cutánea tardía de la infección por *Borrelia*; la cinchocaína, como mucho, aliviaría síntomas, sin acción antimicrobiana |
| Dermatomiositis neonatal | 99.72% | Enfermedad inflamatoria inmunomediada; sin mecanismo inmunomodulador conocido y con riesgos de absorción sistémica en neonatos |
| Enfermedad pulmonar intersticial infantil secundaria a enfermedad del tejido conectivo | 99.72% | Sin mecanismo plausible; población pediátrica que exige especial cautela |
| Acné queloideo | 99.67% | La más próxima biológicamente (tópica y dermatológica); podría aliviar dolor o picor local, sin evidencia sobre inflamación o fibrosis |
| Hidroa vacciniforme familiar | 99.66% | Fotosensibilidad rara; posible analgesia sintomática, sin acción sobre la patología de fondo |
| Dermatomiositis amiopática | 99.65% | Enfermedad autoinmune de predominio cutáneo; posible alivio del picor, sin efecto sobre la patología inmune |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 86172 | COHORTAN 5 MG/G + 5 MG/G POMADA RECTAL (Laboratorio Reig Jofre, S.A.) | Pomada rectal | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (no proceden del texto del prospecto, por lo que deben confirmarse): epilepsia, enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, parada cardíaca súbita, enfermedad del sistema de conducción cardíaco, insuficiencia respiratoria, miastenia gravis (incluida la de inicio en adultos), enfermedad de la unión neuromuscular, deficiencia de butirilcolinesterasa, enfermedad cardiovascular y cardiopatía.
- **Consideraciones adicionales del análisis de la predicción:** el uso en vías respiratorias o en neonatos y niños plantea riesgos de absorción sistémica, cardiotoxicidad, efectos sobre el sistema nervioso central y riesgos tipo metahemoglobinemia propios de los anestésicos locales.
- **Interacciones farmacológicas:** no se encontraron interacciones registradas en la consulta realizada.

Para información completa de advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para bronquitis (y para el resto de indicaciones predichas) se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, con un mecanismo especulativo y un perfil de seguridad no establecido para uso respiratorio.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación autorizada), un paso bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank para analizar el vínculo mecanístico.
- Realizar una revisión sistemática de literatura y de registros de ensayos que busque evidencia preclínica o clínica en bronquitis.
- Evaluar la compatibilidad de vías de administración, ya que la formulación comercializada es rectal y no es adecuada para una indicación respiratoria.
- Si se desea explorar alguna alternativa, priorizar indicaciones dermatológicas tópicas (como el acné queloideo) con estudios preclínicos o piloto de alivio sintomático.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

