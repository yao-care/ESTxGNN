---
layout: default
title: Caplacizumab
parent: Solo predicción del modelo (L5)
nav_order: 99
evidence_level: L5
indication_count: 10
---

# Caplacizumab
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

# Caplacizumab: De Púrpura Trombocítica Trombótica Adquirida a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Caplacizumab es un nanobody anti-factor von Willebrand (vWF) comercializado en España como Cablivi. Por el contexto del caso (ver la nota más abajo), su uso original es la púrpura trombocitopénica trombótica adquirida (PTTa).
El modelo TxGNN predice que podría ser efectivo para **trastorno primario de liberación plaquetaria**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

> Nota: el campo de indicaciones originales del Evidence Pack está vacío y la ficha de AEMPS no incluye texto de indicación. La PTTa se toma de la justificación de reposicionamiento de la predicción n.º 5, que la identifica como la indicación comercializada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99,9998% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, caplacizumab se une al dominio A1 del vWF y bloquea su interacción con el receptor plaquetario GPIb-IX-V. Con ello evita la adhesión plaquetaria y la formación de microtrombos, y por eso es eficaz en la PTTa.

**En este caso la predicción no parece razonable.** En el trastorno primario de liberación plaquetaria, el defecto está en la secreción de gránulos, un paso posterior a la adhesión. Bloquear la adhesión mediada por vWF no aporta un beneficio plausible. Además, inhibir aún más la función plaquetaria aumentaría el riesgo de sangrado.

Lo más probable es que el puntaje alto de TxGNN refleje la cercanía entre nodos en la ontología de trastornos plaquetarios y no una base terapéutica real. Ninguna de las otras predicciones de sangrado o de función plaquetaria (pseudo-enfermedad de von Willebrand, trombastenia de Glanzmann, síndrome de Scott, hemofilia, entre otras) tiene sustento mecanístico. En todas, el bloqueo de vWF-GPIb empeoraría el sangrado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1181305001 | CABLIVI 10 MG POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE (Ablynx) | Polvo y disolvente para solución inyectable |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe evidencia clínica ni preclínica para esta indicación (L5) y el mecanismo apunta a un riesgo mayor de sangrado. El puntaje TxGNN por sí solo no basta para avanzar.

**Nota sobre la PTTa:** la predicción n.º 5 (púrpura trombocitopénica trombótica) sí tiene respaldo sólido. Incluye 13 ensayos clínicos, entre ellos los Fase 3 HERCULES (NCT02553317) y NCT05468320, y 20 publicaciones. Su nivel de evidencia es L1 y su decisión es *Proceed with Guardrails*. Es la indicación ya comercializada, por lo que no constituye un reposicionamiento real.

**Para avanzar se necesita:**
- Completar el texto de indicación aprobada y la advertencias/contraindicaciones desde la ficha técnica de AEMPS.
- Completar el mecanismo de acción desde DrugBank.
- Dar prioridad a la predicción de PTTa, con vigilancia del riesgo de sangrado, monitorización de ADAMTS13 e inmunosupresión concomitante, según las guías ISTH 2020 y su actualización de 2025.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

