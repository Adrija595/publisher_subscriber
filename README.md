## Publisher Subscriber using Iris Dataset

Steps to RUN:
- Start the **Kafka Server**
    * Start `Docker Desktop`
    * Staring `Kafka Server`
        ```sh
        confluent local kafka start --plaintext-ports 52466
        ```
- Start the **Flask Server**
  ```sh
  python server.py
  ```
- Start the **gRPC Store Service**
  ```sh
  python store_service.py
  ```
- Start the **Consumers**
  ```sh
  python consumer1.py   # For Classification
  python consumer2.py   # For Regression
  ```
- Start the **Publisher**
  ```sh
  python subscrier.py
  ```
<br>

Testing using **Postman**
- Open `Postman`
- Set Method to `POST`
- JSON Body
  ```sh
  {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 4.1,
    "petal_width": 0.2
  }  
  ```

  


  