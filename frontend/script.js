
let temperatureChart = null;



let humidityChart = null;



const API_URL = "http://127.0.0.1:8000/api/sensors";


function updateConnectionStatus(status) {

    const indicator = document.getElementById("connectionIndicator");

    const statusText = document.getElementById("connectionStatus");

    indicator.className = "connection";

    indicator.classList.add(status.toLowerCase());

    statusText.textContent = status;

}



async function fetchSensorData() {

    try {

        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Failed to fetch sensor data");
        }

        const data = await response.json();

        // Update temperature
        document.getElementById("temperature").textContent =
            Number(data.temperature).toFixed(2);

        // Update humidity
        document.getElementById("humidity").textContent =
            Number(data.humidity).toFixed(2);

        // Update connection status
        document.getElementById("connectionStatus").textContent =
            "Connected";

        // Update timestamp
        document.getElementById("lastUpdated").textContent =
            new Date(data.timestamp).toLocaleString();

    } catch (error) {

        console.error("Dashboard Error:", error);

        document.getElementById("connectionStatus").textContent =
            "Disconnected";

        throw error;

    }
}
fetchSensorData();


async function fetchHistoricalData() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/api/history"
        );

        if (!response.ok) {
            throw new Error("Failed to fetch historical data");
        }

        const result = await response.json();

        const history = result.history;

        const labels = history.map(item =>
            new Date(item.timestamp).toLocaleTimeString()
        );

        const temperatures = history.map(item =>
            Number(item.temperature)
        );

        const humidities = history.map(item =>
            Number(item.humidity)
        );

        createTemperatureChart(labels, temperatures);
        createHumidityChart(labels, humidities);

    } catch (error) {

        console.error("History Error:", error);
        throw error;

    }
}



function createTemperatureChart(labels, temperatures) {

    const ctx = document.getElementById("temperatureChart");

    if (temperatureChart) {
        temperatureChart.destroy();
    }

    temperatureChart = new Chart(ctx, {

        type: "line",

        data: {
            labels: labels,

            datasets: [{
                label: "Temperature (°C)",
                data: temperatures,
                borderColor: "#3b82f6",
                backgroundColor: "rgba(59, 130, 246, 0.15)",
                fill: true,
                tension: 0.4
            }]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            plugins: {
                legend: {
                    labels: {
                        color: "#e2e8f0"
                    }
                }
            },

            scales: {
                x: {
                    ticks: {
                        color: "#94a3b8"
                    },
                    grid: {
                        color: "#263449"
                    }
                },

                y: {
                    ticks: {
                        color: "#94a3b8"
                    },
                    grid: {
                        color: "#263449"
                    }
                }
            }
        }

    });

}


function createHumidityChart(labels, humidities) {

    const ctx = document.getElementById("humidityChart");

    if (humidityChart) {
        humidityChart.destroy();
    }

    humidityChart = new Chart(ctx, {

        type: "line",

        data: {
            labels: labels,

            datasets: [{
                label: "Humidity (%)",
                data: humidities,
                borderColor: "#22c55e",
                backgroundColor: "rgba(34, 197, 94, 0.15)",
                fill: true,
                tension: 0.4
            }]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            plugins: {
                legend: {
                    labels: {
                        color: "#e2e8f0"
                    }
                }
            },

            scales: {
                x: {
                    ticks: {
                        color: "#94a3b8"
                    },
                    grid: {
                        color: "#263449"
                    }
                },

                y: {
                    ticks: {
                        color: "#94a3b8"
                    },
                    grid: {
                        color: "#263449"
                    }
                }
            }
        }

    });

}


async function fetchAnalytics() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/api/analytics"
        );

        if (!response.ok) {
            throw new Error("Failed to fetch analytics");
        }

        const data = await response.json();

        document.getElementById("avgTemperature").textContent =
            data.average_temperature.toFixed(2) + " °C";

        document.getElementById("maxTemperature").textContent =
            data.maximum_temperature.toFixed(2) + " °C";

        document.getElementById("minTemperature").textContent =
            data.minimum_temperature.toFixed(2) + " °C";

        document.getElementById("avgHumidity").textContent =
            data.average_humidity.toFixed(2) + " %";

        document.getElementById("maxHumidity").textContent =
            data.maximum_humidity.toFixed(2) + " %";

        document.getElementById("minHumidity").textContent =
            data.minimum_humidity.toFixed(2) + " %";

    } catch (error) {

        console.error("Analytics Error:", error);

        throw error;

    }
}



async function refreshDashboard() {

    const button = document.getElementById("refreshButton");

    button.disabled = true;
    button.textContent = "Refreshing...";

    updateConnectionStatus("Updating");

    try {

        const results = await Promise.allSettled([
            fetchSensorData(),
            fetchHistoricalData(),
            fetchAnalytics()
        ]);

        const sensorDataAvailable = results[0].status === "fulfilled";

        if (sensorDataAvailable) {
            updateConnectionStatus("Connected");
        } else {
            updateConnectionStatus("Disconnected");
        }

    } finally {

        button.disabled = false;
        button.textContent = "↻ Refresh Data";

    }
}




// Initial data loading
fetchSensorData();
fetchHistoricalData();
fetchAnalytics();

// Automatic refresh every 20 seconds
setInterval(() => {
    fetchSensorData();
    fetchHistoricalData();
    fetchAnalytics();
}, 20000);

document.getElementById("refreshButton")
    .addEventListener("click", refreshDashboard);

