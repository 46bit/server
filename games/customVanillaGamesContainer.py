#-------------------------------------------------------------------------------
# Copyright (c) 2014 Gael Honorez.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Public License v3.0
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/gpl.html
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#-------------------------------------------------------------------------------

from .gamesContainer import  gamesContainerClass
from .vanillaGame import vanillaClass
from PySide import QtSql

import games.vanillaGame
from games.vanillaGame import vanillaClass

class customVanillaGamesContainerClass(gamesContainerClass):
    '''Class for custom Nuke for the win games'''

    def __init__(self, db, parent = None):
        super(customVanillaGamesContainerClass, self).__init__("vanilla", "Vanilla", db, parent)

        

        self.betaPass = False

        self.parent = parent

    def addBasicGame(self, player, newgame, gamePort):
        
        playerLogin = player.getLogin()
        playerUuid = player.getId()
        playerState = player.getAction()
        session = player.getSession()
        
        gameUuid = self.createUuid(playerUuid)
        
        if playerState == "PLAYING" :
            return False
        elif playerState == "HOST" :
            return False
        elif playerState == "JOIN" :
            return False
        
        # check if the host is already hosting something.
        for game in self.games:
            if game.getLobbyState == 'open' :
                if game.getHostName() == playerLogin :
                    return False
                if game.getHostId() == session :
                    return False
        
        ngame = vanillaClass(gameUuid, self)
        ngame.setLobbyState('Idle')
        ngame.setGameHostName(playerLogin)
        ngame.setGameHostUuid(playerUuid)
        ngame.setGameHostPort(gamePort)
        ngame.setGameHostLocalPort(gamePort)
        ngame.setGameName(newgame)
        ngame.setTime()
        self.games.append(ngame)
        return ngame