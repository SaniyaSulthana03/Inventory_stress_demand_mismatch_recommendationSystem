# # import streamlit as st
# # import pandas as pd
# # import joblib

# # # Load trained model
# # model = joblib.load("rf_inventory_stress_model.pkl")

# # st.title("Inventory Stress & Demand Mismatch Early Warning System")

# # st.write(
# #     "Predicts inventory stress to detect stockout or overstock risks using regression modeling."
# # )


# st.sidebar.header("SKU Input Parameters")

# Inventory_Level = st.sidebar.number_input("Inventory Level", min_value=0, value=100)
# Units_Ordered = st.sidebar.number_input("Units Ordered", min_value=0, value=50)
# Price = st.sidebar.number_input("Price", value=20.0)
# Discount = st.sidebar.number_input("Discount (%)", min_value=0, max_value=100, value=0)
# Promotion = st.sidebar.selectbox("Promotion", [0, 1])
# Epidemic = st.sidebar.selectbox("Epedemic",[0,1])
# Price_Gap = st.sidebar.number_input("Price Gap vs Competitor", value=0.0)
# Seasonality = st.sidebar.selectbox(
#     "Seasonality", ["Winter", "Spring", "Summer", "Autumn"]
# )
# Category = st.sidebar.selectbox(
#     "Category", ["Electronics", "Clothing", "Groceries", "Furniture", "Toys"]
# )
# Region = st.sidebar.selectbox("Region", ["North", "South", "East", "West"])
# Weather_Condition = st.sidebar.selectbox(
#     "Weather Condition", ["Sunny", "Rainy", "Snowy", "Cloudy"]
# )

# input_df = pd.DataFrame({
#     "Inventory_Level": [Inventory_Level],
#     "Units_Ordered": [Units_Ordered],
#     "Price": [Price],
#     "Discount": [Discount],
#     "Promotion": [Promotion],
#     "Price_Gap": [Price_Gap],
#     "Seasonality": [Seasonality],
#     "Category": [Category],
#     "Region": [Region],
#     "Weather_Condition": [Weather_Condition],
#     "Epidemic": [Epidemic]

# X_input_processed = preprocessor.transform(input_df)
# prediction = model.predict(X_input_processed)

# # })

# # prediction = model.predict(input_df)[0]

# if prediction <= 0:
#     risk = "Overstocked"
# elif prediction <= 20:
#     risk = "Safe"
# elif prediction <= 50:
#     risk = "Moderate Risk"
# else:
#     risk = "High Risk"

# st.subheader("Predicted Inventory Stress Score")
# st.metric("Inventory Stress", round(prediction, 2))

# st.subheader("Risk Category")
# if risk == "High Risk":
#     st.error(risk)
# else:
#     st.success(risk)


# import streamlit as st
# import pandas as pd
# import joblib
# from xgboost import XGBRegressor

# # ---------------------------
# # Load preprocessor & model
# # ---------------------------
# @st.cache_resource
# def load_artifacts():
#     preprocessor = joblib.load("preprocessor.pkl")
#     model = XGBRegressor()
#     model.load_model("xgb_model.json")
#     return preprocessor, model

# preprocessor, model = load_artifacts()

# # ---------------------------
# # App UI
# # ---------------------------
# st.title("Inventory Stress & Demand Mismatch Early Warning System")
# st.write(
#     "This application predicts inventory stress to identify overstock or stockout risks."
# )

# st.sidebar.header("SKU Input Parameters")

# Inventory_Level = st.sidebar.number_input("Inventory Level", min_value=0, value=100)
# Units_Ordered = st.sidebar.number_input("Units Ordered", min_value=0, value=50)
# Price = st.sidebar.number_input("Price", value=20.0)
# Discount = st.sidebar.number_input("Discount (%)", min_value=0, max_value=100, value=0)
# Promotion = st.sidebar.selectbox("Promotion", [0, 1])
# Epidemic = st.sidebar.selectbox("Epidemic", [0, 1])
# Price_Gap = st.sidebar.number_input("Price Gap vs Competitor", value=0.0)

# Seasonality = st.sidebar.selectbox(
#     "Seasonality", ["Winter", "Spring", "Summer", "Autumn"]
# )
# Category = st.sidebar.selectbox(
#     "Category", ["Electronics", "Clothing", "Groceries", "Furniture", "Toys"]
# )
# Region = st.sidebar.selectbox("Region", ["North", "South", "East", "West"])
# Weather_Condition = st.sidebar.selectbox(
#     "Weather Condition", ["Sunny", "Rainy", "Snowy", "Cloudy"]
# )

# # ---------------------------
# # Create input DataFrame
# # ---------------------------
# input_df = pd.DataFrame({
#     "Inventory_Level": [Inventory_Level],
#     "Units_Ordered": [Units_Ordered],
#     "Price": [Price],
#     "Discount": [Discount],
#     "Promotion": [Promotion],
#     "Price_Gap": [Price_Gap],
#     "Seasonality": [Seasonality],
#     "Category": [Category],
#     "Region": [Region],
#     "Weather_Condition": [Weather_Condition],
#     "Epidemic": [Epidemic]
# })

# # ---------------------------
# # Prediction
# # ---------------------------
# X_input_processed = preprocessor.transform(input_df)
# prediction = model.predict(X_input_processed)[0]

# # ---------------------------
# # Risk logic
# # ---------------------------
# if prediction <= 0:
#     risk = "Overstocked"
# elif prediction <= 20:
#     risk = "Safe"
# elif prediction <= 50:
#     risk = "Moderate Risk"
# else:
#     risk = "High Risk"

# # ---------------------------
# # Output
# # ---------------------------
# st.subheader("Predicted Inventory Stress Score")
# st.metric("Inventory Stress", round(prediction, 2))

# st.subheader("Risk Category")
# if risk == "High Risk":
#     st.error(risk)
# elif risk == "Moderate Risk":
#     st.warning(risk)
# else:
#     st.success(risk)

import streamlit as st
import pandas as pd
import joblib
from xgboost import XGBRegressor

st.set_page_config(page_title="Inventory Stress Predictor")

# ---------------------------
# Load artifacts
# ---------------------------
@st.cache_resource
def load_artifacts():
    preprocessor = joblib.load("preprocessor.pkl")
    model = XGBRegressor()
    model.load_model("xgb_model.json")
    return preprocessor, model

preprocessor, model = load_artifacts()

# ---------------------------
# UI
# ---------------------------
st.title("Inventory Stress & Demand Mismatch Early Warning System")

st.sidebar.header("SKU Input Parameters")

Inventory_Level = st.sidebar.number_input("Inventory Level", min_value=0, value=100)
Units_Ordered = st.sidebar.number_input("Units Ordered", min_value=0, value=50)
Price = st.sidebar.number_input("Price", value=20.0)
Discount = st.sidebar.number_input("Discount (%)", 0, 100, 0)
Promotion = st.sidebar.selectbox("Promotion", [0, 1])
Epidemic = st.sidebar.selectbox("Epidemic", [0, 1])
Price_Gap = st.sidebar.number_input("Price Gap vs Competitor", value=0.0)

Seasonality = st.sidebar.selectbox(
    "Seasonality", ["Winter", "Spring", "Summer", "Autumn"]
)
Category = st.sidebar.selectbox(
    "Category", ["Electronics", "Clothing", "Groceries", "Furniture", "Toys"]
)
Region = st.sidebar.selectbox("Region", ["North", "South", "East", "West"])
Weather_Condition = st.sidebar.selectbox(
    "Weather Condition", ["Sunny", "Rainy", "Snowy", "Cloudy"]
)

# ---------------------------
# Input DataFrame (DO NOT TOUCH)
# ---------------------------
input_df = pd.DataFrame(
    [[
        Inventory_Level,
        Units_Ordered,
        Price,
        Discount,
        Promotion,
        Price_Gap,
        Seasonality,
        Category,
        Region,
        Weather_Condition,
        Epidemic
    ]],
    columns=[
        "Inventory_Level",
        "Units_Ordered",
        "Price",
        "Discount",
        "Promotion",
        "Price_Gap",
        "Seasonality",
        "Category",
        "Region",
        "Weather_Condition",
        "Epidemic"
    ]
)

# ---------------------------
# Prediction
# ---------------------------
X_input_processed = preprocessor.transform(input_df)
prediction = model.predict(X_input_processed)[0]

# ---------------------------
# Risk logic
# ---------------------------
if prediction <= 0:
    risk = "Overstocked"
elif prediction <= 20:
    risk = "Safe"
