<?php
// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $doctor = $_POST["doctor"];
    $date = $_POST["date"];
    $time = $_POST["time"];

    // Validate form data (add more validation as needed)
    if (empty($doctor) || empty($date) || empty($time)) {
        // Handle validation error
        echo "Please fill in all fields.";
    } else {
        // Assuming you have a database connection
        // Connect to your database
        $servername = "localhost";
        $username = "username";
        $password = "password";
        $dbname = "appointments";

        $conn = new mysqli($servername, $username, $password, $dbname);

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Insert appointment into database
        $sql = "INSERT INTO appointments (doctor, date, time) VALUES ('$doctor', '$date', '$time')";

        if ($conn->query($sql) === TRUE) {
            echo "Appointment booked successfully!";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }

        // Close database connection
        $conn->close();
    }
} else {
    // Handle invalid form submission
    echo "Invalid form submission.";
}
?>
