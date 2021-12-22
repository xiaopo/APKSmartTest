
print('========================================欢迎使用GameProfiler自动化测试工具=====================================')

--开启白点和输出
CS.XProfiler.ActivedProfiler(true);
CS.XOptimizeUtility.InitDebug()
local TemperatureManager = CS.TemperatureManager.Instance
TemperatureManager.isShowTemperature = true
EVENT_SAFE = false
G_FUNC_DEBUG_ENABLE(true)

		
local Application = CS.UnityEngine.Application

local Timerfunc = require("game.framework.funcs.Timerfunc")

local basePath = Application.persistentDataPath .."/GameProfiler"
--===================================================输出路径======================
local outpaht =  basePath .."/profile.data"

--===============================================================================


--=================================创建一个gameObject添加到场景=============

local gameObect = CS.UnityEngine.GameObject("GameProfiler")

CS.UnityEngine.GameObject.DontDestroyOnLoad(gameObect)


--=================================c# 部分 ===================================

local Assembly    = CS.System.Reflection.Assembly
local Activator	  = CS.System.Activator

local dllPath = basePath .. "/GameProfiler.dll"
local dll     = Assembly.LoadFrom(dllPath); --获得dll路径

if not dll then return end
local calltype	= dll:GetType("GameProfiler.GameProfilerComponent");
local gameProfiler = gameObect:AddComponent(calltype)



gameProfiler.SEND_FRAME 		= 60;--写出间隔帧
gameProfiler.RECORD_FRAME		= 1;--记录间隔帧

local TemperatureManager = CS.TemperatureManager.Instance
--=================================指定一个服务器=======================
local sverData;

-- sverData = 
-- {
--     ['unit_server'] = '99001',
--     ['code'] = '1',
--     ['ip2'] = '129.204.7.205#129.204.7.205#129.204.7.205',
--     ['status'] = '1',
--     ['ip'] = '129.204.7.205:9550',
--     ['name'] = "外网测试服",
--     ['create_time'] = 0,
--  }

sverData =
{
    ['unit_server'] = '109999',
    ['code'] = '9999',
    ['ip2'] = '10.0.100.14#10.0.100.14#10.0.100.14',
    ['status'] = '1',
    ['ip'] = '10.0.100.14:9530',
    ['name'] = "内网14",
    ['create_time'] = 0,--1554121796

}

-- sverData =
-- {
--     ['unit_server'] = '110003',
--     ['code'] = '14',
--     ['ip2'] = '10.0.100.14#10.0.100.14#10.0.100.14',
--     ['status'] = '1',
--     ['ip'] = '10.0.100.14:9531',
--     ['name'] = "内网14-2",
--     ['create_time'] = 0,--1554121796

-- }



GameProfiler_serverData = sverData

local GameProfiler = {}

function GameProfiler.Start()
	--激活
	gameProfiler:InitProfiler(outpaht)
end

function GameProfiler.Stop()
	CS.UnityEngine.GameObject.Destroy(gameObect)
end

function GameProfiler.SetLevel(level)
	gameProfiler.FrameInfoVer.level = level
end

function GameProfiler.SetCurrentUIName(currentOpenUI)
	gameProfiler.FrameInfoVer.currentOpenUI = currentOpenUI
end

Timerfunc.register(function ()
    gameProfiler.FrameInfoVer.luaMemory = collectgarbage("count")/1024
    gameProfiler.FrameInfoVer.temperature = TemperatureManager.temperatureInt /10
end,0,-1)

_G.GameProfiler = GameProfiler

return GameProfiler