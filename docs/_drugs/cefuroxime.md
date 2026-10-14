---
layout: default
title: Cefuroxime
parent: Solo predicción del modelo (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Cefuroxime
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

# Cefuroxima: De Infecciones Bacterianas (p. ej., Otitis Media Infecciosa) a Hiperamilasemia

## Resumen en Una Frase

Cefuroxima es una cefalosporina de segunda generación, utilizada originalmente para tratar infecciones bacterianas como la otitis media infecciosa, la neumonía bacteriana, la meningitis bacteriana, la gonorrea y la enfermedad de Lyme.
El modelo TxGNN predice que podría ser efectiva para **hiperamilasemia**, pero no hay **ningún ensayo clínico** ni **ninguna publicación** que respalde esta dirección. La predicción se basa únicamente en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones bacterianas (otitis media infecciosa, neumonía bacteriana, meningitis bacteriana, gonorrea, enfermedad de Lyme, entre otras; según el grafo de conocimiento, ya que los textos de indicación de las autorizaciones españolas no constan en los datos) |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, cefuroxima es un antibiótico betalactámico (cefalosporina de segunda generación) que inhibe la síntesis de la pared celular bacteriana. Su eficacia en infecciones bacterianas respiratorias, otológicas, urinarias y del sistema nervioso central está bien establecida.

**En este caso no se identifica un vínculo mecanístico plausible.** La hiperamilasemia es un hallazgo bioquímico (elevación de amilasa sérica) y no una infección. Cefuroxima no tiene ningún efecto conocido sobre la amilasa sérica. El puntaje alto de TxGNN (99.76%) refleja una asociación derivada de la estructura del grafo de conocimiento, no una base farmacológica ni clínica.

Por lo tanto, esta predicción debe considerarse una señal computacional sin respaldo biológico verificable.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Cefuroxima cuenta con 20 autorizaciones vigentes, todas de medicamentos con un solo principio activo, y ninguna cancelada. Se muestran las 5 primeras:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 80366 | Cefuroxima Tecnigen 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 80318 | Cefuroxima Aurovitas 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 62909 | Cefuroxima Normon 250 mg polvo y disolvente para solución inyectable EFG | Polvo y disolvente para solución inyectable |
| 89750 | Cefuroxima Aristo 250 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 64949 | Cefuroxima Sala 1.500 mg polvo para solución inyectable y para perfusión EFG | Polvo para solución inyectable y para perfusión |

---

## Consideraciones de Seguridad

- **Contraindicaciones / enfermedades de precaución** (según el grafo de conocimiento, no del texto del prospecto): enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, trastornos de la coagulación sanguínea, colitis por *Clostridium difficile*, enterocolitis necrotizante perinatal y deficiencia congénita de protrombina.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Las 20 principales son todas de nivel moderado:
  - Antiácidos y sales de aluminio, calcio y magnesio (hidróxido de aluminio, carbonato de calcio, magaldrato, carbonato, hidróxido y óxido de magnesio).
  - Antagonistas H2 (famotidina, ranitidina, cimetidina, nizatidina, ranitidina con citrato de bismuto).
  - Inhibidores de la bomba de protones (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol).
  - Aminoglucósidos (kanamicina, neomicina) y balsalazida.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hiperamilasemia tiene nivel de evidencia L5: no hay ensayos ni literatura, y no existe un vínculo mecanístico plausible entre un antibiótico betalactámico y la elevación de amilasa sérica. No se recomienda avanzar con esta indicación.

**Para avanzar se necesita:**
- Una hipótesis mecanística y fisiopatológica que justifique el uso de un antibiótico en hiperamilasemia, que hoy no existe.
- Datos de mecanismo de acción y de advertencias del prospecto de las autorizaciones españolas.
- Priorizar otras indicaciones predichas con mejor respaldo:
  - **Infección del tracto urinario** (L3, Proceed with Guardrails): un ensayo observacional completado en pielonefritis (NCT04616352, n=973) y revisiones sistemáticas. Requiere considerar patrones locales de resistencia y prevalencia de BLEE.
  - **Otitis media supurativa** (L3, Proceed with Guardrails): cercana a una indicación ya autorizada, por lo que podría ser en gran parte un reetiquetado. Requiere considerar la resistencia del neumococo y los biofilms en la forma crónica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

