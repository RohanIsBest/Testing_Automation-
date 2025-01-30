import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit
from pymodbus.client import ModbusSerialClient as ModbusClient
from PyQt5.QtCore imp
class HMITestApp(QWidget):
    def __init__(self):
        super().__init__()

        # Setup Modbus client (adjust the serial port, baudrate, etc. as needed)
        self.client = ModbusClient(port='/dev/ttyUSB0', baudrate=9600, timeout=1, stopbits=1, bytesize=8, parity='N')
        self.client.connect()

        # GUI Setup
        self.setWindowTitle("HMI Testing Application")
        self.layout = QVBoxLayout()

        # Button 1 test
        self.button1 = QPushButton("Test Button 1", self)
        self.button1.clicked.connect(self.test_button1)
        self.layout.addWidget(self.button1)

        # Button 2 test
        self.button2 = QPushButton("Test Button 2", self)
        self.button2.clicked.connect(self.test_button2)
        self.layout.addWidget(self.button2)

        # Zoom In/Out test
        self.zoom_in_out_button = QPushButton("Test Zoom In/Out", self)
        self.zoom_in_out_button.clicked.connect(self.test_zoom_in_out)
        self.layout.addWidget(self.zoom_in_out_button)

        # Low Power Indicator test
        self.low_power_button = QPushButton("Test Low Power Indicator", self)
        self.low_power_button.clicked.connect(self.test_low_power_indicator)
        self.layout.addWidget(self.low_power_button)

        # Log area for feedback
        self.log_area = QTextEdit(self)
        self.log_area.setReadOnly(True)
        self.layout.addWidget(self.log_area)

        # Set layout and show window
        self.setLayout(self.layout)

    def log(self, message):
        """Log message to the text area."""
        self.log_area.append(message)

    def test_button1(self):
        self.log("Testing Button 1...")
       
        success = self.send_modbus_command(coil_address=1)   # Send command to HMI via Modbus (replace with actual address and coil)
        if success:
            self.log("Button 1 tested successfully.")
        else:
            self.log("Button 1 test failed.")

    def test_button2(self):
        self.log("Testing Button 2...")
        success = self.send_modbus_command(coil_address=2)
        if success:
            self.log("Button 2 tested successfully.")
        else:
            self.log("Button 2 test failed.")

    def test_zoom_in_out(self):
        self.log("Testing Zoom In/Out...")
        
        zoom_in_success = self.send_modbus_command(coil_address=3)  # Send Zoom In command
        time.sleep(1)                                               # Simulate delay
        
        zoom_out_success = self.send_modbus_command(coil_address=4) # Send Zoom Out command

        if zoom_in_success and zoom_out_success:
            self.log("Zoom In/Out tested successfully.")
        else:
            self.log("Zoom In/Out test failed.")

    def test_low_power_indicator(self):
        self.log("Testing Low Power Indicator...")
       
        success = self.send_modbus_command(coil_address=5)           # Simulate low power condition
        if success:
            self.log("Low Power Indicator tested successfully.")
        else:
            self.log("Low Power Indicator test failed.")

    def send_modbus_command(self, coil_address):
        """Send a command to the HMI via Modbus to activate a coil (e.g., simulate a button press)."""
        try:
            
            self.client.write_coil(coil_address, True)              # Send a Modbus write command to activate the coil
            time.sleep(1)                                           # Wait for action to complete

            result = self.client.read_coils(coil_address, 1)        # Read back the coil to verify it was set
            if result.bits[0]:
                return True
            else:
                return False
        except Exception as e:
            self.log(f"Modbus command failed: {e}")
            return False

    def closeEvent(self, event):
        """Clean up when closing the app."""
        self.client.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HMITestApp()
    window.show()
    sys.exit(app.exec_())
