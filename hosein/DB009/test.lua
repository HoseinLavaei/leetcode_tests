local user = "alice"
local limit = 5
local window = 60
local start_time = 1000
local total_requests = 7
local step = 10

local key = "rate_limit:" .. user
local allowed = 0

for i = 0, total_requests - 1 do
    local now = start_time + i * step
    
    -- Remove entries older than the window
    redis.call('ZREMRANGEBYSCORE', key, 0, now - window)
    
    -- Count current entries
    local count = redis.call('ZCARD', key)
    
    if count < limit then
        -- Allow the request: store the timestamp as score and member
        redis.call('ZADD', key, now, now)
        redis.call('EXPIRE', key, window)
        allowed = allowed + 1
    end
end

return allowed