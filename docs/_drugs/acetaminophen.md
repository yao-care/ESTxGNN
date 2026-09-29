---
layout: default
title: Acetaminophen
parent: Evidencia moderada (L3-L4)
nav_order: 14
evidence_level: L4
indication_count: 1
---

# Acetaminophen
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Acetaminofeno (Paracetamol): De Analgésico y Antipirético a Migraña con Aura del Tronco Encefálico

## Resumen en Una Frase

El acetaminofeno (paracetamol) se usa desde hace décadas para aliviar el dolor y reducir la fiebre. El modelo TxGNN predice que podría ser efectivo para la **migraña con aura del tronco encefálico**, pero no hay **ningún ensayo clínico** registrado y las **20 publicaciones** halladas tratan de la migraña en general, no de este subtipo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Alivio del dolor y la fiebre (según la descripción farmacológica; los textos de indicación de las autorizaciones españolas vienen vacíos) |
| Nueva Indicación Predicha | Migraña con aura del tronco encefálico |
| Puntaje de Predicción TxGNN | 99.15% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el acetaminofeno es un analgésico y antipirético de uso muy extendido. Su acción es similar a la de los compuestos tipo aspirina, pero sin efecto antiinflamatorio ni antiagregante y sin irritar la mucosa gástrica. Las bases de farmacología lo asocian con los objetivos moleculares COX-1 (PTGS1), COX-2 (PTGS2) y TRPV4, aunque no aportan datos cuantitativos de actividad. Se cree que actúa como analgésico a nivel central, con un mecanismo no del todo caracterizado.

La migraña con aura del tronco encefálico es un subtipo de migraña, y el acetaminofeno es un tratamiento agudo establecido para la migraña en general. El puntaje alto de TxGNN (0.99) probablemente refleja la fuerte conexión del fármaco con la migraña como enfermedad madre en el grafo de conocimiento.

Ninguna de las evidencias aportadas aborda específicamente el subtipo con aura del tronco encefálico. Por ello, esta predicción se interpreta mejor como una extensión de un uso ya existente en migraña que como una señal de reposicionamiento novedosa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se encontraron 20 publicaciones, todas sobre migraña en general. La tabla lista las 10 más relevantes.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11112243](https://pubmed.ncbi.nlm.nih.gov/11112243/) | 2000 | ECA | Arch Intern Med | Eficacia y seguridad del acetaminofeno en migraña; estudio poblacional aleatorizado, doble ciego y controlado con placebo |
| [9482363](https://pubmed.ncbi.nlm.nih.gov/9482363/) | 1998 | ECA (3 ensayos) | Arch Neurol | Eficacia y seguridad de acetaminofeno + aspirina + cafeína para aliviar el dolor de migraña; tres ensayos doble ciego controlados con placebo |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | Análisis retrospectivo de 3 ECA | Clin Ther | La combinación acetaminofeno + aspirina + cafeína en migraña asociada a la menstruación, comparada con migraña no menstrual |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guía / evaluación de evidencia | Headache | Evaluación de la American Headache Society sobre las terapias farmacológicas para la migraña aguda en adultos |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Revisión | Neurol Clin | Cefalea en el embarazo y puerperio; el acetaminofeno es el tratamiento sintomático de primera línea |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Revisión | Handb Clin Neurol | Estado migrañoso como complicación de la migraña con o sin aura |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Revisión | Cureus | Terapias abortivas y profilácticas de la migraña en el embarazo |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Revisión | Cureus | Relación y abordaje terapéutico de la migraña en embarazo y lactancia |
| [16018227](https://pubmed.ncbi.nlm.nih.gov/16018227/) | 2005 | Revisión | Pediatr Ann | Tratamiento de la migraña pediátrica: terapia aguda y preventiva |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Revisión | Neurol Int | Ubrogepant en migraña aguda; menciona el acetaminofeno entre los tratamientos de migraña leve a moderada |

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones. Los textos de indicación aprobada vienen vacíos en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 81946 | DOLOSTOP 500 MG SOLUCION ORAL | Solución oral |
| 70349 | PARACETAMOL TEVA 1 g COMPRIMIDOS EFG | Comprimido |
| 81874 | PARACETAMOL VIR 1 g COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | Comprimido recubierto con película |
| 69955 | APIREDOL 100 mg/ml SOLUCION ORAL | Solución oral |
| 88032 | PARACETAMOL PENSA PHARMA 1G COMPRIMIDOS EFG | Comprimido |

También existen otras presentaciones: solución para perfusión, comprimido efervescente y polvo para solución oral en sobre.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos recibidos no incluyen interacciones fármaco-fármaco; las tres entradas de la consulta corresponden a dianas farmacológicas (TRPV4, COX-1, COX-2), no a medicamentos que interactúen.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe evidencia específica para la migraña con aura del tronco encefálico: no hay ensayos clínicos y la literatura trata la migraña en general. El acetaminofeno ya se usa en la migraña, así que la predicción aporta poco como reposicionamiento nuevo y se trata mejor como pregunta de investigación.

**Para avanzar se necesita:**
- Estudios o series de casos que evalúen el acetaminofeno específicamente en migraña con aura del tronco encefálico
- Datos del mecanismo de acción desde DrugBank para analizar el vínculo mecanístico
- Advertencias y contraindicaciones del prospecto de la AEMPS, necesarias para la evaluación de seguridad
- Revisión manual de la relevancia de las publicaciones, que aún figura como pendiente

*Los resultados son solo de referencia para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

