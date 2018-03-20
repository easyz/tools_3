var func_getVersionUrl = Main.prototype.getVersionUrl
var temp_dict = {}
Main.prototype.getVersionUrl = function(t) {
	var url = func_getVersionUrl(t)
	if (!temp_dict[url]) {
		temp_dict[url] = true
		var list = []
		for (var k in temp_dict) {
			list.push(k)
		}
		console.log("")
		console.log("")
		console.log("")
		console.log(">>>>>>>>>>>>>>>>>>>>>>>")
		console.log(list.join("\n"))
	}
	return url
}
RES.web.Html5VersionController.prototype.getVirtualUrl = Main.prototype.getVersionUrl