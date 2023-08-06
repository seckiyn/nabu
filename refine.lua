--	time.lua
--	'c' shows current time on keypress;                     keybind name: "show_time_fn"
--	'C' shows what the time will be at the end of playback; keybind name: "show_end_time_fn"
--	Link: https://github.com/mustaqimM/mpv-scripts/time.lua


options = require 'mp.options'


-- function show_time_fn()
-- 	mp.msg.info(os.date(hour .. ':%M'))
-- 	mp.osd_message(os.date(hour .. ":%M"))
-- end
-- 
-- 
-- function show_end_time_fn()
-- 	clock_hour = tonumber(os.date(hour))
-- 	clock_minutes = tonumber(os.date("%M"))
-- 
-- 	local remaining_t_seconds = mp.get_property_number("playtime-remaining") or 0
-- 	remaining_t_hours = math.floor(remaining_t_seconds / 3600)
-- 	remaining_t_min = (remaining_t_seconds / 60) % 60
-- 
-- 	end_hour = clock_hour + remaining_t_hours
-- 	end_min = math.floor(clock_minutes + remaining_t_min)
-- 
-- 	if end_min >= 60 then
-- 		end_hour = math.floor(end_hour + (end_min / 60))
-- 		end_min = math.floor(end_min % 60)
-- 	end
-- 
-- 	if end_hour >= 24 then
-- 		end_hour = math.abs(end_hour % 24)
-- 	end
-- 
-- 	mp.msg.info(string.format("Playback will end at: %02d:%02d", end_hour, end_min))
-- 	mp.osd_message(string.format("Playback will end at: %02d:%02d", end_hour, end_min))
-- end

start_time = ""
end_time = ""

print("hello world")
function write_to_file(towrite)
    filename = mp.get_property("filename") .. ".timestamp" -- get the filename
    towrite = towrite .. "\n"
    -- print("filename", filename)
    -- print(type(filename))
    opened = io.open(filename, "a") -- open the file in append mode
    opened:write(towrite)           -- write the thing that you should write
    opened:close()                  -- close while you're out
    
end

function flash(word)
    mp.msg.info(word)
    mp.osd_message(word)
end
function return_pos()
    my_time = mp.get_property("time-pos")
    flash(my_time)
    return my_time
end

function set_start_time()
    start_time = return_pos()
end

function set_end_time()
    end_time = return_pos()
end

function save_start_end_time()
    se_time = start_time .. "-" .. end_time
    flash(se_time)
    write_to_file(se_time)
end

-- mp.add_key_binding(opts.time, "show_time", show_time_fn)
-- mp.add_key_binding(opts.key, "show_end_time", show_end_time_fn)

-- mp.remove_key_binding("s")
-- mp.remove_key_binding("d")
mp.add_forced_key_binding("s", "set_start_time", set_start_time)
mp.add_forced_key_binding("d", "set_end_time", set_end_time)
mp.add_key_binding("ENTER", "save_start_end_time", save_start_end_time)

