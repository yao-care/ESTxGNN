---
layout: default
title: Política de privacidad
nav_order: 95
permalink: /privacy-policy/
description: "Política de privacidad de ESTxGNN: sitio estático sin cuentas ni formularios; usa cookies analíticas de Google Analytics 4 para estadísticas de uso."
---

# Política de privacidad

<div class="key-takeaway">
Este es un sitio estático: no requiere registro y no tiene formularios. Usa cookies analíticas de Google Analytics 4 para elaborar estadísticas de uso.
</div>

---

## Qué recopilamos

<p class="key-answer" data-question="¿Recopila ESTxGNN datos personales?">
<strong>Solo estadísticas de uso, mediante Google Analytics 4.</strong> Este sitio está alojado en GitHub Pages como un sitio puramente estático.
No hay sistema de cuentas ni formularios, y no recopilamos nombres, direcciones de correo electrónico ni historias
clínicas. El sitio usa cookies analíticas de Google Analytics 4 para elaborar estadísticas de uso (páginas vistas,
sitio de procedencia, profundidad de desplazamiento y tiempo en la página). Las cookies se instalan al cargar la
página; no se envían términos de búsqueda, contenidos de formularios ni parámetros de consulta de la URL.
</p>

---

## Servicios de terceros

El sitio utiliza los siguientes recursos de terceros, que pueden registrar los accesos conforme a sus propias
políticas:

| Servicio | Finalidad | Política de privacidad |
|---------|---------|----------------|
| GitHub Pages | Alojamiento del sitio | [Declaración de privacidad de GitHub](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement) |
| Google Analytics 4 (www.googletagmanager.com, google-analytics.com) | Estadísticas de visitas (páginas vistas, procedencia); usa cookies de analítica. No se envían términos de búsqueda, contenido de formularios ni parámetros de la URL. | [Política de privacidad de Google](https://policies.google.com/privacy) |
| cdn.jsdelivr.net | Bibliotecas de scripts: gráficos d3 en todas las páginas; Fuse.js para comparar nombres y el cliente SMART on FHIR en las páginas SMART | [Política de privacidad de jsDelivr](https://www.jsdelivr.com/terms/privacy-policy-jsdelivr-net) |
| clinicaltrials.gov | Búsqueda de ensayos clínicos en las páginas SMART: solo cuando usted la solicita, se envían los nombres del medicamento y de la indicación a la API de ClinicalTrials.gov | [Políticas web de la NLM](https://www.nlm.nih.gov/web_policies.html) |
| rxnav.nlm.nih.gov | Aplicación SMART: los códigos RxNorm de los medicamentos leídos de su historia clínica electrónica se envían a la API RxNav de la NLM para obtener el nombre del principio activo (sin datos que identifiquen al paciente) | [Políticas web de la NLM](https://www.nlm.nih.gov/web_policies.html) |

Cuando usted inicia activamente la aplicación SMART on FHIR, esta solicita datos de medicación a su sistema de
historia clínica electrónica. La identidad del paciente y los datos de la historia clínica <strong>no se envían a los
servidores de este sitio</strong> (es un sitio estático, sin backend) y este sitio no los almacena. Para identificar los
medicamentos, la aplicación envía sus códigos RxNorm al servicio RxNav de la Biblioteca Nacional de Medicina de
EE. UU.; estos códigos no contienen datos que identifiquen al paciente. Cuando usted solicita ensayos clínicos, se
envían a ClinicalTrials.gov los nombres del medicamento y de la indicación.

---

<!-- privacy-law:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改；法規與連結見 .claude/privacy_text_20261119.py）-->
## Legislación aplicable

Para visitantes en España se aplican el [Reglamento General de Protección de Datos (RGPD)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) y la [Ley Orgánica 3/2018 (LOPDGDD)](https://www.boe.es/eli/es/lo/2018/12/05/3); las cookies de análisis también se rigen por la LSSI. La autoridad de control es la [Agencia Española de Protección de Datos (AEPD)](https://www.aepd.es/). El responsable está en Taiwán y no tiene establecimiento en la UE; el tratamiento afectado son los datos de uso de Google Analytics 4.

## Sus derechos y cómo ejercerlos

- Derecho de acceso (art. 15 RGPD) y de rectificación (art. 16).
- Derecho de supresión (art. 17) y de limitación (art. 18).
- Derecho de oposición (art. 21), también a la analítica.
- Derecho a reclamar ante la AEPD (art. 77).

Solicitudes: service@yao.care (no hay cuentas: indique la fecha y las páginas de su visita). Puede bloquear o borrar las cookies de análisis en su navegador.

## Derechos de autor y fuentes de datos

Los textos del sitio están protegidos por el [texto refundido de la Ley de Propiedad Intelectual (Real Decreto Legislativo 1/1996)](https://www.boe.es/eli/es/rdlg/1996/04/12/1/con). El código del sitio se publica con licencia MIT en el [repositorio de GitHub](https://github.com/yao-care/ESTxGNN); los textos de los informes son © 藥提醒科技有限公司 (yao.care).

Fuentes de datos de este sitio y sus condiciones:

- Datos de **TxGNN** (Harvard Dataverse): CC0 1.0; cite Huang et al., *Nature Medicine* 2024.
- **ClinicalTrials.gov**, **PubMed**: [condiciones de ClinicalTrials.gov](https://clinicaltrials.gov/about-site/terms-conditions), [políticas del NCBI](https://www.ncbi.nlm.nih.gov/home/about/policies/).
- **DrugBank**: términos de licencia de [DrugBank](https://go.drugbank.com/), uso no comercial.
- **Conjunto de datos local**: [AEMPS: CIMA](https://cima.aemps.es/cima/rest/medicamentos), publicado por Agencia Española de Medicamentos y Productos Sanitarios (AEMPS); su reutilización se rige por las condiciones del editor, y este sitio no otorga derechos adicionales.

<!-- privacy-law:end -->

---

## Cambios en esta política

Cualquier cambio se publicará directamente en esta página.

---

## Sobre el desarrollador

Esta plataforma está desarrollada y operada por **藥提醒科技有限公司** (yao.care). Consulte la página
<a href="{{ '/about/' | relative_url }}">Acerca de</a> para conocer los antecedentes completos de la empresa y de la metodología.

---

<div class="disclaimer">
<strong>Descargo de responsabilidad</strong><br>
Este informe tiene únicamente fines de consulta para la investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Cualquier decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
