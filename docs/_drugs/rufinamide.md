---
layout: default
title: Rufinamide
parent: Solo predicción del modelo (L5)
nav_order: 717
evidence_level: L5
indication_count: 5
---

# Rufinamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Rufinamida: De Síndrome de Lennox-Gastaut a Síndrome de Epilepsia Relacionada con Infección Febril (FIRES)

## Resumen en Una Frase

Rufinamida es un antiepiléptico originalmente utilizado para el tratamiento del síndrome de Lennox-Gastaut.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de epilepsia relacionada con infección febril (FIRES)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome de Lennox-Gastaut (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles en los datos compilados) |
| Nueva Indicación Predicha | Síndrome de epilepsia relacionada con infección febril (FIRES) |
| Puntaje de Predicción TxGNN | 99.57% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la rufinamida es un modulador de los canales de sodio dependientes de voltaje: prolonga su estado inactivo y, en principio, podría reducir la hiperexcitabilidad neuronal en epilepsias refractarias. Su eficacia en el síndrome de Lennox-Gastaut, una encefalopatía epiléptica, está reconocida.

La relación con FIRES es débil. FIRES es una epilepsia refractaria muy grave, pero su patología parece estar impulsada en gran medida por neuroinflamación (por ejemplo, las vías de IL-1 e IL-6), por lo que un mecanismo basado en canales de sodio probablemente no aborde el problema de fondo.

Por tanto, el vínculo se apoya solo en el puntaje del modelo (0.996), sin ensayos ni literatura. Debe considerarse una hipótesis que requiere validación.

### Otras indicaciones predichas (para contexto)

| Rango | Indicación predicha | Puntaje TxGNN | Nivel | Observación |
|------|------|------|------|------|
| 2 | Mioclonía perioral con ausencias | 99.51% | L5 | Los bloqueadores de canales de sodio pueden agravar ausencias y crisis mioclónicas |
| 3 | Epilepsia fotosensible del lóbulo occipital | 99.44% | L5 | Plausibilidad general de clase para crisis focales |
| 4 | Espasmos epilépticos criptogénicos de inicio tardío | 99.44% | L5 | Solapamiento clínico indirecto con Lennox-Gastaut |
| 5 | Epilepsia infantil atípica con puntas centrotemporales | 99.44% | L5 | Posible empeoramiento con bloqueadores de sodio si hay punta-onda continua durante el sueño |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 06378009 | INOVELON 200 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 06378001 | INOVELON 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 06378017 | INOVELON 40 mg/ml suspensión oral | Suspensión oral | No disponible en los datos compilados |
| 06378015 | INOVELON 400 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

Las cuatro autorizaciones son de monocomponente, vigentes y del titular Eisai GmbH.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, leucopenia, trastorno de ansiedad, trastorno neurótico y trastorno distímico.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Las 20 mostradas son todas de nivel moderado, entre ellas hidrocortisona, betametasona, triamcinolona, prednisona, colecalciferol, calcifediol, calcitriol, pioglitazona, bupropión, morfina, metoclopramida, ondansetrón, difenoxilato, difenoxina, dronabinol, nabilona, eliglustat, naloxegol, nitisinona y rolapitant.
- **Consideración específica de la indicación**: en mioclonía perioral con ausencias y en epilepsia infantil atípica con puntas centrotemporales, los bloqueadores de canales de sodio podrían empeorar las crisis.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones oficiales).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero es de nivel L5: no existen ensayos clínicos ni literatura, y el mecanismo de canales de sodio no se corresponde bien con la patología inflamatoria de FIRES. Además, faltan las advertencias y contraindicaciones oficiales.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales), hoy un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, mediante DrugBank).
- Revisión sistemática de literatura y registros de ensayos sobre rufinamida en FIRES y encefalopatías epilépticas afines.
- Evaluar mecanísticamente la relevancia de la neuroinflamación frente al bloqueo de canales de sodio.
- Valorar si alguna de las otras indicaciones predichas (por ejemplo, espasmos epilépticos de inicio tardío, por su cercanía clínica con Lennox-Gastaut) tiene un mejor perfil de beneficio-riesgo.
- Verificar la compatibilidad de las vías de administración (comprimidos y suspensión oral) con la población pediátrica objetivo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

