local board = script.Parent
local RunService = game:GetService("RunService")
local ChatService = game:GetService("Chat")
local HTTPService = game:GetService("HttpService")
local gameoverSent = false
local playerMark = "X"
local computerMark = "O"

local function XorO (space)
	if space.Text == "X" then
		return 2
	elseif space.Text == "O" then
		return 5
	end
	return 0
end

local function checkWinValue (val)
	if val == 6 then
		return "X"
	end

	if val == 15 then
		return "O"
	end

	return nil
end

local function threeInARow () 
	local row1 = 0
	local row2 = 0
	local row3 = 0
	local col1 = 0
	local col2 = 0
	local col3 = 0
	local diag1 = 0
	local diag2 = 0

	-- calculate the board state
	local spaces = board.SurfaceGui:GetChildren()
	for i, space in pairs(spaces) do
		if space:IsA("TextButton") then
			if space.Name == "TextButton1" then
				local val = XorO(space)
				row1 = row1 + val
				col1 = col1 + val
				diag1 = diag1 + val
			elseif space.Name == "TextButton2" then
				local val = XorO(space)
				row1 = row1 + val
				col2 = col2 + val
			elseif space.Name == "TextButton3" then
				local val = XorO(space)
				row1 = row1 + val
				col3 = col3 + val
				diag2 = diag2 + val
			elseif space.Name == "TextButton4" then
				local val = XorO(space)
				row2 = row2 + val
				col1 = col1 + val
			elseif space.Name == "TextButton5" then
				local val = XorO(space)
				row2 = row2 + val
				col2 = col2 + val
				diag1 = diag1 + val
				diag2 = diag2 + val
			elseif space.Name == "TextButton6" then
				local val = XorO(space)
				row2 = row2 + val
				col3 = col3 + val
			elseif space.Name == "TextButton7" then
				local val = XorO(space)
				row3 = row3 + val
				col1 = col1 + val
				diag2 = diag2 + val
			elseif space.Name == "TextButton8" then
				local val = XorO(space)
				row3 = row3 + val
				col2 = col2 + val
			elseif space.Name == "TextButton9" then
				local val = XorO(space)
				row3 = row3 + val
				col3 = col3 + val
				diag1 = diag1 + val
			end
		end
	end

	-- check all sets of 3 spaces for a win
	local winRow1 = checkWinValue(row1)
	if winRow1 ~= nil then
		return true, winRow1
	end

	local winRow1 = checkWinValue(row1)
	if winRow1 ~= nil then
		return true, winRow1
	end

	local winRow2 = checkWinValue(row2)
	if winRow2 ~= nil then
		return true, winRow2
	end

	local winRow3 = checkWinValue(row3)
	if winRow3 ~= nil then
		return true, winRow3
	end

	local winCol1 = checkWinValue(col1)
	if winCol1 ~= nil then
		return true, winCol1
	end

	local winCol2 = checkWinValue(col2)
	if winCol2 ~= nil then
		return true, winCol2
	end

	local winCol3 = checkWinValue(col3)
	if winCol3 ~= nil then
		return true, winCol3
	end

	local winDiag1 = checkWinValue(diag1)
	if winDiag1 ~= nil then
		return true, winDiag1
	end

	local winDiag2 = checkWinValue(diag2)
	if winDiag2 ~= nil then
		return true, winDiag2
	end

	return false, nil
end

local function checkGameState ()
	-- check for three in a row
	local win, winner = threeInARow()
	if win then
		return true, winner
	end
	-- check if board is full
	local spaces = board.SurfaceGui:GetChildren()
	for i, space in pairs(spaces) do
		if space:IsA("TextButton") and space.Text == "" then
			return false, nil
		end
	end
	return true, nil
end

local function sendGameOver (winner)
	print("Game Over!")
	ChatService:Chat(board, "Game Over!")
	if winner ~= nil then
		ChatService:Chat(board, string.format("%s is the winner", winner))
	end
	ChatService:Chat(board, "Send 'clear' in chat to clear the board and play again")
end

local function playTicTacToe ()
	local gameover, winner = checkGameState ()
	if gameover and not gameoverSent then
		sendGameOver(winner)
		gameoverSent = true
	end
end

local function resetBoard ()
	print("resetting board")
	local spaces = board.SurfaceGui:GetChildren()
	for _, space in pairs(spaces) do
		if space:IsA("TextButton") then
			space.Text = ""
		end
	end
	gameoverSent = false
end

local function addPlayerMark(position,mark)
	local spaces = board.SurfaceGui:GetChildren()
	for _, space in pairs(spaces) do
		if space:IsA("TextButton") and space.Text == "" and string.match(space.Name,position) then
			space.Text = mark
		end
	end
end

function validSpace(msg)
	if tonumber(msg) > 0 and tonumber(msg) < 10 then
		return true
	end
	return false
end

local function addComputerMark(mark)
	--Randomly choose a space for now
	local spaces = board.SurfaceGui:GetChildren()
	local spaceFound = false
	while not spaceFound do
		local url = "http://localhost:5000/qiskit"
		local res = HTTPService:GetAsync(url)
		local data = HTTPService:JSONDecode(res)
		local random = tostring(data.number)
		for _, space in pairs(spaces) do
			if space:IsA("TextButton") and space.Text == "" and string.match(space.Name,random) then
				space.Text = mark
				spaceFound = true
			end
		end
	end
end

game.Players.PlayerAdded:Connect(function(player)
	player.Chatted:Connect(function (msg) 
		if msg == "clear" then
			resetBoard()
		end
		if validSpace(msg) and not gameoverSent then
			addPlayerMark(msg,playerMark)
			playTicTacToe()
			wait(2)
			if not gameoverSent then
				addComputerMark(computerMark)
				playTicTacToe()
			end
		end
	end)
end)

RunService.Heartbeat:Connect(playTicTacToe)
