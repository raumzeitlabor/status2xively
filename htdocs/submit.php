<?php
$filename = "data.json";

if (!is_writable($filename)) {
	echo $filename. " nicht schreibbar";
	exit;
}

$output = json_decode(file_get_contents($filename),true);

if (array_key_exists("members", $_REQUEST) && is_numeric($_REQUEST["members"])) {
  $value = intval($_REQUEST["members"]);

  $output["members"] = $value;
  echo "Das RZL hat jetzt $value Mitglieder. ";
}

if (array_key_exists("account", $_REQUEST) && is_numeric($_REQUEST["account"])) {
  $value = floatval($_REQUEST["account"]);
  $value = round($value,2);
	$output["account"] = $value;
  echo "Das RZL hat jetzt $value Geldeinheiten auf dem Konto. ";
}

file_put_contents($filename, json_encode($output));
