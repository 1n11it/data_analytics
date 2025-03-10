import joblib
import numpy as np
import warnings

# Suppress sklearn UserWarnings
warnings.filterwarnings("ignore", category=UserWarning)

# Load the trained model
dtree = joblib.load('bike_price_model.pkl')

# Load the scaler if used
scaler = joblib.load('scaler.pkl')  # Uncomment if you used scaling

def get_user_input():
    """Collect user input for bike details."""
    try:      
        year = int(input("📅 Enter Bike Year (e.g., 2018): "))
        km_driven = float(input("🚗 Enter Kilometers Driven: "))
        power = float(input("⚙️ Enter Engine Power (HP): "))
        brand_encoded = int(input("🏍️ Enter Brand Code (e.g., 1 for Honda, 2 for Yamaha): "))
        fuel_encoded = int(input("⛽ Enter Fuel Type Code (0 for Petrol, 1 for Diesel): "))
        owner = int(input("👤 Enter Owner Type (1 for first owner, 2 for second owner, etc.): "))
        
        return np.array([[year, km_driven, power, brand_encoded, fuel_encoded, owner]])
    
    except ValueError:
        print("\n❌ Invalid input! Please enter correct numerical values.")
        return get_user_input()  # Retry input

def predict_price():
    """Predict bike price based on user input."""
    user_input = get_user_input()
    
    # Apply scaling if a scaler is available
    if scaler:
        user_input = scaler.transform(user_input)

    # Make prediction
    predicted_price = dtree.predict(user_input)
    
    # Display result in a formatted way
    print(f"\n💰 Estimated Resale Price: ₹{predicted_price[0]:,.3f}")

if __name__ == "__main__":
    print("\n🔹 Used Bike Price Prediction 🔹\n")
    predict_price()
    print("\n👋 Thank you for using our service!" )


# bike_code = {
#     0: 'Bajaj',
#     1: 'Hero',  2: 'Honda',  3: 'KTM',  4: 'Benelli',  5: 'Royal Enfield',  6: 'Suzuki',  7: 'TVS', 8: 'Yamaha',
#     9: 'Ducati, Harley-Davidson, Hyosung, Triumph, BMW, Kawasaki, Mahindra, Jawa'
# }

