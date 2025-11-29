# Case 03 — Análisis de Clústeres (Segmentación de Clientes)

**Fecha del análisis:** Noviembre 2025  
**Cliente:** Megamart Retail Group  
**Metodologías aplicadas:** K-Means (particional) y Clustering Jerárquico (aglutinativo)  
**Datos:** Demográficos y comportamiento de gasto de clientes (muestra)  
**Objetivo:** Segmentación no supervisada para diseño de estrategias de marketing

---

## Contenido
- 1. Contexto de negocio  
- 2. Metodología  
- 3. Dataset y variables clave  
- 4. Hallazgos principales  
- 5. Recomendaciones de negocio  
- 6. Estructura del caso y archivos  
- 7. Reproducibilidad y ejecución  
- 8. Referencias

---

## 1. Contexto de negocio
Megamart busca pasar de una estrategia de marketing genérica a campañas personalizadas identificando segmentos de clientes con comportamientos y potenciales de valor distintos.

---

## 2. Metodología
- K-Means: segmentación principal, optimización por inercia.  
- Clustering jerárquico: validación visual (dendrograma) y apoyo en la selección de K.  
Decisiones clave: StandardScaler para escalado, Euclidean como métrica, selección de K con Elbow + silhouette.

### Librerías principales
pandas, numpy, scikit-learn, matplotlib, seaborn, scipy

---

## 3. Dataset y variables clave
Fuente: Megamart Loyalty Program (muestra de 200 observaciones).  
Variables principales usadas en el clustering:  
- Annual Income (k$)  
- Spending Score (1-100)  
- Age (usada para análisis complementario)

(Estructura completa en data/megamart_data_dictionary.md)

---

## 4. Hallazgos principales
- K óptimo sugerido: 5 clústeres (Elbow + dendrograma).  
- Perfiles identificados:
  - 0 — Ahorradores cautelosos (alto ingreso, bajo gasto)  
  - 1 — Promedio estándar (ingreso y gasto medios)  
  - 2 — VIP (alto ingreso, alto gasto)  
  - 3 — Gastadores despreocupados (bajo ingreso, alto gasto)  
  - 4 — Presupuesto ajustado (bajo ingreso, bajo gasto)  
- Edad correlaciona con comportamiento: grupos jóvenes concentran gasto alto relativo.

---

## 5. Recomendaciones de negocio (resumen)
- Segmento VIP: programa de fidelización premium.  
- Ahorradores: cross-selling basado en calidad, no descuentos.  
- Gastadores jóvenes: marketing digital y opciones de pago flexibles.  
- Segmento medio: campañas de volumen y retención con bajo costo.

---

## 6. Estructura del repositorio
case-03-customer-segmentation/
├── README.md  
├── data/  
│   ├── megamart_customers.csv  
│   └── megamart_data_dictionary.md  
├── notebooks/  
│   └── MegamartClustering.ipynb  
├── reports/  
│   ├── customer_profiles.pdf  
│   └── marketing_strategy_v1.pptx  
└── visualizations/  
    ├── elbow_method.png  
    ├── dendrogram.png  
    ├── clusters_2d_scatter.png  
    └── clusters_3d_age.png

---

## 7. Reproducibilidad — cómo ejecutar (Windows)
1. Crear entorno virtual (opcional):
   - python -m venv .venv
   - .venv\Scripts\activate
2. Instalar dependencias:
   - pip install -r requirements.txt
3. Abrir y ejecutar el notebook:
   - cd notebooks
   - jupyter notebook MegamartClustering.ipynb
   (o jupyter lab)

Notas: Escalar variables con StandardScaler antes de aplicar K-Means. Validar K con Elbow + silhouette y revisar dendrograma.

---

## 8. Referencias
- Hartigan, J. A. (1975). Clustering Algorithms.  
- Kaufman, L., & Rousseeuw, P. J. (2009). Finding groups in data.  
- Ng, A. (2000). K-means and Elbow Method (CS229 notes).

Licencia: MIT