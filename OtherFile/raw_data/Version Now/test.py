#去除中文
import re
p1='1-ID20011101-大型水史莱姆-ID3-提瓦特'
line=re.sub('[\u4e00-\u9fa5]', '', p1)

print(line)
gadgets = {
	{ config_id = 645001, gadget_id = 70540039, pos = { x = -1349.125, y = 318.937, z = 3669.815 }, rot = { x = 0.000, y = 78.968, z = 0.000 }, level = 30, area_id = 23 },
	{ config_id = 645002, gadget_id = 70500000, pos = { x = -1348.923, y = 318.445, z = 3670.085 }, rot = { x = 48.676, y = 4.457, z = 305.374 }, level = 30, point_type = 2050, owner = 645001, area_id = 23 },
	{ config_id = 645003, gadget_id = 70540039, pos = { x = -1348.128, y = 320.997, z = 3650.332 }, rot = { x = 356.371, y = 101.724, z = 359.247 }, level = 30, area_id = 23 },
	{ config_id = 645004, gadget_id = 70500000, pos = { x = -1347.806, y = 320.525, z = 3650.504 }, rot = { x = 46.880, y = 30.761, z = 310.200 }, level = 30, point_type = 2050, owner = 645003, area_id = 23 },
	{ config_id = 645005, gadget_id = 70540039, pos = { x = -1351.120, y = 320.413, z = 3642.861 }, rot = { x = 0.000, y = 124.035, z = 0.000 }, level = 30, area_id = 23 },
	{ config_id = 645006, gadget_id = 70500000, pos = { x = -1350.786, y = 319.921, z = 3642.910 }, rot = { x = 48.676, y = 49.522, z = 305.374 }, level = 30, point_type = 2050, owner = 645005, area_id = 23 },
	{ config_id = 645007, gadget_id = 70500000, pos = { x = -1348.766, y = 318.488, z = 3669.691 }, rot = { x = 359.439, y = 351.196, z = 266.379 }, level = 30, point_type = 2050, area_id = 23 },
	{ config_id = 645008, gadget_id = 70500000, pos = { x = -1348.719, y = 318.012, z = 3669.473 }, rot = { x = 331.930, y = 353.094, z = 265.896 }, level = 30, point_type = 2050, area_id = 23 },
	{ config_id = 645009, gadget_id = 70500000, pos = { x = -1347.857, y = 319.979, z = 3650.207 }, rot = { x = 0.007, y = 351.178, z = 270.042 }, level = 30, point_type = 2050, area_id = 23 },
	{ config_id = 645010, gadget_id = 70500000, pos = { x = -1351.122, y = 319.355, z = 3642.341 }, rot = { x = 1.956, y = 32.230, z = 266.901 }, level = 30, point_type = 2050, area_id = 23 },
	{ config_id = 645011, gadget_id = 70500000, pos = { x = -1347.853, y = 320.416, z = 3649.943 }, rot = { x = 0.008, y = 349.073, z = 270.042 }, level = 30, point_type = 2050, area_id = 23 }
}
