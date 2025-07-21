from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score, 
    roc_auc_score, 
    classification_report,
    confusion_matrix
)
import numpy as np

def analisar_metricas_classificacao():
    print("=== Análise de Métricas de Classificação - Câncer de Mama ===\n")
    
    # Carregar dataset
    data = load_breast_cancer()
    X, y = data.data, data.target
    
    print(f"Dataset carregado:")
    print(f"- Número de amostras: {X.shape[0]}")
    print(f"- Número de características: {X.shape[1]}")
    print(f"- Classes: {data.target_names}")
    print(f"- Distribuição das classes: Maligno={np.sum(y==0)}, Benigno={np.sum(y==1)}\n")
    
    # Dividir dados em treino e teste (70% treino, 30% teste)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    print(f"Divisão dos dados:")
    print(f"- Treino: {X_train.shape[0]} amostras")
    print(f"- Teste: {X_test.shape[0]} amostras\n")
    
    # Treinar modelo Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    # Fazer predições
    y_pred = rf_model.predict(X_test)
    y_pred_proba = rf_model.predict_proba(X_test)[:, 1]
    
    # Calcular métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc_roc = roc_auc_score(y_test, y_pred_proba)
    
    # Exibir resultados
    print("=== MÉTRICAS DE CLASSIFICAÇÃO ===")
    print(f"Acurácia (Accuracy):     {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"Precisão (Precision):    {precision:.4f} ({precision*100:.2f}%)")
    print(f"Revocação (Recall):      {recall:.4f} ({recall*100:.2f}%)")
    print(f"F1-Score:                {f1:.4f} ({f1*100:.2f}%)")
    print(f"AUC-ROC:                 {auc_roc:.4f} ({auc_roc*100:.2f}%)")
    
    print(f"\n=== MATRIZ DE CONFUSÃO ===")
    cm = confusion_matrix(y_test, y_pred)
    print(f"Verdadeiros Negativos (TN): {cm[0,0]} - Maligno corretamente identificado")
    print(f"Falsos Positivos (FP):      {cm[0,1]} - Maligno classificado como Benigno")
    print(f"Falsos Negativos (FN):      {cm[1,0]} - Benigno classificado como Maligno")
    print(f"Verdadeiros Positivos (TP): {cm[1,1]} - Benigno corretamente identificado")
    
    print(f"\n=== RELATÓRIO DETALHADO ===")
    print(classification_report(y_test, y_pred, target_names=['Maligno', 'Benigno']))
    
    print(f"\n=== ANÁLISE DOS RESULTADOS ===")
    print(f"1. ACURÁCIA ({accuracy*100:.2f}%): Percentual de predições corretas no total")
    print(f"   - Excelente desempenho geral do modelo")
    
    print(f"\n2. PRECISÃO ({precision*100:.2f}%): Dos casos preditos como benignos, quantos realmente são?")
    if precision > 0.95:
        print(f"   - Muito alta! Baixo risco de falsos positivos")
    elif precision > 0.90:
        print(f"   - Alta! Boa confiabilidade nas predições positivas")
    else:
        print(f"   - Moderada. Cuidado com falsos positivos")
    
    print(f"\n3. RECALL/SENSIBILIDADE ({recall*100:.2f}%): Dos casos realmente benignos, quantos foram detectados?")
    if recall > 0.95:
        print(f"   - Muito alto! Baixo risco de não detectar casos benignos")
    elif recall > 0.90:
        print(f"   - Alto! Boa capacidade de detectar casos positivos")
    else:
        print(f"   - Moderado. Risco de falsos negativos")
    
    print(f"\n4. F1-SCORE ({f1*100:.2f}%): Média harmônica entre Precisão e Recall")
    if f1 > 0.95:
        print(f"   - Excelente equilíbrio entre precisão e recall")
    elif f1 > 0.90:
        print(f"   - Bom equilíbrio entre precisão e recall")
    else:
        print(f"   - Equilíbrio moderado")
    
    print(f"\n5. AUC-ROC ({auc_roc*100:.2f}%): Capacidade de distinguir entre as classes")
    if auc_roc > 0.95:
        print(f"   - Excelente capacidade discriminativa")
    elif auc_roc > 0.90:
        print(f"   - Boa capacidade discriminativa")
    else:
        print(f"   - Capacidade discriminativa moderada")
    
    print(f"\n=== CONCLUSÃO MÉDICA ===")
    print(f"Para diagnóstico de câncer de mama:")
    print(f"- Recall alto ({recall*100:.2f}%) é CRÍTICO: minimiza casos benignos não detectados")
    print(f"- Precisão alta ({precision*100:.2f}%) é IMPORTANTE: evita ansiedade desnecessária")
    print(f"- O modelo Random Forest apresentou desempenho excelente para este dataset")
    print(f"- Recomenda-se validação adicional antes do uso clínico")

if __name__ == "__main__":
    analisar_metricas_classificacao()
