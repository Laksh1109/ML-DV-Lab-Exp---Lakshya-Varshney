# Exp 04: Ridge and Lasso Regularization
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

data = load_diabetes()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = [("Ridge", make_pipeline(StandardScaler(), Ridge(alpha=1))),
          ("Lasso", make_pipeline(StandardScaler(), Lasso(alpha=0.1)))]
for name, model in models:
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(name, "MSE:", mean_squared_error(y_test, pred), "R2:", r2_score(y_test, pred))
