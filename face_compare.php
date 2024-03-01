<?php

// Execution start time
$start_time = microtime(true); 

// MAIN CODE START
$knownImage = "img/real.jpg";
$unknownImage = "img/fake (2).jpg";

$command = "python face_r.py $knownImage $unknownImage";
$output = shell_exec($command);

if (trim($output) === "Authentication successful!") {
    echo "User authenticated!";
} else {
    echo "Authentication failed.";
    
}
// MAIN CODE END


// Execution end time
echo "\n";
$end_time = microtime(true);
$execution_time = round($end_time - $start_time, 2);
echo "Script execution time: $execution_time seconds";
echo "\n";
?>