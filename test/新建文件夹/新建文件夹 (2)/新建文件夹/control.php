<?php
$data = $_REQUEST;
$type = $data['type']??'';
if($type!=''){
  //echo passthru("sh /home/run_cmd.sh $type");
  echo exec("cd /home;./brun_cmd $type");	
  exit;
}
?>
<html>
<head>
</head>
<body>
<input type="button" value="更新琅琊榜服务器" onclick="run_cmd('update_lyb');">
<input type="button" value="更新至尊霸业服务器" onclick="run_cmd('update_zzby');">
<input type="button" value="更新小闹天宫服务器" onclick="run_cmd('update_xntg');">
<input type="button" value="更新仙侠服务器" onclick="run_cmd('update_xian');">
</br>
<input type="button" value="强制关闭琅琊榜服务器" onclick="run_cmd('forcestop_lyb');">
<input type="button" value="强制关闭至尊霸业服务器" onclick="run_cmd('forcestop_zzby');">
<input type="button" value="强制关闭小闹天宫服务器" onclick="run_cmd('forcestop_xntg');">
<input type="button" value="强制关闭仙侠服务器" onclick="run_cmd('forcestop_xian');">
<div id="test"></div>
<!-- <form method="post" action="tcontrol.php">
<input type="submit" value="输出信息aaaa">
</form> -->
<!-- <button type="button"><div id="buttonValue" onclick="add();">更新琅琊榜服务器</div></button> -->
<script src="http://cdn.static.runoob.com/libs/jquery/1.10.2/jquery.min.js"></script>
<script>
	function run_cmd(pparam) {
		$("#test").html('正在执行中...');
		$.ajax({
			type: 'GET',
			url: 'control.php',
			data: {
				type:pparam
			},
			success:function (response) {
				$("#test").html(response);
				//alert(response);
		    }
		});
	}
</script>
</body>
</html>
