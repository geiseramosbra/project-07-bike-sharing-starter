from sklearn.metrics import mean_squared_error, r2_score

def regression_metrics(y_true, y_pred):
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    r2 = r2_score(y_true, y_pred)
    return {'rmse': float(rmse), 'r2': float(r2)}