import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

api_key = "-"

st.title("OpenWeatherMap App")

city_name = st.text_input("Enter your city name:")

if city_name:

    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    try:
        res = requests.get(api_url)

        if res.status_code == 200:
            print(f"Request is accepted : {res.status_code}")
            data = res.json()

            temp = round(data["main"]["temp"] - 273.15, 2)
            humidity = data["main"]["humidity"]
            visibility = data.get("visibility", 0)
            wind = data["wind"]["speed"]
            
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Weather Details")
                st.write(f"*City:* {city_name}")
                st.write(f"*Temperature:* {temp} °C")
                st.write(f"*Humidity:* {humidity}%")
                st.write(f"*Visibility:* {visibility} metres")
                st.write(f"*Wind Speed:* {wind} m/s")

            with col2:
                st.subheader("Visibility Plot")

                
                df = pd.DataFrame({
                    "Index": [1],
                    "Visibility": [visibility]
                })

                plt.figure(figsize=(5,3))
                plt.plot(df["Index"], df["Visibility"], marker='o')
                plt.title(f"Visibility in {city_name}")
                plt.xlabel("Index")
                plt.ylabel("Visibility (m)")

                st.pyplot(plt)

        else:
            st.error("Invalid city name or request failed.")

    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
