---
layout: default
title: Safinamide
parent: Solo predicción del modelo (L5)
nav_order: 481
evidence_level: L5
indication_count: 3
---

# Safinamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Safinamida: De Enfermedad de Parkinson a Encefalitis Subaguda de Rasmussen

## Resumen en Una Frase

Safinamida se utiliza como tratamiento adyuvante en la enfermedad de Parkinson con episodios "off". El modelo TxGNN predice que podría ser efectiva para la **encefalitis subaguda de Rasmussen**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (adyuvante a agonistas dopaminérgicos o levodopa en pacientes con episodios "off"). Los textos de indicación de las autorizaciones de AEMPS vienen vacíos; este dato procede de la base farmacológica consultada. |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos de DrugBank no incluyen una descripción detallada del mecanismo de acción. La base farmacológica sí indica que safinamida es un inhibidor de la monoamino oxidasa B (MAO-B), con una selectividad superior a 800 veces frente a MAO-A. Por farmacología general, no respaldada por los datos aportados, también se le atribuye bloqueo de canales de sodio dependientes de voltaje y reducción de la liberación de glutamato.

La encefalitis de Rasmussen es una encefalitis unilateral de origen inmunomediado, con convulsiones focales refractarias. La excitotoxicidad por glutamato se propone como uno de los factores contribuyentes. Por ello, un efecto de safinamida sobre las convulsiones o la excitotoxicidad es concebible desde el punto de vista teórico.

Aun así, ese beneficio probablemente se limitaría al control sintomático. No actuaría sobre la inflamación subyacente mediada por linfocitos T. No existe ningún estudio específico, y el puntaje de 0.996 es solo una predicción del modelo, sin corroboración clínica.

TxGNN también predijo otras dos indicaciones, ambas con nivel L5 y sin evidencia:
- **Mielitis** (99.46%): no hay una vinculación mecanística respaldada por los datos.
- **Neurodegeneración asociada a PLA2G6** (99.22%): el parkinsonismo y la distonía de estadios avanzados hacen plausible un apoyo sintomático dopaminérgico. No corregiría el defecto de fondo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 91074 | Safinamida Teva 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Teva Pharma S.L.U. |
| 114984008IP1 | Xadago 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | Zambon S.P.A. |
| 90309 | Safinamida Stada 50 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorio Stada S.L. |
| 114984003 | Xadago 50 mg comprimidos recubiertos con película | Comprimido recubierto con película | Zambon S.P.A. |
| 90156 | Safinamida Aurovitas 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Aurovitas Spain, S.A.U. |

Se muestran 5 de las 20 autorizaciones. Los textos de indicación aprobada no figuran en los datos recibidos, por lo que se sustituyó esa columna por el titular.

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

El único registro de interacción es de tipo farmacológico: safinamida actúa sobre su diana, la monoamino oxidasa B (MAO-B). No se trata de una interacción clínica entre fármacos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el vínculo mecanístico es limitado, porque no actuaría sobre el proceso inmunológico central de la enfermedad.

**Para avanzar se necesita:**
- Descargar y revisar la ficha técnica de AEMPS (advertencias y contraindicaciones), paso previo al cribado de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Buscar evidencia preclínica o casos clínicos en encefalitis de Rasmussen, en especial sobre control de convulsiones y excitotoxicidad.
- Evaluar la relevancia clínica frente a los tratamientos inmunomoduladores establecidos.

---

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

