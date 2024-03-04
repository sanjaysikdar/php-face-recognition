<?php

// Execution start time
$start_time = microtime(true); 

// MAIN CODE START
$knownImage = "img/fake.jpg";
$unknownImage = "img/fake (1).jpg";

// Use escapeshellarg to safely escape image paths
$knownImage = escapeshellarg($knownImage);
$unknownImage = escapeshellarg($unknownImage);

// Command Args
$command = "python face_r.py $knownImage $unknownImage";

// Executing
$output = shell_exec($command);

// Printing the output
echo "OUTPUT: $output\n";

// Parsing Data
$output = str_replace(['(', ')'], '', $output); // Remove opening and closing parentheses

list($result, $confidence) = explode(',', $output);

// Condition Check
if (trim($result) === 'True' && (float)$confidence >= 0.5) {
    echo "User authenticated with confidence level: " . number_format((float)$confidence * 100, 2) . "%";
} else {
    echo "Authentication failed.";
}
// MAIN CODE END

// Execution end time
echo "\n-------------------------------------\n";
$end_time = microtime(true);
$execution_time = round($end_time - $start_time, 2);
echo "Script execution time: $execution_time seconds\n";
echo "-------------------------------------\n";
?>
