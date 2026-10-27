---
layout: default
title: Ephedrine
parent: Evidencia moderada (L3-L4)
nav_order: 294
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Ephedrine: nueva indicación predicha, Enfermedad de la cavidad nasal (nivel de evidencia L4). Indicación original: Rinitis alérgica (según las indicaciones del grafo de conocimiento"
monitor_inn: "ephedrine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia"]
---

# Ephedrine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

## Efedrina: De Rinitis Alérgica a Enfermedad de la Cavidad Nasal
{: .text-alpha }

## Resumen en Una Frase

La efedrina es un simpaticomimético utilizado originalmente para cuadros de las vías respiratorias superiores, como la rinitis alérgica, la rinitis vasomotora, la bronquitis y el resfriado común.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal**,
con **0 ensayos clínicos** y **2 publicaciones** de baja calidad (de 1964 y 2000) que respaldan actualmente esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica (según las indicaciones del grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro del fármaco. Según la información conocida, la efedrina es un simpaticomimético con acción indirecta (liberación de noradrenalina) y acción directa como agonista adrenérgico alfa y beta. La vasoconstricción mediada por receptores alfa-1 en los vasos de la mucosa nasal reduce la congestión y la inflamación, lo que es biológicamente plausible en enfermedades de la cavidad nasal.

La enfermedad de la cavidad nasal es una categoría amplia que incluye cuadros ya asociados a la efedrina en los datos compilados (rinitis alérgica, rinitis vasomotora, rinitis, nasofaringitis). Por ello, esta predicción se parece más a una ampliación de un uso existente que a un reposicionamiento genuino. El puntaje TxGNN muy alto (0,999) es coherente con ese solapamiento.

Conviene precisar que este razonamiento se apoya en farmacología general y no en el mecanismo de acción registrado. Además, las formulaciones comercializadas en España son sobre todo inyectables (usadas en otros contextos), por lo que la compatibilidad de vía de administración con un uso nasal queda sin verificar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14211229](https://pubmed.ncbi.nlm.nih.gov/14211229/) | 1964 | Informe de prueba clínica | Svenska lakartidningen | Prueba clínica de una combinación de un antihistamínico fenotiazínico (clorhidrato de N-hidroxietilprometazina) con clorhidrato de efedrina en la cavidad nasal. No hay resumen disponible; los detalles no están verificados. |
| [11789239](https://pubmed.ncbi.nlm.nih.gov/11789239/) | 2000 | Observación clínica preliminar | Zhongguo Zhong xi yi jie he za zhi | Observación preliminar de un espray para rinitis en rinitis crónica. La composición de la formulación no está confirmada y probablemente no fue un estudio controlado. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 90455 | Efedrina Aguettant 3 mg/ml solución inyectable | Solución inyectable | Sin texto de indicación disponible |
| 79516 | Efedrina Aguettant 3 mg/ml solución inyectable en jeringas precargadas | Solución inyectable en jeringa precargada | Sin texto de indicación disponible |
| 90454 | Efedrina Aguettant 30 mg/ml solución inyectable | Solución inyectable | Sin texto de indicación disponible |
| 70338 | Hidrocloruro de Efedrina Altan 10 mg/ml solución inyectable | Solución inyectable | Sin texto de indicación disponible |
| 73280 | Hidrocloruro de Efedrina Kabi 30 mg/ml solución inyectable | Solución inyectable | Sin texto de indicación disponible |

Hay 13 autorizaciones vigentes en total, todas de composición simple. Incluyen también comprimidos (Efedrina Level 50 mg), pomadas rectales (Hemoal, Hemoal Forte) y un jarabe (Codinex).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, insuficiencia cardíaca congestiva, epilepsia, EPOC, trastornos de ansiedad, trastornos psicóticos y esquizoafectivos, hipotiroidismo, glaucoma de ángulo abierto, úlcera gástrica y péptica, enfermedad inflamatoria intestinal, porfiria, enfermedad hepática y renal, pancreatitis, enfermedad de la vesícula biliar y trombocitopenia, entre otras.
- **Interacciones farmacológicas**: se registran 196 interacciones. Entre las de nivel **mayor** figuran tramadol, amitriptilina, bupropión y azul de metileno. Entre las de nivel moderado figuran formoterol, salbutamol, metilfenidato, anfetamina, atenolol, acebutolol, atomoxetina y metformina.

Consultar el prospecto para el resto de la información de seguridad: las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a la predicción del modelo y a dos publicaciones antiguas y de baja calidad, sin ensayos clínicos. Además, la predicción se solapa con indicaciones ya existentes y el perfil de seguridad sistémico es exigente (muchas contraindicaciones y 196 interacciones). Las otras dos predicciones (laringofaringitis aguda y cefalea autonómica trigeminal) tienen nivel L5 y también quedan en Hold.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de la AEMPS, un dato bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar la compatibilidad de vía y formulación (intranasal frente a las presentaciones inyectables y orales disponibles).
- Aclarar si se trata de reposicionamiento real o de una categoría más amplia de un uso ya establecido.
- Recuperar el texto completo de las dos publicaciones y buscar estudios controlados en rinitis o patología nasal.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

