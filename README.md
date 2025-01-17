# Python Windows System Monitoring Flask App

## Project Description

The **Python Windows System Monitoring Flask App** is a lightweight web-based application for monitoring system performance and retrieving system information on Windows machines. It provides real-time metrics such as CPU, RAM, Disk, and Network usage, along with options to view detailed system information using a user-friendly interface. The app is built using Flask and leverages the `psutil` library for system performance monitoring.

## Features

- **Real-Time Metrics**: 
  - CPU usage percentage
  - RAM usage percentage
  - Disk usage percentage
  - Network data sent and received

- **System Information**: 
  - Basic details: OS, machine, processor, and more.
  - Full system details via the `systeminfo` command.

- **Interactive Web Interface**:
  - Dynamic progress bars for real-time CPU, RAM, and Disk usage.
  - Network usage stats in MB.
  - Toggle between basic and full system information.

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS (Bootstrap), JavaScript (jQuery)
- **System Monitoring**: `psutil`, `platform`

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone [https://github.com/hrparab99/Python-MonitoringApp-Using-Flask.git]
   cd python-windows-system-monitor
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python sys_monitoring_app.py
   ```

5. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## File Structure

```plaintext
.
├── app.py               # Main Flask application file
├── templates
│   └── index.html       # HTML template for the web interface
├── static               # Directory for static assets (if any in future)
├── requirements.txt     # List of Python dependencies
└── README.md            # Project documentation
```

## API Endpoints

- **GET /**: Displays the main dashboard with basic system information.
- **GET /usage**: Returns real-time system usage metrics (CPU, RAM, Disk, Network).
- **GET /full-info**: Provides detailed system information when queried with `?show=true`.

## Future Enhancements

- Add support for cross-platform compatibility (Linux, Mac).
- Introduce historical performance graphs using a library like Chart.js.
- Implement user authentication for accessing system info.
- Extend monitoring to specific processes or services.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

## Acknowledgements

- The `psutil` library for system monitoring.
- Bootstrap for responsive UI design.
- Flask for making web development simple and efficient.

---

Developed with ❤️ using Python.
