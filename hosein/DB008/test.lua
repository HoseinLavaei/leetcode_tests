-- Get all scores sorted descending
local all = redis.call('ZREVRANGE', 'leaderboard', 0, -1, 'WITHSCORES')
local scores = {}
local names_by_score = {}

for i = 1, #all, 2 do
    local name = all[i]
    local score = tonumber(all[i+1])
    if not names_by_score[score] then names_by_score[score] = {} end
    table.insert(names_by_score[score], name)
    scores[score] = true
end

-- Extract distinct scores and sort descending
local distinct = {}
for s, _ in pairs(scores) do table.insert(distinct, s) end
table.sort(distinct, function(a,b) return a > b end)

-- Take first 3 distinct scores (or fewer)
local result = {}
local rank = 0
for _, score in ipairs(distinct) do
    rank = rank + 1
    if rank > 3 then break end
    for _, name in ipairs(names_by_score[score]) do
        table.insert(result, {name, score})
    end
end
return result