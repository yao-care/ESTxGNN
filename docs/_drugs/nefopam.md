---
layout: default
title: Nefopam
parent: Solo predicción del modelo (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
---

# Nefopam
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

# Nefopam: De Analgésico No Opioide a Craneoestenosis con Catarata

## Resumen en Una Frase

Nefopam es un analgésico de acción central, no opioide, comercializado en España como solución inyectable.
El modelo TxGNN predice que podría ser efectivo para **craneoestenosis con catarata**, pero sin **ningún ensayo clínico ni publicación** que respalde esta predicción.
Esa predicción, y las otras ocho de catarata, no tienen un vínculo mecanístico plausible.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Craneoestenosis con catarata (craniostenosis cataract) |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, nefopam inhibe la recaptación de monoaminas (serotonina, noradrenalina y dopamina) y modula canales de sodio y calcio dependientes de voltaje.

**Esta predicción no resulta plausible.** Nada de lo anterior conecta el fármaco con la opacidad del cristalino ni con la craneosinostosis. Los mismos hallazgos aplican a las otras ocho predicciones de catarata (inmadura, madura, diabética, senil, nuclear, cortical, asociada a diabetes tipo 2 y tetánica):

- Todas comparten un puntaje casi idéntico (entre 99.97% y 99.98%). Esto apunta a un artefacto de la vecindad en el grafo de conocimiento, no a una señal específica del fármaco.
- La catarata madura se trata habitualmente con cirugía, por lo que un analgésico sistémico no tiene una lógica terapéutica clara.
- Las vías relevantes en la catarata diabética (vía de los polioles, estrés oxidativo) no son dianas conocidas de nefopam.
- En la catarata tetánica, la modulación de canales de calcio no corrige el déficit de calcio subyacente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

---

## Otra Indicación Predicha con Evidencia: Estenosis Espinal Lumbar

De las diez indicaciones predichas, solo **estenosis espinal lumbar** (puntaje TxGNN 99.97%, rango 10) tiene literatura. Su nivel es **L3** y la etiqueta es "pregunta de investigación". No hay ensayos clínicos registrados.

El vínculo es indirecto y orientado a síntomas. La acción analgésica central de nefopam podría aliviar la disestesia de tipo neuropático y el dolor postoperatorio. La literatura trata la analgesia perioperatoria y el ahorro de opioides, no la modificación de la enfermedad. Es una extensión del uso analgésico existente, no un mecanismo nuevo.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38068520](https://pubmed.ncbi.nlm.nih.gov/38068520/) | 2023 | ECA doble ciego | J Clin Med | 73 pacientes con estenosis lumbar operados; nefopam 20 mg frente a suero salino sobre disestesia, dolor postoperatorio y satisfacción |
| [41937571](https://pubmed.ncbi.nlm.nih.gov/41937571/) | 2026 | ECA doble ciego, controlado con placebo | Asian Spine J | Efecto ahorrador de opioides de nefopam intravenoso continuo tras fusión lumbar multinivel |
| [31166320](https://pubmed.ncbi.nlm.nih.gov/31166320/) | 2019 | Comparación de regímenes | Zh Vopr Neirokhir Im N N Burdenko | Efecto de distintos regímenes de analgesia multimodal sobre la tasa de síndrome de cirugía fallida de espalda |
| [25535527](https://pubmed.ncbi.nlm.nih.gov/25535527/) | 2014 | Reporte de caso | J Korean Neurosurg Soc | Estado epiléptico atribuido a nefopam en un varón de 71 años operado de estenosis lumbar |

Los diseños se confirmaron solo a partir de títulos y resúmenes truncados, por lo que el nivel se fijó de forma conservadora.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 90988 | NEPHODOL 20 MG/2 ML SOLUCIÓN INYECTABLE EFG | Solución inyectable | Altan Pharmaceuticals S.A. |

---

## Consideraciones de Seguridad

- **Riesgo de convulsiones**: un reporte de caso (PMID 25535527) describe estado epiléptico causado por nefopam. Cualquier protocolo debería considerar este riesgo. Los efectos neurológicos adversos descritos para el fármaco incluyen confusión, alucinaciones, delirio y convulsiones.

No se dispone de datos de advertencias, contraindicaciones ni interacciones del prospecto de la AEMPS. Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (craneoestenosis con catarata) es solo una salida del modelo (L5), sin ensayos ni literatura y sin vínculo mecanístico plausible. Las demás predicciones de catarata comparten esa debilidad. La estenosis espinal lumbar es la única con apoyo publicado, pero se limita al control del dolor perioperatorio.

**Para avanzar se necesita:**
- Descartar las predicciones de catarata como artefactos del grafo, salvo que aparezca evidencia mecanística o clínica independiente.
- Si se quiere explorar estenosis espinal lumbar, revisar los textos completos de los ECA para confirmar diseños y resultados, y valorar el riesgo de convulsiones.
- Obtener del prospecto de la AEMPS las advertencias, contraindicaciones e indicación aprobada.
- Completar los datos de mecanismo de acción desde DrugBank.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

