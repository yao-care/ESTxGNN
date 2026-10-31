---
layout: default
title: Tadalafil
parent: Solo predicción del modelo (L5)
nav_order: 759
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-31
monitor_inn: "tadalafil"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
description: "Tadalafil: nueva indicación predicha, Ambras type hypertrichosis universalis congenita (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Tadalafil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Tadalafil: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## Resumen en Una Frase

Tadalafilo es un inhibidor de la fosfodiesterasa 5 (PDE5), utilizado originalmente para la hiperplasia prostática benigna, la hipertensión pulmonar y la disfunción eréctil.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita de tipo Ambras**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Ambras type hypertrichosis universalis congenita |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 11) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, tadalafilo es un inhibidor de PDE5 que aumenta el GMP cíclico (cGMP) y produce vasodilatación. Su eficacia en disfunción eréctil, hiperplasia prostática benigna e hipertensión arterial pulmonar está establecida.

Sin embargo, la razonabilidad mecanística de esta predicción es **débil**. El síndrome de Ambras es un trastorno genético raro (reordenamientos cromosómicos que afectan a la regulación de TRPS1), y no existe un mecanismo plausible basado en PDE5 que pueda corregirlo. Una conexión especulativa con la biología del folículo piloso mediante vasodilatación no puede descartarse, pero carece de respaldo.

Además, la hipertricosis es un efecto adverso conocido de algunos vasodilatadores (por ejemplo, minoxidilo). Es probable que el puntaje alto refleje la cercanía en la red con estos fármacos, es decir, una asociación con hipertricosis inducida por fármacos y no un efecto terapéutico. La **dirección del efecto es incierta** y podría ser la opuesta a un beneficio.

Otras predicciones del modelo (hipertricosis, anomalías del tallo piloso, tricomegalia familiar, síndromes malformativos) siguen el mismo patrón: todas son de nivel L5 y sin evidencia clínica. La excepción es la cardiopatía cifoescoliótica, con una justificación indirecta plausible (hipertensión pulmonar), aunque solo hipotética.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal.

Como dato de contexto, para otra predicción (migraña con aura del tronco encefálico) existe un único caso clínico:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) | 2006 | Reporte de caso | Cephalalgia | Tadalafilo asociado con aura migrañosa típica sin cefalea; sugiere un posible desencadenante, no un beneficio terapéutico |

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único). El texto de indicación aprobada no está disponible en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 89934 | Tadalafilo Farmalter 20 mg comprimidos bucodispersables EFG | Comprimido bucodispersable | No disponible |
| 02237003IP3 | Cialis 20 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 82192 | Virvirilo 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 85659 | Tadalafilo Normogen 20 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 80040 | Tadalafilo Teva 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proviene del texto del prospecto): insuficiencia hepática, epilepsia, estenosis aórtica y enfermedad de la válvula aórtica, trastornos hipotensivos, trastornos de la coagulación, síndrome coronario agudo, anemia falciforme y hemoglobinopatías, ictus y trastornos cerebrovasculares, infarto de miocardio, mieloma de células plasmáticas, leucemia, priapismo, enfermedad de Peyronie y otras alteraciones del pene, pérdida auditiva, y miocardiopatía hipertrófica (incluida la familiar).
- **Interacciones farmacológicas**: se identificaron 132 interacciones. Entre las de nivel moderado figuran aprepitant, dexametasona, lorcaserina, cimetidina, claritromicina, miconazol, clotrimazol y los inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina), además de sapropterina y troglitazona. Papaverina es de nivel leve; pantoprazol, glimepirida, doxiciclina, morfina, metformina y omeprazol tienen nivel desconocido.
- **Señal de seguridad adicional**: el único reporte de literatura vincula tadalafilo con aura migrañosa, lo que apunta a un posible riesgo y no a una oportunidad terapéutica.

Para las advertencias del prospecto, consultar el prospecto oficial de la AEMPS.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es únicamente computacional (L5), sin ensayos ni publicaciones, con un mecanismo no plausible para un trastorno genético estructural y con indicios de que el modelo captura hipertricosis como efecto adverso de vasodilatadores. No hay base para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank) y análisis del vínculo mecanístico con la biología del folículo piloso
- Descarga y análisis del prospecto de la AEMPS (advertencias y contraindicaciones), que es un requisito bloqueante para el cribado de seguridad
- Estudios preclínicos que justifiquen la dirección del efecto (tratamiento frente a inducción de hipertricosis)
- Evaluar si alguna de las otras predicciones (p. ej., cardiopatía cifoescoliótica por su vínculo con la hipertensión pulmonar) merece priorizarse
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

