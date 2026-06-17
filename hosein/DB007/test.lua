local keys = redis.call('KEYS', 'counter:*')
local result = {}
for i, key in ipairs(keys) do
    result[i] = {key, tonumber(redis.call('GET', key))}
end
return result