---
layout: default
title: Efmoroctocog Alfa
parent: Solo predicción del modelo (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Efmoroctocog Alfa
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

# Efmoroctocog alfa: De Hemofilia A a Pseudo-enfermedad de von Willebrand

## Resumen en Una Frase

Efmoroctocog alfa es una proteína de fusión recombinante del factor VIII unido a Fc (FVIII-Fc), utilizada originalmente para la hemofilia A. El modelo TxGNN predice que podría ser efectivo para la **pseudo-enfermedad de von Willebrand** (von Willebrand de tipo plaquetario), pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia A (deducida del contexto del fármaco; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Pseudo-enfermedad de von Willebrand (pseudo-von Willebrand disease) |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, efmoroctocog alfa es un factor VIII recombinante fusionado a Fc, cuya eficacia en la hemofilia A (reposición del FVIII deficiente) está comprobada. Mecanísticamente, su aplicabilidad a la nueva indicación es dudosa.

La pseudo-enfermedad de von Willebrand (tipo plaquetario) se debe a una mutación de ganancia de función en GP1BA. Esta provoca una unión anormal entre las plaquetas y el factor von Willebrand (VWF) y la pérdida de multímeros grandes de VWF. La reposición de FVIII no corrige ese defecto. Cualquier vínculo con el fármaco es indirecto y se apoya solo en la predicción del modelo.

La puntuación alta probablemente refleja la cercanía en el grafo de conocimiento entre "trastornos hemorrágicos" y "hemostasia", más que una justificación biológica. Las otras nueve indicaciones predichas (rangos 2 a 10) también quedan en L5 y Hold, y la mayoría carece de un mecanismo plausible. La más próxima biológicamente es "hemofilia A con anomalía vascular", pero tampoco tiene evidencia aportada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 8 autorizaciones. Todas son de Swedish Orphan Biovitrum AB (Publ).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1151046005 | Elocta 1500 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable |
| 1151046004 | Elocta 1000 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable |
| 1151046002 | Elocta 500 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable |
| 1151046001 | Elocta 250 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable |
| 1151046007 | Elocta 3000 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni publicaciones. El defecto de la pseudo-enfermedad de von Willebrand está en la interacción GP1BA-VWF, no en la cantidad de FVIII, por lo que la reposición de FVIII no tiene una base mecanística clara.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un paso que bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar las indicaciones aprobadas de cada autorización española.
- Realizar una revisión de literatura dirigida (FVIII en el tipo plaquetario de von Willebrand) antes de reconsiderar la candidatura.
- Si se reevalúa el fármaco, priorizar "hemofilia A con anomalía vascular", que es la indicación más cercana biológicamente, definiendo antes su componente vascular o de VWF.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

