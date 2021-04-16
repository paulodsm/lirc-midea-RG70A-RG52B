<!DOCTYPE HTML>
<html lang="pt-br">

<!-- This file can be run in a apache server that also runs lirc with MIDEA_RAW codes -->


<?php

	$mode = 'cool';
	$fan = 'low';
	$temp = '25';
	$check_mode = ['','checked="checked"',''];
	$check_fan = ['checked="checked"','',''];

	if($_SERVER['REQUEST_METHOD'] == "POST")
	{
		$mode = $_POST['mode'];
		$fan = $_POST['fan'];
		$temp = $_POST['temp'];
		$status = $_POST['status'];
		#echo $status . '-' . $mode . '-' . $fan . '-' . $temp;
		
		if ($status == 'OFF'){exec('irsend SEND_ONCE MIDEA_RAW off');}
		
		if ($status == 'SILENCIAR'){exec('irsend SEND_ONCE MIDEA_RAW silent');}
		
		if ($mode == 'fan'){
			$temp='off';
			$check_mode = ['checked="checked"','',''];
			}
		if ($mode == 'cool'){$check_mode = ['','checked="checked"',''];}
		if ($mode == 'heat'){$check_mode = ['','','checked="checked"'];}
		
		if ($fan == 'low'){$check_fan = ['checked="checked"','',''];}
		if ($fan == 'med'){$check_fan = ['','checked="checked"',''];}
		if ($fan == 'max'){$check_fan = ['','','checked="checked"'];}
		
		
		
		if ($status == 'ON / Alterar'){exec('irsend SEND_ONCE MIDEA_RAW S.on-M.'.$mode.'-F.'.$fan.'-T.'.$temp);}
		
		if ($temp == 'off'){$temp='25';}
		
	}

	
?>


<head>

<meta name="viewport" content="width=device-width">

<style type="text/css">

body {
    text-align: center;
}

input[type="number"] {
  -webkit-appearance: textfield;
  -moz-appearance: textfield;
  appearance: textfield;
}

input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none;
}

.number-input {
  border: 2px solid #ddd;
  display: inline-flex;
}

.number-input,
.number-input * {
  box-sizing: border-box;
}

.number-input button {
  outline:none;
  -webkit-appearance: none;
  background-color: transparent;
  border: none;
  align-items: center;
  justify-content: center;
  width: 2rem;
  height: 2rem;
  cursor: pointer;
  margin: 0;
  position: relative;
}

.number-input button:before,
.number-input button:after {
  display: inline-block;
  position: absolute;
  content: '';
  width: 1rem;
  height: 2px;
  background-color: #212121;
  transform: translate(-50%, -50%);
}
.number-input button.plus:after {
  transform: translate(-50%, -50%) rotate(90deg);
}

.number-input input[type=number] {
  font-family: sans-serif;
  max-width: 5rem;
  padding: .5rem;
  border: solid #ddd;
  border-width: 0 2px;
  font-size: 1.7rem;
  height: 2rem;
  font-weight: bold;
  text-align: center;
}

.disable{
pointer-events:none;
background:#E6E6E6;
}

</style>

<title>Midea Ar Cond.</title>

</head>

<body>

<p style="font-size:1px;">&nbsp</p>

<h1 style="margin: 8px;">Midea AC</h1>


<form action="." method="post">
  <p>Modo:
  <input type="radio" id="fan" name="mode" value="fan" <?php echo $check_mode[0]; ?>>
  <label for="fan">Ventilar</label>
  <input type="radio" id="cool" name="mode" value="cool" <?php echo $check_mode[1]; ?>>
  <label for="cool">Frio</label>
  <input type="radio" id="heat" name="mode" value="heat" <?php echo $check_mode[2]; ?>>
  <label for="heat">Quente</label></p>

  <p>Ventilação:
  <input type="radio" id="low" name="fan" value="low" <?php echo $check_fan[0]; ?>>  
  <label for="low">Fraca</label>
  <input type="radio" id="med" name="fan" value="med" <?php echo $check_fan[1]; ?>>
  <label for="med">Média</label>
  <input type="radio" id="max" name="fan" value="max" <?php echo $check_fan[2]; ?>>
  <label for="max">Forte</label></p>
  

  Temperatura:
  <div class="number-input">
  <button type="button" onclick="this.parentNode.querySelector('input[type=number]').stepDown()" ></button>
  <input min="17" max="30" id="temp" name="temp" value=<?php echo $temp; ?> type="number" class="disable" >
  <button type="button" onclick="this.parentNode.querySelector('input[type=number]').stepUp()" class="plus"></button>
  </div>

  <p>
  <input type="submit" name="status" value="ON / Alterar" style="font-size:20px; height:30px; width: 180px;">
  </p>
  <p>
  <input type="submit" name="status" value="SILENCIAR" style="font-size:20px; height:30px; width: 180px;" />
  </p>
  <p>
  <input type="submit" name="status" value="OFF" style="font-size:20px; height:30px; width: 180px;" />
  </p>
</form>


</body>
</html>
