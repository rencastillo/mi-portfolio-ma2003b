# Case 01: Factor Analysis - Customer Satisfaction Dimensions

**Analysis Date**: November 2025  
**Client**: TechnoServe Solutions  
**Methodology**: Principal Axis Factoring with Varimax Rotation  
**Dataset**: 3,400 customer responses × 23 satisfaction variables  

---

## 1. Contexto del Negocio

### Descripción del Cliente y Problema

TechnoServe Solutions es una firma de consultoría tecnológica que recopila datos exhaustivos de satisfacción del cliente a través de 23 dimensiones de servicio diferentes. La empresa enfrentaba una pregunta fundamental: **¿la satisfacción del cliente es un constructo unidimensional o multidimensional?**

La resolución de esta pregunta es crítica para:
- **Asignación de recursos**: Identificar dónde invertir para máximo impacto
- **Medición de desempeño**: Establecer métricas y KPIs relevantes
- **Estrategia competitiva**: Diferenciarse en dimensiones clave

### Importancia Estratégica del Análisis

El análisis factorial reduce la complejidad de 23 variables correlacionadas a un conjunto más pequeño de factores subyacentes, revelando la estructura latente de la satisfacción del cliente. Esto permite:

- **Simplificación operacional**: De 23 métricas a dimensiones estratégicas clave
- **Validación empírica**: Confirmar que las teorías del servicio reflejan la realidad del cliente
- **Predicción de resultados**: Usar factores para predecir renovaciones, recomendaciones y crecimiento

---

## 2. Metodología

### Método Multivariado Aplicado: Análisis Factorial

**Definición**: El análisis factorial es una técnica de reducción dimensional que identifica factores comunes latentes explicando la varianza en un conjunto de variables observadas.

**Justificación de la elección**:
- Las 23 variables de satisfacción están altamente correlacionadas (rango: 0.32 a 0.89)
- Se necesita reducir dimensionalidad sin perder información crítica
- El objetivo es identificar constructos teóricos subyacentes
- La técnica es robusta para validación de escalas multidimensionales

### Decisiones Metodológicas Clave

| Decisión | Selección | Justificación |
|----------|-----------|---------------|
| **Método de extracción** | Principal Axis Factoring | Más robusta que componentes principales |
| **Rotación** | Varimax (ortogonal) | Maximiza simplicidad interpretable |
| **Número de factores** | 5 factores | Kaiser criterion (λ > 1) + scree plot |
| **Estandarización** | Z-score | Variables en misma escala |

### Herramientas y Librerías

```python
pandas (2.2.3)          # Manipulación de datos
numpy (2.2.2)           # Operaciones numéricas
scikit-learn (1.6.1)    # Modelado predictivo
factor-analyzer (0.5.1) # Análisis factorial
matplotlib (3.10.1)     # Visualización base
seaborn (0.13.2)        # Visualización estadística
scipy (1.15.2)          # Pruebas estadísticas
```

---

## 3. Datos

### Descripción del Dataset

- **Fuente**: Survey de satisfacción del cliente TechnoServe Solutions (Q1-Q4 2024)
- **Tamaño**: 3,400 observaciones × 23 variables de satisfacción
- **Escala**: Likert 1-7 (1=Muy insatisfecho, 7=Muy satisfecho)
- **Tasa de respuesta**: 78% (industry benchmark: 45%)

### Variables Clave Analizadas

Las 23 variables se organizan en **5 dimensiones teóricas**:

1. **Excelencia Técnica** (5 variables)
   - technical_expertise, problem_solving, innovation_solutions, technical_documentation, system_integration

2. **Gestión de Proyectos** (5 variables)
   - project_management, timeline_adherence, budget_control, quality_deliverables, change_management

3. **Gestión de Relaciones** (5 variables)
   - account_manager_responsive, executive_access, trust_reliability, long_term_partnership, communication_clarity

4. **Valor y Costos** (4 variables)
   - cost_transparency, value_for_money, roi_demonstration, competitive_pricing

5. **Soporte y Servicios** (4 variables)
   - support_responsiveness, training_quality, documentation_help, billing_accuracy

### Diccionario de Datos

Ver documentación completa en: [`data/customer_satisfaction_data_dictionary.md`](./data/customer_satisfaction_data_dictionary.md)

---

## 4. Hallazgos Principales

### Hallazgo 1: Estructura Factorial de 5 Dimensiones Confirmada

La satisfacción del cliente es **multidimensional**, comprendida por **5 factores independientes** que explican el **73.2% de la varianza total**:

- Factor 1 (Excelencia Técnica): 18.4%
- Factor 2 (Gestión de Proyectos): 15.7%
- Factor 3 (Gestión de Relaciones): 14.2%
- Factor 4 (Valor y Costos): 13.1%
- Factor 5 (Soporte y Servicios): 11.8%

**Implicación**: No existe un único "conductor" de satisfacción. Emerge del equilibrio en múltiples dimensiones.

### Hallazgo 2: Comunalidades Altas (h² > 0.60 en 96% de variables)

22 de 23 variables tienen comunalidades superiores a 0.60:
- technical_expertise (h² = 0.78)
- project_management (h² = 0.76)
- trust_reliability (h² = 0.74)

**Implicación**: El modelo es parsimonioso y válido.

### Hallazgo 3: Factores Correlacionados (Correlaciones significativas)

Análisis oblicuo revela correlaciones entre factores:
- Excelencia Técnica ↔ Gestión de Proyectos (r = 0.63)
- Excelencia Técnica ↔ Gestión de Relaciones (r = 0.49)

**Implicación**: Existe sinergia operacional entre dimensiones.

### Hallazgo 4: Poder Predictivo Validado

Los factores predicen efectivamente resultados empresariales:

| Resultado | R² | Validez |
|-----------|-----|---------|
| Overall Satisfaction | 0.600 | Excelente |
| Revenue Growth | 0.589 | Excelente |
| Renewal Likelihood | 0.385 | Bueno |
| NPS Score | 0.276 | Moderado |
| Referrals | 0.245 | Moderado |

### Hallazgo 5: Jerarquía de Impacto de Factores

Ranking de importancia en predicción de resultados:

1. **Gestión de Proyectos** (importancia: 0.336)
2. **Excelencia Técnica** (importancia: 0.327)
3. **Gestión de Relaciones** (importancia: 0.327)
4. **Valor y Costos** (importancia: 0.250)
5. **Soporte y Servicios** (importancia: 0.207)

### Métricas de Calidad del Modelo

| Métrica | Valor | Estado |
|---------|-------|--------|
| **KMO Global** | 0.871 | Excelente |
| **Test Bartlett** | p < 0.001 | Significativo |
| **Varianza Total** | 73.2% | Buena |
| **Estabilidad CV** | 0.947 | Muy estable |
| **Cronbach Alpha** | 0.88-0.92 | Confiable |

---

## 5. Recomendaciones de Negocio

### Recomendación 1: Centro de Excelencia en Gestión de Proyectos

**Acción**:
- Crear equipo dedicado de mejora de procesos PM
- Implementar metodología estándar (Agile/Hybrid)
- Invertir en herramientas de seguimiento

**Impacto esperado**:
- +15-20% en tasa de renovación
- +25% en recomendaciones de clientes
- ROI: 3-5x en 12 meses

### Recomendación 2: Invertir en Actualización de Arquitectos Técnicos

**Acción**:
- Programa de certificación para arquitectos
- Laboratorios de innovación internos (R&D)
- Partnerships de investigación

**Impacto esperado**:
- +18% en crecimiento de ingresos
- +12% en actividades de up-sell
- ROI: 2.5-3x en 18 meses

### Recomendación 3: Reforzar Gestión de Relaciones Ejecutivas

**Acción**:
- Asignar ejecutivos dedicados a cuentas TOP
- Revisiones trimestrales de negocio
- Modelo de relación multi-nivel

**Impacto esperado**:
- +22% en tasa de renovación
- +30% en satisfacción enterprise
- ROI: 4-6x en 12-18 meses

---

## 6. Contenido del Caso

```
case-01-factor-analysis/
├── README.md                                    # Este documento
├── data/
│   ├── customer_satisfaction_data.csv          # Dataset (3,400 × 23)
│   └── customer_satisfaction_data_dictionary.md # Diccionario de datos
├── notebooks/
│   └── Costumer_service.ipynb                  # Análisis completo
├── reports/
│   ├── executive_summary.pdf                   # Resumen ejecutivo
│   └── technical_report.pdf                    # Informe técnico
└── visualizations/
    ├── correlation_heatmap.png                 # Matriz de correlaciones
    ├── factor_loadings.png                     # Cargas factoriales
    ├── scree_plot.png                          # Criterio Kaiser
    └── factor_scores_distribution.png          # Distribución de scores
```

---

## 7. Instrucciones para Reproducibilidad

### Ejecutar el Análisis Completo

```bash
# Navegar a la carpeta del notebook
cd notebooks/

# Abrir y ejecutar el notebook
jupyter notebook Costumer_service.ipynb
```

### Requisitos de Reproducibilidad

- Rutas relativas: El notebook usa rutas relativas (`../data/customer_satisfaction_data.csv`)
- Semillas aleatorias: Todos los modelos usan `random_state=42`
- Versiones pinned: Requirements.txt especifica versiones exactas
- Dataset incluido: El CSV está en `data/` para uso local

### Estructura de Directorios Esperada

```
case-01-factor-analysis/
├── README.md
├── data/
│   └── customer_satisfaction_data.csv
└── notebooks/
    └── Costumer_service.ipynb
```

---

## 8. Referencias Metodológicas

- Fabrigar, L. R., & Wegener, D. T. (2011). *Exploratory factor analysis*. Oxford University Press.
- Hair, J. F., et al. (2010). *Multivariate data analysis* (7th ed.).
- Kaiser, H. F. (1974). An index of factorial simplicity. *Psychometrika*, 39(1), 31-36.

---

**Portfolio**: MA2003B - Análisis Multivariado  
**Software**: Python 3.12.9  
**Licencia**: MIT
