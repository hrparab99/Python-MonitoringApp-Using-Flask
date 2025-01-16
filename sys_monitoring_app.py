from flask import Flask, render_template, jsonify, request
import psutil  # Library for retrieving system performance metrics
import platform  # Library for retrieving system information
import datetime  # Library for working with date and time
import subprocess  # Library to run system commands

app = Flask(__name__)  # Initialize the Flask application

# Initialize CPU percent calculation to start tracking CPU usage
psutil.cpu_percent(interval=None)

# Execute a shell command and return its output as a string
def execute_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = "\n".join([line.strip() for line in result.stdout.splitlines() if line.strip()])
    return output

# Retrieve basic system information
def get_system_info():
    info = {
        "System Name": platform.system(),  # Operating system name
        "Node Name": platform.node(),  # System's network name
        "Release": platform.release(),  # OS release version
        "Version": platform.version(),  # OS version details
        "Machine": platform.machine(),  # Machine type (e.g., x86_64)
        "Processor": platform.processor(),  # Processor details
        "Date and Time": datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),  # Current date and time
    }
    return info

# Retrieve current CPU usage percentage
def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)  # Calculate CPU usage over a 1-second interval
    return cpu_percent

# Retrieve network usage statistics (sent and received in MB)
def get_network_usage():
    net_io = psutil.net_io_counters()
    sent = net_io.bytes_sent / (1024 * 1024)  # Convert bytes to MB
    recv = net_io.bytes_recv / (1024 * 1024)  # Convert bytes to MB
    return {"sent": round(sent, 2), "recv": round(recv, 2)}

# Retrieve disk usage percentage
def get_disk_usage():
    disk_usage = psutil.disk_usage('/')  # Get disk usage statistics for the root directory
    used_percent = disk_usage.percent  # Percentage of disk space used
    return used_percent

# Retrieve RAM usage percentage
def get_ram_usage():
    ram_usage = psutil.virtual_memory().percent  # Get percentage of RAM currently in use
    return ram_usage

# Retrieve full system information by running the "systeminfo" command
def get_full_system_info():
    command = "systeminfo"
    raw_output = execute_command(command)

    # Preprocess the raw output into a structured format
    formatted_output = []
    for line in raw_output.splitlines():
        if line.startswith(" "):  # Continuation of a previous line
            if formatted_output:  # Append to the last line if available
                formatted_output[-1] += f"\n{line.strip()}"
        else:
            formatted_output.append(line.strip())
    
    return "\n".join(formatted_output)

# Route for the main page
@app.route("/")
def index():
    system_info = get_system_info()  # Get basic system information
    return render_template("index.html", system_info=system_info)

# Route to fetch system usage metrics (RAM, Disk, CPU, and Network usage)
@app.route("/usage")
def get_usage():
    ram_percent = get_ram_usage()  # Get current RAM usage
    disk_percent = get_disk_usage()  # Get current Disk usage
    cpu_percent = get_cpu_usage()  # Get current CPU usage
    network_usage = get_network_usage()  # Get current network usage (sent/received)
    return jsonify(
        ram_percent=ram_percent,
        disk_percent=disk_percent,
        cpu_percent=cpu_percent,
        network_sent=network_usage["sent"],
        network_recv=network_usage["recv"],
    )

# Route to fetch full system information on demand
@app.route("/full-info", methods=["GET"])
def full_info():
    if request.args.get("show") == "true":  # Check if the "show" parameter is set to true
        full_info = get_full_system_info()  # Get full system information
        return jsonify(full_info=full_info)
    return jsonify(full_info="")  # Return empty if "show" is not true

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode