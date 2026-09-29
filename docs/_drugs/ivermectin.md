---
layout: default
title: Ivermectin
parent: Solo predicción del modelo (L5)
nav_order: 296
evidence_level: L5
indication_count: 9
---

# Ivermectin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Ivermectina: De Infecciones Parasitarias a Candidiasis Vulvovaginal

## Resumen en Una Frase

La ivermectina es un antiparasitario utilizado en infecciones parasitarias (excluida la tenia) y, en crema, en otras afecciones dermatológicas. El modelo TxGNN predice que podría ser efectiva para la **candidiasis vulvovaginal**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones parasitarias (según datos farmacológicos; los textos de indicación de AEMPS no están disponibles) |
| Nueva Indicación Predicha | Candidiasis vulvovaginal |
| Puntaje de Predicción TxGNN | 99,95 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de origen. Según la información conocida, la ivermectina actúa en invertebrados activando los canales de cloruro dependientes de glutamato, lo que paraliza y elimina al parásito. Los datos farmacológicos aportados también la vinculan con el receptor de glicina, el receptor nicotínico de acetilcolina α7 (CHRNA7), P2X4 (dato de rata) y P2X7. Ninguno de estos blancos describe un efecto antifúngico.

La indicación original (parasitosis) y la nueva (infección por *Candida*) no comparten un mecanismo evidente. Los datos suministrados no documentan actividad antifúngica, y la puntuación alta no está respaldada por ningún ensayo ni publicación. Por ahora, la predicción debe considerarse una hipótesis del modelo y no un hallazgo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 85728 | IVERGALEN 3 MG COMPRIMIDOS EFG | Comprimido |
| 85956 | ZULIMA 3 MG COMPRIMIDOS EFG | Comprimido |
| 79911 | SOOLANTRA 10 MG/G CREMA | Crema |
| 86297 | IVERCARE 3 MG COMPRIMIDOS EFG | Comprimido |
| 88545 | IVERMECTINA TEVA 3 MG COMPRIMIDOS EFG | Comprimido |

Nota: el registro indica 6 autorizaciones en total, pero solo se detallan 5. Los textos de indicación aprobada no figuran en los datos recibidos, por lo que se omite esa columna.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Las advertencias y contraindicaciones de AEMPS no están disponibles. Las 4 entradas de la consulta de interacciones son blancos farmacológicos (receptores) y no interacciones con otros medicamentos, por lo que no hay datos de interacciones farmacológicas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ningún ensayo clínico ni publicación de respaldo (nivel L5), y no existe un mecanismo antifúngico documentado. Las otras 8 predicciones del modelo (candidiasis esofágica, VPH anogenital, vulvovaginitis, candidiasis neonatal, entre otras) también son L5 y quedan en Hold. Los dos artículos vinculados a candidiasis esofágica y congénita tratan de usos antiparasitarios (estrongiloidiasis y sarna costrosa) y no son evidencia antifúngica.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), que bloquea el cribado de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Estudios preclínicos in vitro de actividad antifúngica frente a *Candida* (por ejemplo, CMI).
- Revisar la literatura y los registros de ensayos con una búsqueda específica de ivermectina y candidiasis.
- Definir la vía de administración (oral o tópica) y comprobar su compatibilidad con los productos autorizados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

