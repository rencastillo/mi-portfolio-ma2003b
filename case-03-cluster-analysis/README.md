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

# Case 03: Análisis de Clústeres — Segmentación de Clientes

**Fecha del análisis**: Noviembre 2025  
**Cliente**: Megamart Retail Group  
**Metodologías aplicadas**: K-Means, Clustering Jerárquico (dendrograma), análisis de silhouette  
**Datos**: Demográficos y comportamiento de gasto de clientes (muestra)  
**Objetivo**: Segmentación no supervisada para diseño de estrategias de marketing y personalización

## 📹 Presentación en Video
[**Ver el Video de Case 03 — Segmentación Megamart**](https://drive.google.com/file/d/1tPVL8W6lEwPGtgwEMRshIULkYKvjriua/view?usp=sharing)

---

## 1. Contexto del Negocio

Megamart busca pasar de una estrategia de marketing genérica a campañas personalizadas identificando segmentos de clientes con comportamientos y potenciales de valor distintos. La segmentación permitirá diseñar promociones, programas de fidelización y acciones de retención más eficientes.

---

## 2. Metodología

### Métodos aplicados
- **K-Means**: segmentación principal, optimización por inercia y evaluación con silhouette.
- **Clustering Jerárquico (aglutinativo)**: dendrograma para apoyar la selección de K y validar la estructura.

### Decisiones metodológicas clave
- **Escalado**: `StandardScaler` aplicado antes de clustering.
- **Métrica**: Euclidean para K-Means y Ward para jerárquico.
- **Selección de K**: Elbow method + silhouette score + inspección de dendrograma.

### Herramientas y librerías
```text
pandas (>=2.0)
numpy (>=2.0)
scikit-learn (>=1.2)
matplotlib
seaborn
scipy
plotly (opcional)
```

---

## 3. Datos

- **Fuente**: Megamart Loyalty Program (muestra).  
- **Tamaño**: ~200 observaciones (ejemplo) — ajustar según dataset real.  
- **Variables clave**:
   - `annual_income` (k$)
   - `spending_score` (1-100)
   - `age`
   - `purchase_frequency` (opcional)

Ver diccionario completo en: `data/megamar t_data_dictionary.md` (o el archivo equivalente en `data/`).

---

## 4. Hallazgos Principales

- **K sugerido**: 5 clústeres (Elbow + silhouette + dendrograma).
- **Perfiles identificados**:
   - **Cluster 0 — Ahorradores cautelosos**: alto ingreso, bajo gasto.
   - **Cluster 1 — Promedio**: ingreso y gasto medios.
   - **Cluster 2 — VIP**: alto ingreso, alto gasto.
   - **Cluster 3 — Gastadores jóvenes**: bajo/medio ingreso, alto gasto.
   - **Cluster 4 — Presupuesto ajustado**: bajo ingreso, bajo gasto.

- **Edad** correlaciona con comportamiento; segmentos jóvenes concentran gasto relativo mayor.

Implicación: Estos perfiles permiten acciones dirigidas (fidelización premium, cross-sell, promociones digitales, campañas de retención).

---

## 5. Recomendaciones de Negocio

- **Segmento VIP**: lanzar programa premium con beneficios exclusivos y ofertas personalizadas.
- **Ahorradores**: enfoque en productos de valor (cross-selling) y no en descuentos frecuentes.
- **Gastadores jóvenes**: campañas digitales y pagos flexibles (BNPL, descuentos temporales).
- **Presupuesto ajustado**: promociones por volumen y ofertas de bajo costo.

Monitoreo: definir KPIs por segmento (LTV, churn, avg order value) y re-segmentar trimestralmente.

---

## 6. Contenido del Caso

```
case-03-cluster-analysis/
├── README.md                               # Este documento
├── data/
│   ├── retail_customer_data-1.csv
│   └── retail_customer_data_with_labels-1.csv (si existe)
├── notebooks/
│   └── MegamartClustering.ipynb            # Notebook principal
├── reports/
│   └── customer_profiles.pdf
└── visualizations/
      ├── elbow_method.png
      ├── dendrogram.png
      ├── clusters_2d_scatter.png
      └── clusters_3d_age.png
```

---

## 7. Reproducibilidad — Cómo ejecutar (macOS / Linux)

1. Crear y activar entorno virtual (zsh):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar el notebook:

```bash
cd notebooks
jupyter notebook MegamartClustering.ipynb
# o jupyter lab
```

Notas:
- Ajustar `random_state` para reproducibilidad.
- Escalar solo con los parámetros aprendidos en el conjunto de entrenamiento.
- Validar elección de K con cross-validation y scores de silhouette.

---

## 8. Referencias

- Hartigan, J. A. (1975). Clustering Algorithms.
- Kaufman, L., & Rousseeuw, P. J. (2009). Finding groups in data.
- Ng, A. (2000). K-means and Elbow Method (CS229 notes).

**Portfolio**: MA2003B - Análisis Multivariado  
**Software**: Python 3.x  
**Licencia**: MIT
