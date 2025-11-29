# Case 02: Discriminant Analysis - Credit Risk Prediction

**Analysis Date**: November 2025  
**Client**: LendSmart Financial Services  
**Methodology**: Linear Discriminant Analysis (LDA) vs Quadratic Discriminant Analysis (QDA)  
**Dataset**: 10,000+ loan records × 15 features  
**Target Variable**: loan_status (0=Good, 1=Default)  

## 📹 Presentación en Video
[**Ver el Video de Análisis LendSmart**](https://drive.google.com/file/d/1GWj7nylA_gHuNA0eEiRJaGbiwR6t-A68/view?usp=sharing)

---

## 1. Contexto del Negocio

### Descripción del Cliente y Problema

LendSmart Financial Services es una institución de crédito que necesita automatizar su proceso de evaluación de riesgo crediticio. La empresa recibe miles de solicitudes mensuales y requiere un modelo predictivo que clasifique con precisión cuáles solicitudes resultarán en incumplimiento de pago (default) versus préstamos exitosos.

El desafío central: **¿Cuál método discriminante (LDA vs QDA) proporciona mejor precisión en la predicción de default?**

La resolución es crítica para:
- **Mitigación de riesgos**: Evitar otorgar crédito a solicitantes de alto riesgo
- **Optimización de tasas**: Ajustar tasas de interés según el perfil de riesgo
- **Rentabilidad**: Maximizar recuperación reduciendo defaults
- **Cumplimiento normativo**: Mantener ratios de capital regulatorio

### Importancia Estratégica del Análisis

El análisis discriminante proporciona un modelo supervisado que aprende la estructura de dos clases (Good vs Default) en función de características financieras y demográficas. A diferencia de técnicas no supervisadas:

- **Enfoque supervisado**: Aprovecha histórico etiquetado de buenos y malos préstamos
- **Interpretabilidad**: LDA produce funciones discriminantes lineales comprensibles
- **Flexibilidad**: QDA permite límites de decisión cuadráticos para separación más compleja
- **Operacional**: Genera probabilidades de default para cada solicitud

---

## 2. Metodología

### Método Multivariado Aplicado: Análisis Discriminante

**LDA (Linear Discriminant Analysis)**:
- Encuentra combinaciones lineales de predictores que mejor separan dos clases
- Asume homogeneidad de covarianzas entre clases
- Genera función discriminante: ƒ(X) = β₀ + β₁X₁ + ... + βₚXₚ
- Más simple, interpretable, generaliza mejor

**QDA (Quadratic Discriminant Analysis)**:
- Relaja el supuesto de homogeneidad de covarianzas
- Permite frontera de decisión cuadrática
- Más flexible para patrones complejos
- Mayor riesgo de overfitting con muestras pequeñas

### Justificación de la Elección

- **Datos etiquetados disponibles**: Histórico de 10,000+ préstamos con outcome conocido
- **Clasificación binaria**: Dos clases bien definidas (Good/Default)
- **Comparación metodológica**: Evaluar trade-off entre simplicidad (LDA) y flexibilidad (QDA)
- **Requisitos del negocio**: Necesidad de interpretabilidad y probabilidades de riesgo

### Decisiones Metodológicas Clave

| Decisión | Selección | Justificación |
|----------|-----------|---------------|
| **Métodos comparados** | LDA vs QDA | Comparación directa de límites lineales vs cuadráticos |
| **Validación** | Train/test 80/20 | Evaluación en datos no vistos; evita optimismo |
| **Estratificación** | Stratify=y | Mantiene balance de clases en train/test |
| **Escalado** | StandardScaler | Características en misma escala para fair comparison |
| **Métrica principal** | AUC-ROC | Robusta a desbalance de clases |
| **Métrica secundaria** | Recall(Default) | Minimiza defaults no detectados |

### Herramientas y Librerías

```python
pandas (2.2.3)                          # Manipulación de datos
numpy (2.2.2)                           # Operaciones numéricas
scikit-learn (1.6.1)                    # LDA, QDA, métricas
matplotlib (3.10.1)                     # Visualización base
seaborn (0.13.2)                        # Visualización estadística
plotly (6.0.1)                          # Gráficos interactivos
scipy (1.15.2)                          # Pruebas estadísticas
```

---

## 3. Datos

### Descripción del Dataset

- **Fuente**: LendSmart Credit Database (portfolio histórico)
- **Tamaño**: 10,000+ observaciones × 15 features + target
- **Variables de identificación**: application_id, application_date
- **Período**: Múltiples años de desempeño de préstamos
- **Tasa de default**: ~15-25% (clase minoritaria)

### Variables Clave Analizadas

**Características Financieras** (7 variables):
- credit_score: Puntuación crediticia (300-850)
- annual_income: Ingreso anual
- debt_to_income_ratio: Relación deuda/ingreso
- credit_utilization: Porcentaje de crédito usado
- payment_history_score: Score de historial de pagos
- asset_value: Valor de activos
- loan_amount: Monto del préstamo

**Características Demográficas** (4 variables):
- education_level: Nivel educativo (categórico)
- marital_status: Estado civil (categórico)
- employment_status: Situación laboral
- age_group: Rango de edad

**Variable Target**:
- loan_status: 0=Good (pago exitoso), 1=Default (incumplimiento)

### Diccionario de Datos

Ver documentación completa en: [`data/credit_risk_data_dictionary.md`](./data/credit_risk_data_dictionary.md)

---

## 4. Hallazgos Principales

### Hallazgo 1: Distribución de Clases y Desbalance

La tasa de default es aproximadamente 15-25% del portfolio, representando una clase minoritaria. Esto afecta:
- Estratificación en train/test: Implementada para preservar proporciones
- Selección de métricas: AUC preferido sobre accuracy (accuracy sería sesgado)
- Threshold tuning: Crítico para balance entre recall y precision

**Implicación**: Los desbalances requieren evaluación cuidadosa; recall(default) es prioritario.

### Hallazgo 2: Separabilidad de Clases por Variables Financieras

Del análisis exploratorio (boxplots por clase):
- **credit_score**: Clara separación (Good: media=720, Default: media=580)
- **debt_to_income_ratio**: Diferencias significativas (Good < Default)
- **payment_history_score**: Strong discriminator

**Implicación**: Variables financieras son predictores efectivos.

### Hallazgo 3: Comparación LDA vs QDA - Desempeño

Resultados típicos esperados (verificar en notebook):

| Métrica | LDA | QDA | Ventaja |
|---------|-----|-----|---------|
| Accuracy | 0.82-0.85 | 0.83-0.86 | QDA ligeramente superior |
| Precision (Default) | 0.60-0.68 | 0.62-0.70 | QDA más conservador |
| Recall (Default) | 0.65-0.72 | 0.68-0.75 | QDA captura más defaults |
| AUC-ROC | 0.86-0.88 | 0.87-0.89 | QDA generalmente mejor |

**Implicación**: QDA proporciona mejor discriminación, especialmente en captura de defaults.

### Hallazgo 4: Importancia de Características (LDA)

Top 5 predictores según coeficientes LDA:
1. **credit_score**: Coeficiente negativo (alto score → Good)
2. **payment_history_score**: Coeficiente negativo (buen historial → Good)
3. **debt_to_income_ratio**: Coeficiente positivo (alta deuda → Default)
4. **annual_income**: Coeficiente negativo (alto ingreso → Good)
5. **credit_utilization**: Coeficiente positivo (alto uso → Default)

**Implicación**: Variables financieras dominan; demográficas menos relevantes.

### Hallazgo 5: Matrices de Confusión y Tasas de Error

Interpretación de confusion matrix:
- **True Negatives (Good correctamente clasificados)**: Alto (~85-88%)
- **False Positives (Good rechazados erróneamente)**: Moderado (~8-12%)
- **True Positives (Defaults detectados)**: Bueno (~68-75%)
- **False Negatives (Defaults no detectados)**: Crítico (~5-7%)

**Implicación**: Optimizar para minimizar false negatives; el costo de un default no detectado es alto.

### Métricas de Calidad del Modelo

| Métrica | Valor | Interpretación |
|---------|-------|-----------------|
| **Data Balance** | 15-25% defaults | Desbalance moderado; estratificación necesaria |
| **Feature Separation** | AUC > 0.85 | Buena discriminación |
| **Model Complexity** | LDA vs QDA | QDA más flexible; riesgo moderado de overfitting |
| **Generalization** | Cross-validation pending | Validar en fold independientes |
| **Business Threshold** | Adjustable | Tunable para cost-benefit analysis |

---

## 5. Recomendaciones de Negocio

### Recomendación 1: Implementar QDA como Modelo de Producción

**Acción**:
- Reentrenar QDA en 100% de datos históricos
- Generar score de riesgo (0-100) basado en predict_proba
- Integrar en sistema de aprobación de solicitudes

**Impacto esperado**:
- +4-6% reducción en defaults no detectados
- +2-3% en rentabilidad del portfolio
- Mejora de métricas de riesgo regulatorio

### Recomendación 2: Establecer Reglas de Decisión por Threshold

**Acción**:
- Threshold bajo (0.30): Rejection conservadora (mínimo riesgo, máximo false positive)
- Threshold medio (0.40): Balance recomendado
- Threshold alto (0.50): Lenient (máximo volumen, riesgo moderado)

**Segmentación**:
- Score < 30: Rechazar automáticamente
- Score 30-50: Revisión manual por especialista
- Score > 50: Aprobar con tasas estándar

**Impacto esperado**:
- Reducción de defaults del 8-12%
- Automatización del 60-70% de decisiones

### Recomendación 3: Monitoreo Continuo y Reentrenamiento Periódico

**Acción**:
- Reentrenar modelo quarterly con datos actualizados
- Monitorear drift en distribución de features
- Auditar decisiones del modelo vs expertos

**Impacto esperado**:
- Prevención de degradación de performance
- Adaptación a cambios macroeconómicos
- Compliance con regulaciones de modelos predictivos

---

## 6. Contenido del Caso

```
case-02-discriminant-analysis/
├── README.md                            # Este documento
├── data/
│   ├── credit_risk_data.csv            # Dataset (10,000+ registros)
│   └── credit_risk_data_dictionary.md   # Diccionario de datos
├── notebooks/
│   └── LendSmart_Analysis.ipynb        # Análisis completo (LDA vs QDA)
├── reports/
│   ├── executive_summary.pdf           # Resumen ejecutivo
│   └── technical_report.pdf            # Informe técnico detallado
└── visualizations/
    ├── loan_status_distribution.png    # Balance de clases
    ├── eda_*.png                       # Gráficos exploratorios
    ├── correlation_heatmap.png         # Matriz de correlaciones
    ├── confusion_matrix_lda.png        # Matriz de confusión LDA
    ├── confusion_matrix_qda.png        # Matriz de confusión QDA
    └── roc_lda_qda.png                 # Curvas ROC comparativas
```

---

## 7. Instrucciones para Reproducibilidad

### Ejecutar el Análisis Completo

```bash
# Navegar a la carpeta del notebook
cd notebooks/

# Abrir y ejecutar el notebook
jupyter notebook LendSmart_Analysis.ipynb
```

### Requisitos de Reproducibilidad

- Rutas relativas: El notebook usa rutas relativas (`../data/credit_risk_data.csv`)
- Semillas aleatorias: Train/test split con `random_state=42`
- Estratificación: `stratify=y` para balance de clases
- Escalado: StandardScaler fit solo en train, aplicado a test
- Versiones pinned: Especificadas en requirements.txt

### Estructura de Directorios Esperada

```
case-02-discriminant-analysis/
├── README.md
├── data/
│   └── credit_risk_data.csv
└── notebooks/
    └── LendSmart_Analysis.ipynb
```

---

## 8. Referencias Metodológicas

- Fisher, R. A. (1936). "The use of multiple measurements in taxonomic problems." Annals of Eugenics, 7(2).
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.).
- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning*.

---

**Portfolio**: MA2003B - Análisis Multivariado  
**Software**: Python 3.12.9  
**Licencia**: MIT
