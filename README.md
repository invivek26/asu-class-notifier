# Class Seat Notifier

This project is designed to monitor the availability of seats in a specified class at Arizona State University (ASU). If seats become available, the program sends an email and SMS notification to the specified recipient.

## Features

- Periodically checks the availability of seats in a specified class.
- Sends email notifications when seats are available.
- Validates input data and email addresses.
- Supports sending SMS notifications via email to different carriers.

## Requirements

- Python 3.x
- The following Python packages:
  - `requests`
  - `PyYAML`
- An email account to send notifications from.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/class-seat-notifier.git
   cd class-seat-notifier
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `config.json` file in the project directory with the following format:

   ```json
   {
     "classnum": "12345",
     "phone_number": "1234567890",
     "carrier": "AT&T",
     "email_id": "your_email@example.com"
   }
   ```

4. Create a `credentials.yaml` file in the project directory with your email credentials:

   ```yaml
   user: "your_email@example.com"
   password: "your_password"
   ```

## Usage

Run the script using the following command:

```bash
python main.py
```

OR

```bash
python3 main.py
```

The script will continuously check the availability of seats in the specified class. When seats become available, it will send an email notification to the specified recipient and stop checking.

## Configuration

### `config.json`

- `classnum`: The 5-digit class number to monitor.
- `phone_number`: The 10-digit phone number to receive SMS notifications.
- `carrier`: The carrier of the phone number (must be one of the supported carriers).
- `email_id`: The email address to receive notifications.

### `credentials.yaml`

- `user`: The email address to send notifications from.
- `password`: The password for the email account.

### Supported Carriers

The following carriers are supported for SMS notifications:

- AT&T
- Sprint
- T-Mobile
- Verizon Wireless
- Virgin Mobile
- Rogers Wireless
- Boost Mobile
- Telus Mobility
- Airfire Mobile
- Ameritech
- Assurance Wireless
- BellSouth
- Bluegrass Cellular
- Cellcom
- Cellular South
- Chariton Valley Wireless
- Chat Mobility
- Cleartalk
- Consumer Cellular
- Cricket
- Element Mobile
- Esendex
- Mellon Mobile
- MetroPCS
- Nextech
- Page Plus Cellular (Verizon MVNO)
- South Central Communications
- Southernlinc
- Straight Talk
- Syringa Wireless
- Teleflip
- Union Wireless
- US Cellular
- Voyager Mobile
- Centennial Wireless
- TracFone (prepaid)

## Functions

### `fetch_class_info(class_num)`

Fetches the class information for a given class number.

**Args:**

- `class_num` (str): The class number to fetch information for.

**Returns:**

- `int`: The number of available seats in the class.

### `input_data()`

Reads and validates input data from the `config.json` file.

**Returns:**

- `list`: A list containing class number, phone number, carrier, and email ID.

**Raises:**

- `ValueError`: If the input data is not valid.

### `get_credentials(filepath)`

Gets email credentials from a YAML file.

**Args:**

- `filepath` (str): The path to the credentials YAML file.

**Returns:**

- `tuple`: A tuple containing the email address and password.

**Raises:**

- `Exception`: If there is an error loading the credentials file.

### `send_mail(email_id, class_num)`

Sends an email notification that a class is open.

**Args:**

- `email_id` (str): The recipient's email address.
- `class_num` (str): The class number to include in the email.

**Raises:**

- `Exception`: If there is an error sending the email.

### `main()`

Main function to check class availability and send notifications.

## License

This project is licensed under the MIT License.

---

## Contribution

Feel free to open issues and submit pull requests if you have any suggestions or improvements.

---
