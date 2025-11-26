"""
Utilidades para el análisis factorial.

Este módulo contiene funciones auxiliares para el procesamiento
y análisis de datos en el caso de estudio de análisis factorial.
"""

import numpy as np
import pandas as pd
from typing import Tuple, Optional


def load_data(filepath: str) -> pd.DataFrame:
    """
    Carga los datos desde un archivo CSV.
    
    Args:
        filepath: Ruta al archivo CSV.
        
    Returns:
        DataFrame con los datos cargados.
    """
    return pd.read_csv(filepath)


def calculate_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula la matriz de correlación para las variables numéricas.
    
    Args:
        df: DataFrame con los datos.
        
    Returns:
        Matriz de correlación.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    return df[numeric_cols].corr()


def check_kmo_adequacy(correlation_matrix: pd.DataFrame) -> Tuple[float, str]:
    """
    Verifica la adecuación de los datos para análisis factorial
    usando la medida KMO (Kaiser-Meyer-Olkin).
    
    Args:
        correlation_matrix: Matriz de correlación.
        
    Returns:
        Tuple con el valor KMO y su interpretación.
        
    Raises:
        NotImplementedError: Esta función es un placeholder.
    
    Example:
        Para implementar, usar factor_analyzer:
        >>> from factor_analyzer.factor_analyzer import calculate_kmo
        >>> kmo_all, kmo_model = calculate_kmo(df)
    """
    raise NotImplementedError(
        "Esta función es un placeholder. Implementar usando factor_analyzer: "
        "from factor_analyzer.factor_analyzer import calculate_kmo"
    )


def standardize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Estandariza las variables numéricas (z-score).
    
    Args:
        df: DataFrame con los datos.
        
    Returns:
        DataFrame con datos estandarizados.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df_standardized = df.copy()
    df_standardized[numeric_cols] = (
        (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()
    )
    return df_standardized
