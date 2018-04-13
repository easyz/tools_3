#!/bin/bash
log_file=`pwd`"/log_run_cmd.txt"
echo "========== run_cmd: `date '+%Y-%m-%d %H:%M:%S'` ==========" >> $log_file
help ()
{
	echo "gamectl 使用说明"
	echo "基本语法: gamectl [start|stop|restart|client|cross|update] "
	echo "命令模块："
	echo "help						显示当前帮助内容"
	echo "start						启动游戏服务"
	echo "startbg					后台运行游戏服务"
	echo "stop                      关闭游戏服务"
	echo "stopall                   关闭所有服务"
	echo "restart                   重新启动游戏服务"
	echo "client					启动模拟客户端"
	echo "record					启动后台数据服务"
	echo "platform					启动平台登录服务"
	echo "cross						启动跨服服务"
	echo "crossw					启动跨服逻辑服务"
	echo "update                    更新lua脚本"
	echo "updateall                 更新所有服务lua脚本"
	echo "调用失败"
}

update_lyb ()
{
	cd "/home/lyb"
	svn up --config-dir /root/.subversion 2>&1 >> $log_file
	chmod +x /home/lyb/server/lua/libc++/*
	cd "/home/lyb/server/sql"
	bash alter_db.sh "update" 2>&1 >> $log_file
	cd "/home/lyb/server/sh"
	bash gamectl.sh "restart" 2>&1 >> $log_file
	echo "更新琅琊榜服务器成功" >> $log_file
	echo "更新琅琊榜服务器成功"
	exit 0
}

forcestop_lyb ()
{
	cd "/home/lyb/server/sh"
	bash gamectl.sh "forcestop" 2>&1 >> $log_file
	echo "强制关闭琅琊榜服务器成功" >> $log_file
	echo "强制关闭琅琊榜服务器成功"
	exit 0
}

update_zzby ()
{
	cd "/home/develop"
	svn up --config-dir /root/.subversion 2>&1 >> $log_file
	chmod +x /home/develop/server/lua/libc++/*
	cd "/home/develop/server/sql" 
	bash alter_db.sh "update" 2>&1 >> $log_file
	cd "/home/develop/server/sh"
	bash gamectl.sh "restart" 2>&1 >> $log_file
	echo "更新至尊霸业服务器成功" >> $log_file
	echo "更新至尊霸业服务器成功"
	exit 0
}

forcestop_zzby ()
{
	cd "/home/develop/server/sh"
	bash gamectl.sh "forcestop" 2>&1 >> $log_file
	echo "强制关闭至尊霸业服务器成功" >> $log_file
	echo "强制关闭至尊霸业服务器成功"
	exit 0
}

update_xntg ()
{
	cd "/home/xntg"
	svn up --config-dir /root/.subversion 2>&1 >> $log_file
	chmod +x home/xntg/server/libc++/*
	cd "/home/xntg/server/sh"
	bash gamectl.sh "restart" 2>&1 >> $log_file
	echo "更新小闹天宫服务器成功" >> $log_file
	echo "更新小闹天宫服务器成功"
	exit 0
}
forcestop_xntg ()
{
	cd "/home/xntg/server/sh"
	bash gamectl.sh "forcestop" 2>&1 >> $log_file
	echo "强制关闭小闹天宫服务器成功" >> $log_file
	exit 0
}

update_xian ()
{
	cd "/home/xian"
	svn up --config-dir /root/.subversion 2>&1 >> $log_file
	chmod +x /home/xian/server/lua/libc++/*
	cd "/home/xian/server/sql"
	bash alter_db.sh "update" 2>&1 >> $log_file
	cd "/home/xian/server/sh"
	bash gamectl.sh "restart" 2>&1 >> $log_file
	echo "更新仙侠服务器成功" >> $log_file
	echo "更新仙侠服务器成功"
	exit 0
}

forcestop_xian ()
{
	cd "/home/xian/server/sh"
	bash gamectl.sh "forcestop" 2>&1 >> $log_file
	echo "强制关闭仙侠服务器成功" >> $log_file
	echo "强制关闭仙侠服务器成功"
	exit 0
}

TARGET=$1
shift
case $TARGET in
	update_lyb) update_lyb;;
	forcestop_lyb) forcestop_lyb;;
	update_zzby) update_zzby;;
	forcestop_zzby) forcestop_zzby;;
	update_xntg) update_xntg;;
	forcestop_xntg) forcestop_xntg;;
	update_xian) update_xian;;
	forcestop_xian) forcestop_xian;;
	help) help;;
	*) help ;;
esac
echo "命令执行失败" >> $log_file
echo "命令执行失败"
