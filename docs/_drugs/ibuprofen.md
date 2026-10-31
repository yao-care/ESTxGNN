---
layout: default
title: Ibuprofen
parent: Solo predicción del modelo (L5)
nav_order: 400
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-31
monitor_inn: "Ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Ibuprofen: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) (nivel de evidencia L5). Indicación original: No consta en los dat…"
---

# Ibuprofen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Ibuprofen: Displasia acromesomélica, tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## Resumen en Una Frase

Ibuprofeno es un antiinflamatorio no esteroideo (AINE) utilizado ampliamente por su acción analgésica y antipirética, con indicaciones originales como artritis reumatoide, artrosis, cefalea y artropatías.
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Puntaje de Predicción TxGNN | 0.9974 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 16) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, ibuprofeno es un inhibidor no selectivo de la ciclooxigenasa (COX-1 y COX-2), y su eficacia en artritis reumatoide, artrosis y otras artropatías está bien establecida.

La displasia acromesomélica tipo Hunter-Thompson es una displasia esquelética rara causada por variantes de pérdida de función en CDMP1/GDF5 (vía de señalización BMP). No se aprecia un vínculo mecanístico plausible entre la inhibición de COX y la señalización de GDF5, ni una forma de corregir la displasia esquelética con ibuprofeno.

El puntaje alto del modelo (0.9974) probablemente es un artefacto del modelo TxGNN (aprendizaje profundo), derivado de anotaciones fenotípicas musculoesqueléticas compartidas con las indicaciones originales (artritis y artropatía). En el mejor de los casos, ibuprofeno podría ofrecer analgesia sintomática para el dolor articular, lo cual no constituye modificación de la enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de monofármaco; ninguna cancelada). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 90114 | Ibuprofeno Combix 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 68200 | Ibufarmalid 400 mg suspensión oral | Suspensión oral |
| 80719 | Espidifen 600 mg granulado para solución oral sabor cola-limón | Granulado para solución oral |
| 64030 | Ibuprofeno Mabo 50 mg/g gel | Gel |
| 85161 | Ibuprofeno B. Braun Pediátrico 200 mg solución para perfusión | Solución para perfusión |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, insuficiencia hepática, hepatopatía, enfermedad renal, úlcera péptica, enfermedad inflamatoria intestinal, trombocitopenia, trastornos de la coagulación, ictus y trastornos cerebrovasculares, infarto de miocardio, epilepsia, EPOC, diabetes mellitus y cetoacidosis diabética, lupus eritematoso sistémico, hipotiroidismo, enfermedad de la vesícula biliar, hipertrofia prostática benigna, hipotensión, déficit de potasio y abuso/dependencia de sustancias.
- **Interacciones y dianas farmacológicas**: los datos compilados describen dianas farmacológicas (COX-1, COX-2, PPAR-γ, ASIC1, SMCT1 y el transportador de aminoácidos acoplado a protones 1), no interacciones con otros medicamentos con nivel de gravedad definido.
- **Exposición prenatal**: para síndromes malformativos congénitos como el síndrome braquidactilia-sindactilia, la exposición prenatal a AINE es en sí misma una preocupación de seguridad.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de COX y la señalización GDF5/BMP. Lo más probable es que el puntaje elevado sea un artefacto del modelo TxGNN (aprendizaje profundo).

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados desde DrugBank
- Advertencias y contraindicaciones oficiales de los prospectos de la AEMPS
- Estudios preclínicos o de mecanismo que sustenten un efecto sobre la señalización GDF5/BMP
- Si se considera, evaluar el uso solo como analgesia sintomática (cuidado de soporte), no como reposicionamiento modificador de la enfermedad

**Otras predicciones del modelo (todas L5, Hold):** síndrome de braquiolmia-amelogénesis imperfecta, miosclerosis, braquiolmia, síndrome de braquidactilia-sindactilia, pseudoacondroplasia y síndrome de microftalmia colobomatosa-displasia rizomélica. Ninguna cuenta con ensayos ni literatura, y en todas el vínculo mecanístico es indirecto o inexistente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

