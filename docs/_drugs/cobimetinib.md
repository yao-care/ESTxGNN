---
layout: default
title: Cobimetinib
parent: Solo predicción del modelo (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
---

# Cobimetinib
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

# Cobimetinib: De Melanoma Metastásico a Esclerosis Lateral Amiotrófica

## Resumen en Una Frase

Cobimetinib es un inhibidor de MEK1/2, originalmente utilizado para el tratamiento del melanoma metastásico.
El modelo TxGNN predice que podría ser efectivo para **esclerosis lateral amiotrófica (ELA)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Melanoma metastásico |
| Nueva Indicación Predicha | Esclerosis lateral amiotrófica |
| Puntaje de Predicción TxGNN | 99,73% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Cobimetinib inhibe MEK1/2, componentes de la vía RAS-RAF-MEK-ERK. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción original, pero esta vía es conocida por su papel en la proliferación celular, y su bloqueo es la base de su uso en melanoma.

La relación con la ELA es indirecta. La señalización ERK/MAPK se ha implicado en la neuroinflamación y en las respuestas de estrés de las motoneuronas en modelos de ELA, por lo que existe un vínculo plausible pero no validado. Además, la penetración de cobimetinib en el sistema nervioso central es limitada (es sustrato de la glicoproteína P), lo que debilita el fundamento para una enfermedad neurológica.

Las demás predicciones de mayor puntaje (todas con puntajes entre 99,5% y 99,7%) son en su mayoría trastornos de la motoneurona del espectro de la ELA (síndrome de Mills, ELA tipo 22, susceptibilidad a ELA, síndrome de motoneurona inferior de inicio tardío, amiotrofia monomélica, entre otros) o enfermedades del desarrollo y esqueléticas sin vínculo mecanístico claro (polimicrogiria parieto-occipital parasagital bilateral, displasia espondilometafisaria axial, síndrome de tricomegalia-degeneración pigmentaria de la retina-enanismo). Ninguna cuenta con ensayos ni literatura. Cabe destacar que la toxicidad retiniana (retinopatía serosa) de cobimetinib supone una preocupación de seguridad específica para fenotipos de degeneración retiniana.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1151048001 | COTELLIC 20 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de MEK) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto; en general, hemograma, función hepática y renal, y control oftalmológico por el riesgo conocido de retinopatía serosa |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en la consulta (fuente: DDInter). Entre las de nivel **Mayor** figuran:
  - Aprepitant
  - Dexametasona
  - Claritromicina
  - Cobicistat
  - Samario (153Sm) lexidronam

  Entre las de nivel **Moderado** se incluyen cimetidina, clotrimazol, eliglustat, metreleptina, miconazol, naltrexona, rolapitant, troglitazona, deferasirox, palifermina, cloruro de estroncio Sr-89, fostamatinib, ticagrelor, quinina e ivacaftor. Muchas de ellas afectan probablemente al metabolismo mediado por CYP3A, por lo que requieren revisión farmacológica antes de cualquier uso.
- **Toxicidad ocular**: la retinopatía serosa es un efecto adverso conocido de cobimetinib, relevante para cualquier fenotipo con afectación retiniana.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, con un vínculo mecanístico especulativo y penetración limitada en el sistema nervioso central. Además, el perfil de toxicidad de cobimetinib y las numerosas interacciones farmacológicas hacen desfavorable la relación riesgo-beneficio sin evidencia adicional.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (consulta a la API de DrugBank)
- Advertencias y contraindicaciones del prospecto de AEMPS (descarga y análisis del PDF), necesarias para el cribado de seguridad
- Estudios preclínicos en modelos de ELA que demuestren eficacia y exposición suficiente en el sistema nervioso central
- Revisión sistemática de la literatura sobre inhibición de MEK/ERK en enfermedades de la motoneurona
- Evaluación de la compatibilidad de vías de administración y de la similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

