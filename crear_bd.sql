-- PARTE 1
create database PuertoGames2025
go
USE PuertoGames2025;
GO

--
CREATE TABLE Plataformas(
    id_plataforma INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Videojuegos(
    id_videojuego INT PRIMARY KEY IDENTITY(1,1),
    titulo VARCHAR(50) NOT NULL,
    precio INT NOT NULL DEFAULT 0,
    stock INT NOT NULL CHECK (stock>=0) DEFAULT 0,
    id_plataforma INT NOT NULL
);
ALTER TABLE Videojuegos ADD CONSTRAINT fk_videojuego_plataforma 
FOREIGN KEY (id_plataforma) REFERENCES Plataformas(id_plataforma);
--
insert into Plataformas values
('PlayStation 5'),
('PlayStation 4'),
('Xbox Series X'),
('Xbox One'),
('Nintendo Switch'),
('Wii U'),
('Nintendo 3DS'),
('PC (Windows)'),
('Steam Deck'),
('PlayStation Vita'),
('Xbox 360'),
('PlayStation 3'),
('Nintendo Wii'),
('Android'),
('iOS');
--
insert into Videojuegos (titulo, precio, stock, id_plataforma) values
('Tetris', 10000, 200, 8), 
('Super Mario 64', 50000, 150, 3), 
('The Legend of Zelda: Ocarina of Time', 60000, 180, 3), 
('Doom', 30000, 220, 8), 
('Ms. Pac-Man', 15000, 210, 3), 
('Minecraft', 30000, 250, 8), 
('The Legend of Zelda', 40000, 140, 3), 
('Super Mario Bros.', 30000, 200, 3), 
('The Oregon Trail', 20000, 130, 8), 
('World of Warcraft', 40000, 160, 8), 
('Sid Meiers Civilization IV', 50000, 190, 8), 
('Final Fantasy VI', 60000, 180, 3), 
('SimsCity', 25000, 110, 8), 
('Quake', 30000, 140, 8), 
('Counter-Strike', 20000, 150, 8), 
('Grand Theft Auto III', 50000, 130, 8), 
('Half-Life 2', 60000, 160, 8), 
('Rise of the Tomb Raider', 60000, 100, 8), 
('Space Invaders', 15000, 200, 8), 
('Zork', 10000, 110, 8), 
('Diablo II', 40000, 120, 8), 
('GoldenEye 007', 50000, 90, 3), 
('Microsoft Flight Simulator X', 60000, 80, 8), 
('Final Fantasy VII', 60000, 200, 3), 
('Halo: Combat Evolved', 50000, 160, 3), 
('StarCraft II: Wings of Liberty', 50000, 170, 8), 
('Mortal Kombat', 20000, 180, 8), 
('Donkey Kong', 15000, 150, 3), 
('Myst', 30000, 140, 8), 
('Pokémon Red & Blue', 30000, 200, 3), 
('The Sims', 30000, 130, 8), 
('Wolfenstein 3D', 20000, 110, 8), 
('Super Mario Kart', 40000, 120, 3), 
('Red Dead Redemption', 60000, 100, 8), 
('Galaga', 10000, 250, 8), 
('Fallout 3', 50000, 90, 8), 
('Braid', 20000, 80, 8), 
('Portal 2', 40000, 110, 8), 
('Castlevania', 30000, 150, 8), 
('Pong', 10000, 180, 8), 
('ESPN NFL 2K5', 30000, 120, 8), 
('BioShock', 60000, 170, 8), 
('Call of Duty 2', 50000, 160, 8), 
('Super Smash Bros.', 50000, 200, 3), 
('Gran Turismo 3', 40000, 180, 3), 
('Resident Evil 4', 60000, 150, 8), 
('Guitar Hero', 50000, 140, 8), 
('Angry Birds', 1000, 300, 14), 
('Dota 2', 30000, 220, 8), 
('Kings Quest III: To Heir Is Human', 20000, 100, 8);
--


