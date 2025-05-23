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
('Tetris', 10.000, 200, 8), 
('Super Mario 64', 50.000, 150, 3), 
('The Legend of Zelda: Ocarina of Time', 60.000, 180, 3), 
('Doom', 30.000, 220, 8), 
('Ms. Pac-Man', 15.000, 210, 3), 
('Minecraft', 30.000, 250, 8), 
('The Legend of Zelda', 40.000, 140, 3), 
('Super Mario Bros.', 30.000, 200, 3), 
('The Oregon Trail', 20.000, 130, 8), 
('World of Warcraft', 40.000, 160, 8), 
('Sid Meiers Civilization IV', 50.000, 190, 8), 
('Final Fantasy VI', 60.000, 180, 3), 
('SimsCity', 25.000, 110, 8), 
('Quake', 30.000, 140, 8), 
('Counter-Strike', 20.000, 150, 8), 
('Grand Theft Auto III', 50.000, 130, 8), 
('Half-Life 2', 60.000, 160, 8), 
('Rise of the Tomb Raider', 60.000, 100, 8), 
('Space Invaders', 15.000, 200, 8), 
('Zork', 10.000, 110, 8), 
('Diablo II', 40.000, 120, 8), 
('GoldenEye 007', 50.000, 90, 3), 
('Microsoft Flight Simulator X', 60.000, 80, 8), 
('Final Fantasy VII', 60.000, 200, 3), 
('Halo: Combat Evolved', 50.000, 160, 3), 
('StarCraft II: Wings of Liberty', 50.000, 170, 8), 
('Mortal Kombat', 20.000, 180, 8), 
('Donkey Kong', 15.000, 150, 3), 
('Myst', 30.000, 140, 8), 
('Pokémon Red & Blue', 30.000, 200, 3), 
('The Sims', 30.000, 130, 8), 
('Wolfenstein 3D', 20.000, 110, 8), 
('Super Mario Kart', 40.000, 120, 3), 
('Red Dead Redemption', 60.000, 100, 8), 
('Galaga', 10.000, 250, 8), 
('Fallout 3', 50.000, 90, 8), 
('Braid', 20.000, 80, 8), 
('Portal 2', 40.000, 110, 8), 
('Castlevania', 30.000, 150, 8), 
('Pong', 10.000, 180, 8), 
('ESPN NFL 2K5', 30.000, 120, 8), 
('BioShock', 60.000, 170, 8), 
('Call of Duty 2', 50.000, 160, 8), 
('Super Smash Bros.', 50.000, 200, 3), 
('Gran Turismo 3', 40.000, 180, 3), 
('Resident Evil 4', 60.000, 150, 8), 
('Guitar Hero', 50.000, 140, 8), 
('Angry Birds', 1.000, 300, 14), 
('Dota 2', 30.000, 220, 8), 
('Kings Quest III: To Heir Is Human', 20.000, 100, 8);
--


