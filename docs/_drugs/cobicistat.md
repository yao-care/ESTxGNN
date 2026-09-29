---
layout: default
title: Cobicistat
parent: Solo predicción del modelo (L5)
nav_order: 142
evidence_level: L5
indication_count: 3
---

# Cobicistat
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

# Cobicistat: De Potenciador Farmacocinetico en la Infeccion por VIH-1 a Infeccion por el Virus de la Inmunodeficiencia Simia

## Resumen en Una Frase

Cobicistat es un inhibidor de CYP3A que se comercializa como potenciador farmacocinetico de antirretrovirales contra el VIH-1.
El modelo TxGNN predice que podria ser util en la **infeccion por el virus de la inmunodeficiencia simia (VIS)**,
pero actualmente hay **0 ensayos clinicos** y **0 publicaciones** que respalden esta direccion, por lo que es solo una prediccion del modelo.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Nueva Indicacion Predicha | Infeccion por el virus de la inmunodeficiencia simia (VIS) |
| Puntaje de Prediccion TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | ✓ Comercializado |
| Numero de Autorizaciones | 1 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en el paquete de evidencia. Segun la informacion conocida, cobicistat inhibe la enzima CYP3A y se usa como potenciador farmacocinetico junto con antirretrovirales como elvitegravir, darunavir y atazanavir. No tiene actividad antiviral propia relevante. Su funcion es aumentar la exposicion del antirretroviral que lo acompana.

El VIS es un lentivirus de primates muy parecido al VIH-1. Lo mas probable es que la puntuacion alta refleje la cercania en el grafo de conocimiento con el VIH-1, y no un efecto directo sobre el VIS. Cualquier utilidad seria indirecta, por ejemplo potenciar antirretrovirales coadministrados en modelos animales de VIS.

Este vinculo es una inferencia, no un hecho verificado. Los datos de origen no incluyen indicaciones originales ni mecanismo de accion, y no hay ensayos ni literatura que lo apoyen.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Informacion de Mercado en Espana

| Numero de Autorizacion | Nombre del Producto | Forma Farmaceutica | Titular |
|---------|------|------|-----------|
| 113872001 | TYBOST 150mg comprimidos recubiertos con pelicula | Comprimido recubierto con pelicula | Gilead Sciences Ireland Unlimited Company |

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion se apoya solo en el modelo (L5). No hay ensayos ni publicaciones, y el mecanismo es indirecto, ya que cobicistat solo potenciaria a otro antirretroviral. Ademas, el VIS es una infeccion animal, por lo que el flujo de reposicionamiento para uso humano no se aplica directamente.

**Para avanzar se necesita:**
- Datos del mecanismo de accion desde DrugBank.
- Advertencias y contraindicaciones del prospecto de AEMPS.
- Estudios preclinicos en modelos de VIS que evaluen cobicistat como potenciador de un antirretroviral concreto.
- Una justificacion clara de la relevancia para uso humano.

**Otras predicciones del modelo (no priorizadas):**
- **Sindrome de inmunodeficiencia adquirida felina** (99.92%): indicacion veterinaria, sin evidencia. Decision: Hold.
- **Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y disminucion de la sustancia blanca cortical** (99.91%): no se identifico ningun vinculo mecanistico plausible, y probablemente sea un artefacto del grafo. Decision: Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

