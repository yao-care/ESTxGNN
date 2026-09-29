---
layout: default
title: Cefuroxime
parent: Solo predicción del modelo (L5)
nav_order: 112
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

# Cefuroxima: De Antibiótico Cefalosporínico a Hiperamilasemia

## Resumen en Una Frase

Cefuroxima es una cefalosporina de segunda generación, utilizada como antibiótico antibacteriano (los datos recibidos no detallan la indicación original registrada).
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.
La predicción es solo una señal del grafo del modelo y, por ahora, no tiene plausibilidad biológica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización (cefalosporina antibacteriana) |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99,76 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, cefuroxima es una cefalosporina de segunda generación que inhibe la síntesis de la pared celular bacteriana, y su eficacia se ha establecido en infecciones bacterianas.

La hiperamilasemia es un hallazgo de laboratorio (elevación de la amilasa en sangre), no una enfermedad infecciosa. No se identificó ningún vínculo mecanístico entre un antibiótico que actúa sobre la pared bacteriana y la reducción de la amilasa sérica.

El puntaje alto (99,76 %) refleja cercanía en el grafo de conocimiento, no evidencia clínica. Por eso esta predicción debe leerse como una hipótesis sin respaldo, probablemente un artefacto de la red.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 80366 | Cefuroxima Tecnigen 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 80318 | Cefuroxima Aurovitas 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 62909 | Cefuroxima Normon 250 mg polvo y disolvente para solución inyectable EFG | Polvo y disolvente para solución inyectable |
| 89750 | Cefuroxima Aristo 250 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 64949 | Cefuroxima Sala 1.500 mg polvo para solución inyectable y para perfusión EFG | Polvo para solución inyectable y para perfusión |

Se muestran 5 de las 20 autorizaciones. El texto de indicación aprobada no figura en los datos recibidos.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos, literatura ni mecanismo plausible que respalden el uso de cefuroxima en hiperamilasemia. El puntaje alto del modelo por sí solo no basta para avanzar.

**Nota sobre otras candidatas del mismo análisis:**
- **Infección del tracto urinario** (puesto 6, nivel L3, Proceed with Guardrails): cuenta con 17 ensayos y abundante literatura, entre ellos el estudio observacional NCT04616352 (n=973) sobre cefuroxima en pielonefritis. Probablemente sea un uso ya autorizado y no un reposicionamiento real, y la clasificación es provisional porque solo se revisaron 10 de los 17 ensayos.
- **Otitis media supurativa** (puesto 9, nivel L4, Research Question): tiene un vínculo antibacteriano plausible, pero la literatura es sobre todo microbiológica e indirecta.

**Para avanzar se necesita:**
- Completar la indicación original y el mecanismo de acción (MOA) desde DrugBank y los prospectos de la AEMPS
- Obtener advertencias y contraindicaciones del prospecto de la AEMPS para el cribado de seguridad
- Confirmar si las candidatas de infección urinaria y otitis corresponden a indicaciones ya autorizadas
- No invertir más esfuerzo en hiperamilasemia salvo que aparezca evidencia clínica nueva
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

