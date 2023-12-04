function searchCity() {
    const searchInput = document.getElementById("searchInput");
    const resultDiv = document.getElementById("result");
    const cityName = searchInput.value;

    // Clear previous search results
    resultDiv.innerHTML = "";

    // Example data for a bar chart
    const chartData = {
        labels: ['Temperature', 'Humidity', 'Pressure'],
        datasets: [{
            label: cityName,
            data: [72, 50, 1020], // Example data, replace with real data
            backgroundColor: ['rgba(75, 192, 192, 0.2)', 'rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)'],
            borderColor: ['rgba(75, 192, 192, 1)', 'rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)'],
            borderWidth: 1
        }]
    };

    // Create and display a bar chart
    const chartCanvas = document.getElementById('chart').getContext('2d');
    new Chart(chartCanvas, {
        type: 'bar',
        data: chartData,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
