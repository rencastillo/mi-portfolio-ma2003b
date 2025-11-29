# Portfolio de Análisis Multivariado (MA2003B)

**Institución:** Tecnológico de Monterrey (ITESM)
**Fecha de Entrega:** Noviembre 2025
**Software Principal:** Python 3.12 (scikit-learn, pandas, seaborn)

---

## 1. Información del Equipo

A continuación se presentan los integrantes responsables del desarrollo de los tres casos de estudio:

| Nombre Completo | Matrícula (ID) | Rol Principal |
| :--- | :--- | :--- |
| [Mario Carlos Gaitan Reyna] | [A01659057] | [Ej: Modelado / EDA / Limpieza] |
| [Renato Castillo Camarena] | [A01029375] | [Ej: Business Intel / Visualización / Documentación] |


---

## 2. Resumen Ejecutivo de Casos

Este portafolio integra tres aplicaciones de técnicas multivariadas para resolver problemas de negocio complejos mediante la reducción de dimensiones, la clasificación predictiva y la segmentación de mercado.

| Proyecto | Cliente / Industria | Técnica Principal | Objetivo de Negocio |
| :--- | :--- | :--- | :--- |
| **Caso 01** | **TechComm Inc.** (Telecomunicaciones) | **Factor Analysis (EFA)** | **Satisfacción del Cliente:** Reducir 30+ variables de encuestas en dimensiones latentes (e.g., Servicio, Precio, Cobertura) para priorizar áreas de mejora. |
| **Caso 02** | **LendSmart** (Fintech / Banca) | **Discriminant Analysis (LDA/QDA)** | **Riesgo Crediticio:** Crear un modelo supervisado para clasificar solicitudes de préstamo en "Aprobados" o "Default" y minimizar pérdidas financieras. |
| **Caso 03** | **Megamart Group** (Retail) | **Cluster Analysis (K-Means)** | **Segmentación de Clientes:** Agrupar consumidores sin etiquetas previas basándose en Ingresos y Score de Gasto para personalizar campañas de marketing. |

---

## 3. Comparación Metodológica

A lo largo del curso, hemos aplicado tres familias distintas de algoritmos. A continuación se presenta una comparativa técnica de cuándo y por qué se utilizó cada una.

### 3.1. Tabla Comparativa

| Característica | Factor Analysis (Caso 01) | Discriminant Analysis (Caso 02) | Cluster Analysis (Caso 03) |
| :--- | :--- | :--- | :--- |
| **Tipo de Aprendizaje** | No Supervisado | Supervisado | No Supervisado |
| **Enfoque Principal** | **Columnas (Variables):** Busca agrupar variables correlacionadas. | **Etiquetas (Clases):** Busca separar grupos predefinidos. | **Filas (Observaciones):** Busca agrupar individuos similares. |
| **Variable Target (Y)** | No existe. | Sí existe (Categórica: 0/1). | No existe. |
| **Supuestos Clave** | Multicolinealidad necesaria (KMO > 0.6). | Normalidad multivariada y homogeneidad de covarianzas. | Sensibilidad a la escala (requiere estandarización). |
| **Resultado Clave** | Factores Latentes (Conceptos abstractos). | Funciones Discriminantes (Reglas de decisión). | Centroides y Perfiles (Tipos de clientes). |

### 3.2. Análisis de Idoneidad

1.  **Por qué Factor Analysis en el Caso 01:**
    El problema era la **redundancia**. Teníamos demasiadas preguntas en la encuesta que medían lo mismo. Discriminant o Cluster no hubieran servido para simplificar la estructura de las variables, solo Factor Analysis permite descubrir "conceptos" ocultos detrás de los datos.

2.  **Por qué Discriminant Analysis (LDA/QDA) en el Caso 02:**
    El problema era de **predicción**. Teníamos historia (sabíamos quién pagó y quién no). Usar Clustering habría ignorado esta valiosa información histórica. LDA/QDA son ideales para maximizar la separación entre clases conocidas.

3.  **Por qué Cluster Analysis en el Caso 03:**
    El problema era de **descubrimiento**. No sabíamos qué tipos de clientes existían. No podíamos usar Discriminant Analysis porque no teníamos una variable "Target" que nos dijera a qué grupo pertenecían. El agrupamiento fue la única vía para encontrar la estructura natural del mercado.

---

## 4. Lecciones Aprendidas

Tras la ejecución de los tres proyectos, el equipo ha consolidado las siguientes reflexiones técnicas y de negocio:

### A. La Importancia del Preprocesamiento
En los tres casos, el éxito del modelo dependió en un **80% de la limpieza de datos**.
* En **Cluster (C03)**, si no hubiéramos escalado los datos (`StandardScaler`), la variable de "Ingresos" habría dominado al "Score", arruinando la segmentación.
* En **Discriminant (C02)**, el manejo de *outliers* fue vital, ya que LDA es muy sensible a valores extremos que distorsionan la media.

### B. No existe el "Mejor Modelo" Universal
Aprendimos que la complejidad no siempre es mejor.
* En el Caso 02, aunque **QDA** es más flexible (curvas cuadráticas), **LDA** (líneas rectas) ofreció mayor estabilidad y menor riesgo de *overfitting*, demostrando que a veces la simplicidad es preferible para la implementación en producción.

### C. Traducción de Datos a Estrategia
Los algoritmos matemáticos (Eigenvalues, Inercia, Distancia de Mahalanobis) son inútiles si no se traducen a acciones.
* El mayor valor del **Caso 03** no fue el gráfico de codo, sino la identificación del grupo "VIP" para crear un programa de fidelización.
* El valor del **Caso 01** no fueron las cargas factoriales, sino entender que el "Servicio al Cliente" pesaba más que el "Precio" en la satisfacción global.

---

## 5. Stack Tecnológico Utilizado

Para reproducir cualquiera de los tres proyectos, se requiere el siguiente entorno:

* **Lenguaje:** Python 3.12+
* **Manipulación de Datos:** Pandas, NumPy.
* **Modelado Estadístico:** Scikit-learn (PCA, LDA, QDA, KMeans), FactorAnalyzer, SciPy.
* **Visualización:** Matplotlib, Seaborn, Plotly (para gráficos interactivos).

---

## 6. Estructura del Repositorio

```
mi-portfolio-ma2003b/
│
├── README.md                                           # Este documento
├── LICENSE                                             # Licencia (MIT)
├── pyproject.toml                                      # Configuración del proyecto Python
├── requirements.txt                                    # Dependencias del proyecto
│
├── case-01-factor-analysis/
│   ├── README.md                                       # Documentación Case 01: Factor Analysis
│   ├── data/
│   │   ├── customer_satisfaction_data.csv              # Dataset (encuestas, 30+ variables)
│   │   └── customer_satisfaction_data_dictionary.md    # Diccionario de datos
│   ├── notebooks/
│   │   └── Costumer_service.ipynb                      # Notebook con análisis factorial
│   ├── reports/                                        # Reportes generados
│   └── visualizations/                                 # Gráficos (scree plot, cargas, etc.)
│
├── case-02-discriminant-analysis/
│   ├── README.md                                       # Documentación Case 02: Discriminant Analysis
│   │                                                   # 📹 Incluye enlace de video
│   ├── data/
│   │   ├── credit_risk_data.csv                        # Dataset (10,000+ registros)
│   │   └── credit_risk_data_dictionary.md              # Diccionario de datos
│   ├── notebooks/
│   │   └── LendSmart_Analysis.ipynb                    # Notebook con LDA vs QDA
│   ├── reports/                                        # Reportes generados
│   └── visualizations/                                 # Gráficos (ROC, matrices de confusión, etc.)
│
├── case-03-cluster-analysis/
│   ├── README.md                                       # Documentación Case 03: Cluster Analysis
│   │                                                   # 📹 Incluye enlace de video
│   ├── data/
│   │   ├── retail_customer_data-1.csv                  # Dataset (segmentación de clientes)
│   │   └── retail_customer_data_with_labels-1.csv     # Dataset etiquetado
│   ├── notebooks/
│   │   └── MegamartClusttetring.ipynb                  # Notebook con K-Means y clustering jerárquico
│   ├── reports/                                        # Reportes generados
│   └── visualizations/                                 # Gráficos (elbow, dendrograma, scatter, etc.)
│
└── presentation/                                        # Presentaciones finales
```

### Descripción de Carpetas Clave

- **case-0X-XXX/**: Cada carpeta es un caso de estudio independiente con su propia documentación, datos y análisis.
- **data/**: Contiene datasets originales en CSV y diccionarios de datos en Markdown.
- **notebooks/**: Jupyter Notebooks con el código, análisis exploratorio y visualizaciones.
- **reports/**: Reportes PDF o documentos generados (resúmenes ejecutivos, reportes técnicos).
- **visualizations/**: Gráficos estáticos (PNG/PDF) para reportes y presentaciones.

---

**© 2025 Equipo de Análisis Multivariado - ITESM**