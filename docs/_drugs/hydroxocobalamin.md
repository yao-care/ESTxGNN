---
layout: default
title: Hydroxocobalamin
parent: Solo predicción del modelo (L5)
nav_order: 267
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Hidroxocobalamina: De Indicación Original No Registrada a Várices Esofágicas con Sangrado

## Resumen en Una Frase

La hidroxocobalamina es una forma de vitamina B12 comercializada en España en inyectables y en kits para perfusión, pero los datos disponibles no recogen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **várices esofágicas con sangrado**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las 4 autorizaciones están vacíos) |
| Nueva Indicación Predicha | Várices esofágicas con sangrado |
| Puntaje de Predicción TxGNN | 99.23% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción ni sobre las indicaciones originales. Los nombres de los productos autorizados (MEGAMILBEDOCE, HIDROXOCOBALAMINA BASI y CYANOKIT) sugieren usos como vitamina B12 y como antídoto en intoxicación por cianuro. Es una inferencia a partir de los nombres, no un dato del expediente.

Existe una hipótesis especulativa y no verificada. La hidroxocobalamina es conocida por captar óxido nítrico (NO) y sulfuro de hidrógeno (H2S). La vasodilatación esplácnica mediada por exceso de NO contribuye a la hipertensión portal, que a su vez favorece las várices esofágicas. Ningún dato aportado respalda este vínculo.

Hay además motivos para desconfiar del resultado:
- El puntaje es idéntico para las variantes con y sin sangrado (99.23%), lo que apunta a una predicción a nivel de clase de enfermedad y no a una señal específica de sangrado.
- El sangrado agudo de várices ya se maneja con terapias establecidas (fármacos vasoactivos, ligadura endoscópica con bandas y profilaxis antibiótica), y una forma de vitamina B12 no tiene un papel reconocido en ese contexto.

También se predijo la indicación **várices esofágicas sin sangrado**, con el mismo puntaje y la misma ausencia de evidencia. Su profilaxis primaria estándar (betabloqueantes no selectivos, ligadura con bandas) tampoco tiene equivalente en evidencia para la hidroxocobalamina.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 46090 | MEGAMILBEDOCE 5.000 MICROGRAMOS/ML SOLUCIÓN INYECTABLE | Solución inyectable | Aristo Pharma Iberia S.L. |
| 07420001 | CYANOKIT 2,5 g POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Polvo para solución para perfusión | Serb Sa |
| 88743 | HIDROXOCOBALAMINA BASI 1 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | Laboratorios Basi Industria Farmacéutica S.A. |
| 07420002 | CYANOKIT 5 g POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Polvo para solución para perfusión | Serb Sa |

Las cuatro autorizaciones tienen el texto de indicación aprobada vacío en los datos recibidos.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el grafo de TxGNN (nivel L5), sin ensayos ni literatura. El puntaje idéntico para las variantes con y sin sangrado sugiere un artefacto de clase. Además, el sangrado variceal tiene tratamientos establecidos sin papel conocido para la vitamina B12.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), que es un requisito bloqueante para el cribado de seguridad.
- Completar el mecanismo de acción y las indicaciones originales desde DrugBank.
- Revisar sistemáticamente la literatura preclínica sobre captación de NO/H2S e hipertensión portal.
- Definir la compatibilidad de vía de administración y la similitud con la indicación original, hoy pendientes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

