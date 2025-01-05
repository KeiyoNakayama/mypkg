import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests

class EarthquakePublisher(Node):
    def __init__(self):
        super().__init__('earthquake_publisher')
        self.publisher = self.create_publisher(String, 'earthquake', 10)
        self.timer = self.create_timer(10.0, self.publish_earthquake_info)
        
    def fetch_earthquake(self):
        url = "https://www.j-shis.bosai.go.jp/api-pshm-meshinfo"
        params = {
            "lat": 35,
            "lon": 139,
            "out": "json",
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def publish_earthquake_info(self):
        data = self.fetch_earthquake()
        hazard_info = data.get("hazard", "No hazard data available")
        message = String()
        message.data = f"Earthquake Hazard Info:\n{hazard_info}"
        self.publisher.publish(message)


def main():
    rclpy.init()
    node = EarthquakePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

